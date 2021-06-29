from math import inf
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
text_speech = pyttsx3.init()
voices = text_speech.getProperty('voices')
text_speech.setProperty('voice',voices[0].id) #voice
text_speech.say('Hey, I am Robin...How may I help you...')
text_speech.runAndWait()

def robin_talk(userText):
    text_speech.say(userText)
    text_speech.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'robin' in command:
                command = command.replace('robin','')
                print(command)
                # robin_talk(command)
    except:
        print("Error in Listening....")
    return command

def search():
    command = listen()
    if 'play' in command:
        command = command.replace('play','')
        robin_talk('Playing '+command)
        print('Playing '+command)
        pywhatkit.playonyt('Playing'+command)
    elif 'time' in command:
        currTime = datetime.datetime.now().strftime('%I:%M %p')
        robin_talk('Current Time is'+currTime)
        print('Current Time is'+currTime)
    elif 'search' in command:
        srch = command.replace('search','')
        info = wikipedia.summary(srch,1)
        # pywhatkit.info(srch,1)
        robin_talk(info)
        print(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        robin_talk(joke)
        print(joke)
    elif 'date' in command:
        currDate = datetime.datetime.now().strftime("%d %B, %Y")
        robin_talk("Today's Date is"+currDate)
        print("Today's Date is "+currDate)
    elif 'close' in command:
        robin_talk("Okay, it's time for me to leave....Good Bye")
        print("Okay, it's time for me to leave....Good Bye")
        quit()
    else:
        robin_talk('Can you please Repeat....')
        print('Can you please Repeat....')
    

while True:
    search()