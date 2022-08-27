import speech_recognition as sr
import pyttsx3 as ptt
import datetime
import pywhatkit
import wikipedia
import pyjokes
import subprocess

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
            else:
                talk("can't hear you")
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
    elif 'tell me about' or 'info' in command:
        look_for = command.replace('tell me about', '') , command.replace('info', '')
        info = wikipedia.summary(look_for, 2)
        print(info)
        talk(info)
    elif 'jokes' in command:
        talk('let me tell you something funny' + pyjokes.get_joke())
    elif 'on date' in command:
        talk('yes of course. But we have to do it virtually')
    elif 'open' in command:
        app = command.replace('open', '')
        talk('opening' + app)
        subprocess.call(app)
    else:
        talk('showing relevant results')
        pywhatkit.search(command)

run_alexa()