import os
import pyttsx3
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning')
    elif hour >= 12 and hour < 18:
        speak('Good AfterNoon')
    else:
        speak('Good Evening')

files = os.listdir()
files.remove("main.py")

def exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def intro():
    speak('I am The Clutter Cleaner.....')
def creating():
    
    speak("Creating Folders....")
    print("Creating Folders....")

def speakmoving():
    
    speak("Moving Files")
    print("Moving Files")

def showingstats():
    
    speak("Showing Stats")
    print("Showing Stats")

def CheckingFiles():
    
    speak('Checking Files ....')          
exists("Images")
exists("Docs")
exists("Media")
exists("Programs")

ImgExt = ['.png','.jpg','.jpeg']

Images = [file for file in files if os.path.splitext(file)[1].lower() in ImgExt]



DocsExt = ['.txt','.docx','.doc','.pdf','.html','.htm']

Docs = [file for file in files if os.path.splitext(file)[1].lower() in DocsExt]

Media  = ['.mp3','.mp4']

medias = [file for file in files if os.path.splitext(file)[1].lower() in Media]

ProgramExt  = ['.py','.js','.c','.cpp']

programs = [file for file in files if os.path.splitext(file)[1].lower() in ProgramExt]


# Moving The Files In The Folders
def move(folder,files):
    print(f"Moving {len(files)} Files To :{folder}")
    for file in files:
     os.replace(file,f"{folder}/{file}")

if __name__ == "__main__":
    WishMe()
    intro()
    creating()
    CheckingFiles()
    speakmoving()
    showingstats()
    move("Images",Images)    
    move("Docs",Docs)    
    move("Media",medias)
    move("Programs",programs)

    