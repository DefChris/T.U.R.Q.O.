import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os.path

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def greeting():
 hour = int(datetime.datetime.now().hour)
 if hour>=0 and hour<12:
    speak("Good Morning!")

 elif hour>=12 and hour<18:
  speak("Good Afternoon")

 else:
  speak("Good Evening")

 speak('My name is Turqo, your Artificial intelligence assistant,, Please tell me how I may help you')

def username():
  speak("What should i call you")
  uname = takeCommand()
  speak("Welcome, ")
  speak(uname)
     
  print("#####################")
  print("Welcome", uname)
  print("#####################")

def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

  try:
    print("Recognizing...")
    query = r.recognize_google(audio, language='en-US')
    print(f"User said '{query}'\n ")

  except Exception as e:
    print("I'm sorry can you say that again please")
    speak("I'm sorry can you say that again please")
    return "None"
  return query

username()

if __name__=='__main__':
  greeting()
  while True: 
    query = takeCommand().lower()

    if 'wikipedia' in query:
      speak('Searching Wikipedia...')
      query = query.replace("wikipedia", "")
      results = wikipedia.summary(query, sentences=4)
      speak("According to Wikipedia")
      print(results)
      speak(results)

    elif 'open youtube' in query:
      webbrowser.open("www.youtube.com")

    elif 'open google' in query:
      webbrowser.open("www.google.com")

    elif 'search on google' in query:
      speak('Searching on google')
      query = query.replace("search on google", "")
      webbrowser.open("https://www.google.com/search?q=" + query)

    elif 'the time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S")
      speak(f"The current time is {strTime}")

    elif 'open code' in query:
      codePath = "C:/Users/Christian Jousma/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code/Visual Studio Code"
      os.startfile(codePath)
    
    elif 'exit' in query:
      speak("Thanks for giving me your time")
      print("Shutting T.U.R.Q.O. down")
      exit()