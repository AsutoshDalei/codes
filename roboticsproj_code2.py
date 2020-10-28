#Project has been successfully finished and demonstrated. 28th of October, 2020
#SHIVIKA BISARIA CRISTIANA JOHN SHIVAM DUBEY ASUTOSH DALEI

import speech_recognition as sr
#import RPi.GPIO as GPIO
import sys
#_,flr=sys.argv
from time import sleep
#GPIO.setmode(GPIO.BCM)
import pyttsx3
import requests
import json
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


'''in11=18
in12=23
in21=24
in22=25
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(in11, GPIO.OUT)
GPIO.setup(in12, GPIO.OUT)
GPIO.setup(in21, GPIO.OUT)
GPIO.setup(in22, GPIO.OUT)
GPIO.output(in11 , 0)
GPIO.output(in12 , 0)
GPIO.output(in21, 0)
GPIO.output(in22, 0)'''
#Assuming that we have 3 floors: 0 1 2 3 4 5 6 7
#https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/#:~:text=The%20design%20of%20the%20Raspberry,common%20(connect%20them%20together).
#https://circuitdigest.com/microcontroller-projects/raspberry-pi-remote-controlled-car

def xmotor(d):
    if d==0:                            #0 is + or forward, 1 is - or backward
        print("x axis up")
        #GPIO.output(in11,GPIO.HIGH)
        #GPIO.output(in12,GPIO.LOW)
        sleep(1)
        #GPIO.output(in11,GPIO. LOW)
        #GPIO.output(in12,GPIO.LOW)

    elif d==1:
        #GPIO.output(in11,GPIO.LOW)
        #GPIO.output(in12,GPIO.HIGH)
        print("x axis down")
        sleep(1)
        #GPIO.output(in11,GPIO. LOW)
        #GPIO.output(in12,GPIO.LOW)
    else:
        #GPIO.output(in11,GPIO.LOW)
        #GPIO.output(in12,GPIO.LOW)
        print("x axis stop")

def ymotor(d):
    if d==0:                               #0 is + or forward, 1 is - or backward
        #GPIO.output(in21,GPIO.HIGH)
        #GPIO.output(in22,GPIO.LOW)
        print("y axis up")
        sleep(1)
        #GPIO.output(in21,GPIO.LOW)
        #GPIO.output(in22,GPIO.LOW)
    elif d==1:
        #GPIO.output(in21,GPIO.LOW)
        #GPIO.output(in22,GPIO.HIGH)
        print("y axis down")
        sleep(1)
        #GPIO.output(in21,GPIO.LOW)
        #GPIO.output(in22,GPIO.LOW)
    else:
        #GPIO.output(in21,GPIO.LOW)
        #GPIO.output(in22,GPIO.LOW)
        print("y axis stop")

#Assuming we always start from ground (0)
def control(flr1):
    a,b=int(flr1/2),int(flr1%2)
    for x in range(2):
        for i in range(b):
            xmotor(x)
        for j in range(a):
            ymotor(x)
        if(x==0):
            print('click')

def main(flr):
    #flr=int(input("Please enter your floor: "))
    if flr in range(8):
        print(f'going to floor {flr}')
        say(f"going to floor {flr}")
        control(flr)
        say(f"pressed floor number {flr}")
    else:
        say('I did not get you')

#main(int(flr))

if 'Robo' in listen():
    say("kindly tell your required floor")
    #main(int(listen))
    a=listen()
    main(int(a))
else:
    print('I did not get you')



'''                      O
                        \ /
                         |
                        / \
|-------------------------|
|                         |
|                         |
|    6                7   |
|                         |
|                         |
|    4               5    |
|                         |
|                         |
|    2               3    |
|                         |
|                         |
|    0               1    |
--------------------------- '''
