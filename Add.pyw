import cv2

def addition(txt, txt1):
    with open('id_name.txt', 'a',encoding="windows-1251") as file:
        file.write(txt.get()+' ')
    
    with open('id_name.txt', 'a',encoding="windows-1251") as file:
        file.write(txt1.get()+'\n')
        
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # ширина
    cam.set(4, 480) # высота

    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_id=txt.get()

# выборка
    count = 0
    while(True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
        # сохранение фотографий
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff # нажмите ESC чтобы закрыть камеру
        if k == 27:
            break
        elif count >= 30: 
             break

    cam.release()
    cv2.destroyAllWindows()







