import speech_recognition as sr
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

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

GPIO.setup(in11,GPIO.OUT)
GPIO.setup(in12,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)

GPIO.setup(in21,GPIO.OUT)
GPIO.setup(in22,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)

GPIO.output(in11,GPIO.LOW)
GPIO.output(in12,GPIO.LOW)
GPIO.output(in21,GPIO.LOW)
GPIO.output(in22,GPIO.LOW)
#Assuming that we have 3 floors: 0 1 2 3
#https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/#:~:text=The%20design%20of%20the%20Raspberry,common%20(connect%20them%20together).
if int(flr)==0:
    # click ground

elif int(flr)==1:

    #click 1
elif int(flr)==2:
    #click 2
elif int(flr)==3:
    #click 3
