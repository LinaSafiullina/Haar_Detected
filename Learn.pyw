import cv2
import numpy as np
from PIL import Image
import os

def learning():

    path = 'dataset'

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

# получение данных по фотографиям
    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
        faceSamples=[]
        ids = []
        for imagePath in imagePaths:
            img = cv2.imread(imagePath)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faceSamples.append(img)
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            ids.append(id)
        return faceSamples,ids  
   
    print ("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces,ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))


    recognizer.write('trainer.yml') 


    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))


