import speech_recognition as sr
import pyttsx3 as ptt
import datetime
import pywhatkit
import wikipedia

listener = sr.Recognizer()
alexa = ptt.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[0].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("Now it's is " + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing '+ song)
        pywhatkit.playonyt(song)
    elif 'tell me about' or 'info':
        look_for = command.replace('tell me about', '') , command.replace('info', '')
        info = wikipedia.summary(look_for, 2)
        talk(info)

run_alexa()