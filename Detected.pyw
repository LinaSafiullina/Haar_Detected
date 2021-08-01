import cv2

def checking():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);

    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 0

# запуск видео 
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # ширина
    cam.set(4, 480) # высота

# минимальный размер окна
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    k=0
    list=[' ']
    while True:
    
        ret, img =cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize = (int(minW), int(minH)))
    
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        
            if (confidence < 100):
            
                out_file=open('input.txt','a',encoding="windows-1251")
                outR_file=open('input.txt','r',encoding="windows-1251")
                in_file= open('id_name.txt', 'r',encoding="windows-1251")
                for line in in_file:
                    k=0
                    if str(id) in line:
                        for elem in list:
                            if elem==line:
                                k=k+1
                        if k==0:
                            list.append(line)
                            out_file.write(list[len(list)-1])
                            print(list[len(list)-1])
                    
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
        
            cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
    
        cv2.imshow('camera',img) 

        k = cv2.waitKey(10) & 0xff # нажмите ESC чтобы закрыть камеру
        if k == 27:
            break

    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
