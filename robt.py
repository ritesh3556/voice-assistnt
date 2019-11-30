import pyttsx3 # module    python for text to speech
import speech_recognition as sr # speech module
import datetime # already install on pc  
import wikipedia
import webbrowser
import os  # operating system directory use

engine = pyttsx3.init('sapi5') # windows api   sapi5 is provide by microsoft
voices = engine.getProperty('voices') # get the voice as property
#print(voices) # print voices which are available
#print(voices[0].id) # print id of voice
engine.setProperty('voices', voices[0].id) # set the property of voice 



def speak(audio):
   engine.say(audio) # audio string speak by pc
   engine.runAndWait() 

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("i am ritesh how can i help you.....")            
def takeCommand():
    # it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold = 1
        audio =r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)
        print("Say that again please....")                 
        return "None"
    return query    
if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()    # if we are not use lower function then it will fail during the execution time because it takes as a small letter and capital letter word is tkane....
    # logic based on executing tasks based on query
        if 'wikipedia' in query:      # pip install wikipedia and set module to (import wikipedia)
            speak("searching on wikipedia....")
            #query =query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)   # two sentence is return because sentence = 2 speak two
            speak("According to wikipedia: ")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com") 
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")           
        elif "play music" in query:
            music_dir = 'E:\\songs'
            songs = os.listdir(music_dir) # list all the music files
            print(songs) # print list songs
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "time" in query:
            start_time= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" the time is : {start_time}")    
            print(f"the time is : {start_time}")
        elif "open visual studio" in query:
            c_path = "C:\\Users\\Ritesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(c_path) # startfile to start anything where the path is located and mentioned .
        elif "open d" in query:
            o = "D:"
            os.startfile(o)    
        elif "open chrome" in query:
            o="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(o)    

        elif "suno" in query:
            speak("ji boliye sir")    

        elif "exit" in query:
            print("YOUR PROGRAM IS CLOSE THANKYOU FOR USING ME AND HAVE A NICE DAY : ")
            speak("your program is close Thank  you for using me and have a nice day")
            exit()
                    