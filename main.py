import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
   #engine.say('Hey! I am Alexa!')
   #engine.say('What would you like to know from me?')
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')


    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is'+ time)
    elif 'who' in command:
        person = command.replace('who','')
        information = wikipedia.summary(person,2)
        print(information)
        talk(information)
    elif 'are you mad' in command:
        talk('Are you speaking about yourself dear!')
        print('Are you speaking about yourself dear!')
    elif 'I love you' in command:
        talk('I love you too')
        print('I love you too')
    elif 'joke' in command:
        Joke = pyjokes.getjoke()
        talk(Joke)
        print(Joke)
    else:
        talk('Repeat yourself please')


while True:
    run_alexa()