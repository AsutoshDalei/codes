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
    engine.setProperty('voice', voices[1].id)
    engine.say(r)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        say("Talk")
        audio_text = r.listen(source)
        sleep(3)
        print("Time over, thanks")
        try:
            print("Text: "+r.recognize_google(audio_text))
        except:
            say("Sorry, I did not get that")

def voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY"))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service: {0}".format(e))

    WIT_AI_KEY = "INSERT WIT.AI API KEY HERE"  # Wit.ai keys are 32-character uppercase alphanumeric strings
    try:
        print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))

'''GPIO.setup(in11,GPIO.OUT)
GPIO.setup(in12,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)

GPIO.setup(in21,GPIO.OUT)
GPIO.setup(in22,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)

GPIO.output(in11,GPIO.LOW)
GPIO.output(in12,GPIO.LOW)
GPIO.output(in21,GPIO.LOW)
GPIO.output(in22,GPIO.LOW)'''
#Assuming that we have 3 floors: 0 1 2 3 4 5 6 7
#https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/#:~:text=The%20design%20of%20the%20Raspberry,common%20(connect%20them%20together).

def xmotor(d):
    if d==0:                            #0 is + or forward, 1 is - or backward
        #GPIO.output(in11,GPIO.HIGH)
        #GPIO.output(in12,GPIO.LOW)
        print("x axis forward")
    elif d==1:
        #GPIO.output(in11,GPIO.LOW)
        #GPIO.output(in12,GPIO.HIGH)
        print("x axis backward")
    else:
        #GPIO.output(in11,GPIO.LOW)
        #GPIO.output(in12,GPIO.LOW)
        print("x axis stop")

def ymotor(d):
    if d==0:                               #0 is + or forward, 1 is - or backward
        #GPIO.output(in21,GPIO.HIGH)
        #GPIO.output(in22,GPIO.LOW)
        print("y axis forward")
    elif d==1:
        #GPIO.output(in21,GPIO.LOW)
        #GPIO.output(in22,GPIO.HIGH)
        print("y axis backward")
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
    else:
        say('I did not get you')

#main(int(flr))

listen()


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
