class User():
    import speech_recognition as sr
    #import RPi.GPIO as GPIO
    import sys
    #_,flr=sys.argv
    from time import sleep
    import pyttsx3
    import numpy as np
    import cv2 as cv2
    engine = pyttsx3.init()
    r = sr.Recognizer()

    face_cascade = cv2.CascadeClassifier(r'C:\Users\asuto\Desktop\cache\face.xml')
    eye_cascade = cv2.CascadeClassifier(r'C:\Users\asuto\Desktop\cache\eye.xml')

    def __init__(self,name):
        self.username=name
        self.task1=[]
        self.alarm1=[]
        self.load1=[]
    
    def say(self,r):
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', 125)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        self.engine.say(r)
        self.engine.runAndWait()

    def listen(self):
        r = self.sr.Recognizer()
        with self.sr.Microphone() as source:
            print("Kindly speak now:")
            #self.say(f"Hello {self.username}, kindly speak now")
            audio_text = r.listen(source)
            self.sleep(3)
            print("Time over, thanks")
            try:
                self.say("Did you say: "+r.recognize_google(audio_text))
                print(r.recognize_google(audio_text))
                return(r.recognize_google(audio_text))
            except:
                self.say("Sorry, I did not get that")
                return("Sorry")
    
    def view(self):
        cap = self.cv2.VideoCapture(0)
        #face_cascade = self.cv2.CascadeClassifier(r'C:\Users\asuto\Desktop\cache\face.xml')
        #eye_cascade = self.cv2.CascadeClassifier(r'C:\Users\asuto\Desktop\cache\eye.xml')
        while True:
            ret, img = cap.read()
            gray = self.cv2.cvtColor(img, self.cv2.COLOR_BGR2GRAY)
            #faces = face_cascade.self.cv2.detectMultiScale(gray, 1.3, 5)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                self.cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                eyes = self.eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    self.cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            
            img = self.cv2.putText(img, self.username, (x-20,y-20), self.cv2.FONT_HERSHEY_SIMPLEX ,1,(255, 0, 0), 3, self.cv2.LINE_AA) #blue font
            self.cv2.imshow('img',img)
            k = self.cv2.waitKey(30) & 0xff
            if k == 27:
                break
        cap.release()
        self.cv2.destroyAllWindows()

    def addtasks(self,x):
        self.task1.append(x)
    def addalarms(self,y):
        self.alarm1.append(x)
    def addloads(self,y):
        self.load1.append(x)

norm=User('Stranger')
asu=User('asutosh')
cup=User('robot2')

asu.task1=['light','Fan','Ac','Tv']
cup.task1=['Light','Fan','Ac','Tv']

asu.alarm1=['6 30','6 40','6 50','7','7 10']
cup.alarm1=['5 30','5 40','5 50','6','6 10']

#a=norm.listen()
a='I am Alexa'
print(a)
if 'Alexa' in a:
    norm.say('Could I know your name?')
    y=norm.listen()
    if 'Robo' in y:
        asu.say('Hello asutosh, how are you ? What can I do for you today?')
        asu.view()
        x=asu.listen()
        if x in asu.task1:
            asu.say(f'Ok, doing task turn on {x}')
        else:
            asu.say('I did not get you')
    elif 'test' in y:
        cup.say('Hello test, how are you ? What can I do for you today?')
        x=cup.listen()
        if x in asu.task1:
            cup.say(f'Ok, doing task turn on {x}')
        else:
            cup.say('I did not get you')
    else:
        norm.say('I do not know you')
        



