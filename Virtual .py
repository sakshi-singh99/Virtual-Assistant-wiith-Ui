
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import time
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from VirtualUI import Ui_VirtualAssistance


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print (voices[0].id)
engine.setProperty('voices',voices[1].id)


#TO CONVERT TEXT TO SPPECH
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#TO WISH
def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<10:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am Prisa, tell me how can i help you...")  

#SEND EMAIL
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("nishasakshi999@gmail.com","Pratiksha@99")
    server.sendmail('nishasakshi999@gmail.com',to,content)
    server.close()     


class MainThread(QtCore.QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution

    #TO CONVERT SPEECH TO TEXT
    def takecommand(self):
        r= sr.Recognizer()
        with sr.Microphone() as source:
            print("listening....")
            r.pause_threshold=1
            audio = r.listen(source,timeout=1,phrase_time_limit=5)

        try:
            print("Recognizing....")
            self.query = r.recognize_google(audio,language='en-in')
            print(f"user said: {self.query}")
        except Exception as e:
            speak("say that again, please....")
            return "none"
        return self.query

    #FOR TASK EXECUTION        
    def TaskExecution(self):
        #speak("hello")
        #takecommand()
        wish()
        while True:
        #if 1:

            self.query = self.takecommand()

            #LOGIC BUILDING FOR TASK
            #TO OPEN NOTEPAD
            if "open notepad" in self.query:
                npath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories" 
                os.startfile(npath)

            #TO OPEN cmd
            elif "open command prompt" in self.query:
                os.system("start cmd")

            #OPEN CAMERA
            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret,img=cap.read()
                    cv2.imshow("WebCam",img)
                    k=cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindow() 

            #OPEN MUSIC
            elif "play music" in self.query:
                music_dir = "F:\\songs"
                songs = os.listdir(music_dir)
                rd=random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir,song))

            #FOR IP ADDRESS
            elif  "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")
                
            #SEARCH ON WIKIPEDIA
            elif "wikipedia" in self.query:
                speak("searching wikipedia....")
                self.query=self.query.replace("wikipedia","")
                result= wikipedia.summary(self.query,sentences=2)
                speak("According to wikipedia")
                speak(result)

            #OPEN YOUTUBE    
            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            #OPEN INSTAGRAM
            elif "open instagram" in self.query:
                webbrowser.open("www.instagram.com")

            #OPEN GOOGLE
            elif "open google" in self.query:
                speak("SAKSHI what should i search on google")
                cm=self.takecommand()
                webbrowser.open(f"{cm}")
                webbrowser.open("www.google.com")

            #OPEN WHATSAPP
            elif "send message" in self.query:
                kit.sendwhatmsg("+918789676457","Hii",20,31)

            #PLAY SONG ON YOUTUBE
            elif "play song on youtube" in self.query:
                kit.playonyt("intenstion")

            #SEND EMAIL
            elif "email to sakshi" in self.query:
                try:
                    speak("what should i say?")
                    content=self.takecommand()
                    to="nishasakshi999@gamil.com"
                    sendEmail(to,content)
                    speak("email has been send to sakshi")

                except Exception as e:
                    print(e)
                    speak("sorry,i am not able to send this email to sakshi")

            #PRAISE
            elif "do you love me" in self.query:
                speak("yes i love you so much you are a amazing soul")        

            #NO WORK
            elif "no thanks" in self.query:
                speak("Thanks for using me,Have a good day")
                sys.exit()

            #ASK FOR OTHER TASK
            speak("hey SAKSHI,do you have any other work")
                
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VirtualAssistance()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie=QtGui.QMovie("C:/Users/SAKSHI/Desktop/final year project/image/ui1.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()  
        self.ui.movie=QtGui.QMovie("../../../Users/SAKSHI/Desktop/final year project/image/p.png")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer =QTimer(self)
        timer.start(1000)
        startExecution.start()
        

app = QApplication(sys.argv)
prisa=Main()
prisa.show()
exit(app.exec_())    










                 
            
