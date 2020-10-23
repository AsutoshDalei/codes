import speech_recognition as sr
#import RPi.GPIO as GPIO
import sys
#_,flr=sys.argv
from time import sleep
import pyttsx3
import numpy as np
import cv2
#GPIO.setmode(GPIO.BCM)
engine = pyttsx3.init()
r = sr.Recognizer()

def say(r):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(r)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Kindly speak now:")
        say("Kindly speak now")
        audio_text = r.listen(source)
        sleep(3)
        print("Time over, thanks")
        try:
            say("Did you say: "+r.recognize_google(audio_text))
            print(r.recognize_google(audio_text))
            return(r.recognize_google(audio_text))
        except:
            say("Sorry, I did not get that")
            return("sorry")

if 'Internet' in listen():
    say("kindly tell your task")
    a=listen()
    say('Did you say?')
    
    print(a)
    say(a)
else:
    print('I did not get you')




#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier(r'C:\Users\asuto\Desktop\cache\face.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier(r'C:\Users\asuto\Desktop\cache\eye.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()