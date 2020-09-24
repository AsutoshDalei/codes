import speech_recognition as sr
#import RPi.GPIO as GPIO
from time import sleep
#GPIO.setmode(GPIO.BCM)
import pyttsx3
engine = pyttsx3.init()


def say(r):
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(r)
    engine.runAndWait()

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
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

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
    if d=='+':
        #GPIO.output(in11,GPIO.HIGH)
        #GPIO.output(in12,GPIO.LOW)
        print("x axis forward")
    elif d=='-':
        #GPIO.output(in11,GPIO.LOW)
        #GPIO.output(in12,GPIO.HIGH)
        print("x axis backward")
    else:
        #GPIO.output(in11,GPIO.LOW)
        #GPIO.output(in12,GPIO.LOW)
        print("x axis stop")

def ymotor(d):
    if d=='+':
        #GPIO.output(in21,GPIO.HIGH)
        #GPIO.output(in22,GPIO.LOW)
        print("y axis forward")
    elif d=='-':
        #GPIO.output(in21,GPIO.LOW)
        #GPIO.output(in22,GPIO.HIGH)
        print("y axis backward")
    else:
        #GPIO.output(in21,GPIO.LOW)
        #GPIO.output(in22,GPIO.LOW)
        print("y axis stop")

#Assuming we always start from ground (0)

def main(flr):
    if int(flr)==1:
        say("Okay")
        xmotor('+')
        #click servo
        print('click')
        xmotor('-')

    elif int(flr)==2:
        say("Okay")
        ymotor('+')
        #click servo
        print('click')
        ymotor('-')

    elif int(flr)==3:
        say("Okay")
        xmotor('+')
        ymotor('+')
        #click servo
        print('click')
        ymotor('-')
        xmotor('-')

    elif int(flr)==4:
        say("Okay")
        xmotor('+')
        xmotor('+')
        #click servo
        print('click')
        xmotor('-')
        xmotor('-')

    elif int(flr)==5:
        say("Okay")
        xmotor('+')
        ymotor('+')
        ymotor('+')
        #click servo
        print('click')
        ymotor('-')
        ymotor('-')
        xmotor('-')

    elif int(flr)==6:
        say("Okay")
        xmotor('+')
        xmotor('+')
        xmotor('+')
        #click servo
        print('click')
        xmotor('-')
        xmotor('-')
        xmotor('-')

    elif int(flr)==7:
        say("Okay")
        xmotor('+')
        ymotor('+')
        ymotor('+')
        ymotor('+')
        #click servo
        print('click')
        ymotor('-')
        ymotor('-')
        ymotor('-')
        xmotor('-')

    else:
        say("I did not get you, kindly repeat")
        flr=int(input("Pls enter your floor, again: "))
        if(flr not in range(0,8)):
            print("exit")
        else:
            main(flr)

flr=int(input("Pls enter your floor: "))
#flr=voice()  #takevoice input
main(flr)
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
-------------------------- '''
