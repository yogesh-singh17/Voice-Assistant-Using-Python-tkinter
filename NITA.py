
import wolframalpha
import pywhatkit 
import translator
from translator import translate
import pyttsx3 
import time
import tkinter
import covid_data
from covid_data import covid_d
import tkinter.ttk as ttk
import imagetotxt
from imagetotxt import imgtotxt
import imagetoword
from imagetoword import Docx
import Autocorrect
from Autocorrect import autocorrect_text
import PIL
from PIL import Image, ImageTk
from tkinter import *
import threading
import pytube
from pytube import YouTube
import json 
import tqdm
from tqdm import tqdm
import random 
import operator 
import speech_recognition as sr 
import datetime 
import wikipedia 
import webbrowser 
import os 
import winshell 
import pyjokes 
import feedparser 
import smtplib 
import time 
import getpass
import glob
import requests 
import shutil

#from twilio.rest import Client 
import clint.textui
from clint.textui import progress  
import bs4
from bs4 import BeautifulSoup 
import win32com.client as wincl 
import urllib
from urllib.request import urlopen 
from tkinter import messagebox,filedialog
import sys
#sys.setrecursionlimit(10**6)
#threading.stack_size(10**8)
 

win=Tk()

win.geometry("405x450+432+133")
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) 
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)

flag=0
breakloop=0
contact_loc=os.getcwd()+"\\"+"contacts.txt"
nita_loc=os.getcwd()+"\\"+"NITA.txt"
#fileSizeInBytes=0


def Start():
    
    #print(wishthread.is_alive())
    tcomm=threading.Thread(target=takeCommand)
    tcomm.start()
    #print(tcomm.is_alive())
    
    #pass

def Stop():
    exit()

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait()

def wishMeThread(): 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        #Entry1.delete("1.0",END)
       
        Entry1.insert(END,"Good Morning!")
        
        speak("Good Morning!")
        
            
    
    elif hour>=12 and hour<18:
        Entry1.delete("1.0",END)
       
        Entry1.insert(END,"Good Afternoon!")
        #print("Good afternoon")
        speak("Good Afternoon!")   
        #Entry1.insert(END,"Good Afternoon!")

    else:
        Entry1.delete("1.0",END)
    
        Entry1.insert(END,"Good Evening!")
        speak("Good Evening!")  
        #speak("Baku")
        
    Entry1.delete("1.0",END)
    Entry1.insert(END,"I am Nita, Sir.\r Please tell me how may I help you")
    speak("I am Nita, Sir. Please tell me how may I help you")  
    
    
#def tComm():
    

def takeCommand(): 
    global flag,breakloop,tcomm
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Listening...")
        Entry1.delete("1.0", END)
        Entry1.insert(END,"Listening...")  
      
        #r.energy_threshold=10
        r.pause_threshold = 1

        audio = r.record(source,duration=6)

    try:
        #print("Recognizing...")  
        Entry1.delete("1.0", END)
        Entry1.insert(END,"Recognizing...")  
        query = r.recognize_google(audio, language='en-in')
        #print(query)
        #Entry1.insert(END,query)
        time.sleep(2)
    except Exception as e:
        # print(e)    
        Entry1.delete("1.0", END)
        Entry1.insert(END,"Say that again please")  
        speak("Sorry I didn't get that, Say that again please")
        query="None"
    #while True:
    if query=="None":
        Entry1.delete("1.0",END)
        Entry1.insert(END,"Press the \"Start\" Button to give query. ")
    else:
        work(query)
        time.sleep(2)
          
    
def takeCommand2(): 
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Listening...")
        Entry1.delete("1.0", END)
        Entry1.insert(END,"Listening...")  
      
        #r.energy_threshold=10
        r.pause_threshold = 1

        audio = r.record(source,duration=7)

    try:
        #print("Recognizing...")  
        Entry1.delete("1.0", END)
        Entry1.insert(END,"Recognizing...")  
        query = r.recognize_google(audio, language='en-in')
        #print(query)
        Entry1.insert(END,query)

    except Exception as e:
        # print(e)    
        Entry1.delete("1.0", END)
        Entry1.insert(END,".....")  
        #print("Say that again please")
        return "None"
    return query

def Download():
    Donethread=threading.Thread(target=Done)
    Donethread.start()
def Done():
    global flag,breakloop,contact_loc
    try:
        if flag==1:
    
                string =Entry2.get()
                yt = YouTube(str(string))
                selectedVideo =yt.streams.filter(progressive=True,file_extension='mp4').first()
                #selectedVideo=yt.get('mp4','720p')
                username = getpass.getuser()
                dest="C:\\Users\\"+username+"\\Downloads\\"
                j=0
                for i in tqdm(range(100)):
                
                    Entry1.delete("1.0",END)
                    Entry1.insert(END,"Downloading : ")
                    time.sleep(0.05)
                    per=f"{j} %"
                    Entry1.insert(END,per)
                    time.sleep(0.05)
                    selectedVideo.download(dest)
                    j=j+1
                Entry1.delete("1.0",END)
                Entry1.insert(END,"Download Completed : 100%")
                time.sleep(3)
                
                
        elif flag==2:
            global name
            e_id=Entry2.get()
            contact=name+":"+e_id
            
            con=open(contact_loc,"a")
            con.write("\n"+contact)
            con.close()
            Entry1.delete("1.0",END)
            Entry1.insert(END,"Contact added")
            time.sleep(3)
        else:
            messagebox.showerror("INVALID INPUT", "Please give input again")
        flag=0
        breakloop=0
        time.sleep(2)
        Entry1.delete("1.0",END)
        Entry1.insert(END,"Press \"Start\" Button for another query .")
        
    except :
        messagebox.showerror("Error", "Can not perform the action now. Please Try again later.")
    Entry2.delete("0",END)
    flag=0
    breakloop=0
    
def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 
    
    # Enable low security in gmail 
    server.login('talesweekly@gmail.com', '##**ilpaiwfh))>>') 
    server.sendmail('talesweekly@gmail.com', to, content) 
    server.close() 
    
    #Entry1.delete("1.0",END)
    #Entry1.insert(END,"Press \"Start\" Button for another query .")

def work(query):
        global flag,breakloop,contact_loc,nita_loc
        query = query.lower() 
        
        chrome="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chromex', None,webbrowser.BackgroundBrowser(chrome))
            
        try:
            if 'wikipedia' in query: 
                speak('Searching Wikipedia...')
                query =  query.replace("wikipedia", "")
                results = wikipedia.summary( query, sentences=2)
                speak("According to Wikipedia")
                Entry1.delete("1.0", END)
                Entry1.insert(END, results)
                    #results
                speak(results)
            
            
                
            elif 'open youtube' in query: 
                speak("Here you go to Youtube\n") 
                webbrowser.get("chromex").open("youtube.com")
                #pywhatkit.search('www.youtube.com')

            elif 'open google' in query: 
                speak("Here you go to Google\n") 
                webbrowser.get("chromex").open("youtube.com")
                

            elif 'open stackoverflow' in query: 
                speak("Here you go to Stack Over flow.Happy coding") 
                webbrowser.get("chromex").open("stackoverflow.com") 

            elif 'wanna travel' in query or "want to travel" in query or "rail ticket" in query: 
                speak("Sure, let me help you in buying tickets") 
                webbrowser.get("chromex").open("irctc.co.in")
                
            elif 'virus' in query or 'corona' in query or 'covid' in query:
                breakloop=1
                Entry1.delete("1.0",END)
                Entry1.insert(END,"Processing...")
                #query="corona cases in India"
                query=query.split()
                Country=query[len(query)-1].capitalize()
                cases=covid_d(Country)
                Entry1.delete("1.0",END)
                Entry1.insert(END,"                               "+Country+"      \n")
                Entry1.insert(END,"Total Cases : "+str(cases[0])+"\n")
                Entry1.insert(END,"Active Cases : "+str(cases[1])+"\n")
                Entry1.insert(END,"Death Cases : "+str(cases[2])+"\n")
                Entry1.insert(END,"Cured Cases : "+str(cases[3])+"\n")
                speak("Total Cases : "+str(cases[0]))
                speak("Active Cases : "+str(cases[1]))
                speak("Death Cases : "+str(cases[2]))
                speak("Cured Cases : "+str(cases[3]))
                
                time.sleep(5)       
                breakloop=0    
                
                
                
                
            
            elif 'play music' in query or "play song" in query or "play random" in query:
                breakloop=1 
                speak("Here you go with music") 
                # music_dir = "G:\\Song" 
                username = getpass.getuser()
                music_dir = "C:\\Users\\"+username+"\\Music\\"
                
                songs = os.listdir(music_dir) 
                Entry1.delete("1.0",END)
                Entry1.insert(END,"Playing...")
                mp3Counter = len(glob.glob1(music_dir,"*.mp3"))
                ran=random.randint(1,mp3Counter)
                current_song = os.startfile(os.path.join(music_dir, songs[ran])) 
                time.sleep(5)
                breakloop=0
                
            elif 'the time' in query or 'tell time' in query: 
                h = datetime.datetime.now().strftime("%H")
                m = datetime.datetime.now().strftime("%M")    
                s = datetime.datetime.now().strftime("%S")    
                
                time1="Time : "+h+":"+m+":"+s  
                Entry1.delete("1.0",END)
                Entry1.insert(END,time1)
                speak(f"Sir, the time is {h} hours {m} minutes {s} seconds") 
                
            
            elif "send an email" in query or "send mail" in query or "send email" in query: 
                breakloop=1
                query=query.split("to")
                to=query[len(query)-1].strip().capitalize()
                file=open(contact_loc,"r")
                line=file.readlines()
                temp=0
                for i in line:
                    c=i.split(":")
                    if c[0]==to:
                        temp=1
                        to=c[1]
                        try: 
                            speak("What should I say?") 
                            content = takeCommand2() 
                            sendEmail(to, content) 
                            speak("Email has been sent !") 
                        except Exception as e: 
                            #print(e) 
                            speak("I am not able to send this email")   
                        break
                        
                if temp==0:
                    Entry1.delete("1.0",END)
                    Entry1.insert(END,"Email not found")
                    speak("Email not found")
                    
                breakloop=0


            elif  "your name" in query: 
                Entry1.insert(END,"NITA")
                speak("My friends call me Nita") 

            elif "send a file" in query or "send file" in query:
                Entry1.delete('1.0',END)
                Entry1.insert(END,"Select file..")
                time.sleep(2)
                send_file=filedialog.askopenfilename()
                #f= filedialog.askopenfilename()
                p="qr-filetransfer "+ send_file
                Entry1.delete('1.0',END)
                Entry1.insert(END,"Processing...")
                os.system(p)
                time.sleep()

            elif "send files" in query or "send multiple files" in query or 'send folder' in query or 'send a folder' in query:
                Entry1.delete('1.0',END)
                Entry1.insert(END,"Select folder..")
                time.sleep(2)
                send_folder=filedialog.askdirectory()
                #f= filedialog.askopenfilename()
                p="qr-filetransfer "+ send_folder + "/"
                Entry1.delete('1.0',END)
                Entry1.insert(END,"Processing...")
                os.system(p)
                time.sleep()

            elif "receive a file" in query or "receive file" in query:
                
                username = getpass.getuser()
                dest="C:\\Users\\"+username+"\\Downloads\\"
                #f= filedialog.askopenfilename()
                p="qr-filetransfer -r "+ dest
                Entry1.delete('1.0',END)
                Entry1.insert(END,"Processing...")
                os.system(p)
                time.sleep(1)




            elif "update contact" in query or "add a contact" in query or "add contact" in query:
                breakloop=1
                global name
                flag=2
                #con=open("contacts.txt","a")
                Entry1.delete("1.0",END)
                Entry1.insert(END,"What is the name of the contact?")
                speak("What is the name of the contact?")
                name=takeCommand2().capitalize()
                Entry1.delete("1.0",END)
                Entry1.insert(END,"Write the email of the contact down below and press button \"Done\"")
                speak("Write the email of the contact down below and press button")

            elif 'exit' in query: 
                speak("Thanks for giving me your time")
                Entry1.delete("1.0",END)
                Entry1.insert(END,"Closing")
                time.sleep(0.5)
                Entry1.insert(END,".") 
                time.sleep(0.5)
                Entry1.insert(END,".")
                time.sleep(0.5)
                Entry1.insert(END,".")
                time.sleep(0.5)
                win.destroy()

        
                
            elif 'joke' in query: 
                joke=pyjokes.get_joke()
                Entry1.delete("1.0",END)
                Entry1.insert(END,joke)
                speak(joke)
                
                
            elif "calculate" in query: 
                Entry1.delete("1.0",END)
                app_id = "E3V7RK-6XKWVPQTQX"
                client = wolframalpha.Client(app_id) 
                indx = query.lower().split().index('calculate') 
                query = query.split()[indx + 1:] 
                res = client.query(' '.join(query)) 
                answer = next(res.results).text 
                Entry1.insert(END,"The answer is " + str(answer)) 
                speak("The answer is " + answer) 

            elif 'search' in query:
                query=query.replace('search',"")
                pywhatkit.search(query)
            elif 'play' in query:
                query=query.replace('play',"")
                pywhatkit.playonyt(query)
                
                
            elif 'convert image to text' in query or 'convert image into text' in query:
                breakloop =1
                imgtotxt()
                Entry1.delete("1.0",END)
                Entry1.insert(END,"Converted Successfully ")
                time.sleep(3)
                breakloop=0
                
            
            elif "Correct spellings" in query or "correct spelling" in query or "autocorrect english" in query or "correct file" in query or "correct english" in query:
                breakloop=1
                autocorrect_text()
                Entry1.delete("1.0",END)
                Entry1.insert(END,"Corrected Successfully .")
                time.sleep(3)
                breakloop=0
                
            elif 'convert image to word'  in query or 'convert image into word'  in query:
                breakloop=1
                Docx()
                Entry1.delete("1.0",END)
                Entry1.insert(END,"Converted Successfully ")
                time.sleep(3)
                breakloop=0
        

            
    

            elif 'news' in query: 
                
                try: 
                    #jsonObj=urlopen('''http://newsapi.org/v2/top-headlines?country=in&apiKey=e0884690df40458c9b0d4f39f10c2c9a''')
                    jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=win&apiKey=e0884690df40458c9b0d4f39f10c2c9a''') 
                    data = json.load(jsonObj) 
                    i = 1
                    
                    speak('here are some top news from the times of india') 
                    #print("====== TIMES OF INDIA ====="+ '\n')
                    Entry1.delete("1.0",END)
                    Entry1.insert(END,"======== TIMES OF INDIA ========\n")
                    for item in data['articles']: 
                        #print(item['description']+'\n')
                        item1='*'+item['description']+'\n\n'
                        Entry1.insert(END,item1)
                        i += 1
                except Exception as e: 
                    Entry1.delete("1.0",END)
                    Entry1.insert(END,"Can not fetch now")#print(str(e))
                    speak("Can not fetch now")
                time.sleep(30)
            
            

            elif "don't listen" in query or "stop listening" in query: 
                speak("for how much time you want to stop Nita from listening commands") 
                a = int(takeCommand2()) 
                time.sleep(a) 
                
                #print(a)

            elif "where is" in query: 
                query = query.replace("where is", "") 
                location = query 
                speak("User asked to Locate") 
                speak(location) 
                webbrowser.get("chromex").open("https://www.google.nl/maps/place/" + location + "") 

            

            elif "write a note" in query: 
                speak("What should i write, sir") 
                note = takeCommand2() 
                file = open(nita_loc, 'w') 
                speak("Sir, Should i include date and time") 
                snfm = takeCommand2() 
                if 'yes' in snfm or 'sure' in snfm: 
                    strTime = datetime.datetime.now().strftime("%H:%M:%S") 
                    file.write(strTime) 
                    file.write(" :- ") 
                    file.write(note) 
                else: 
                    file.write(note) 
            
            elif "show note" in query: 
                speak("Showing Notes") 
                file = open(nita_loc, "r") 
                #print(file.read()) 
                speak(file.read(6)) 

            
            # NPPR9-FWDCX-D2C8J-H872K-2YT43 
            
            elif "weather" in query or "temperature" in query : 
                
                # Google Open weather website 
                # to get API of Open weather 
                
                breakloop =1
                query=query.split(" ")
                #print(query)
                q_len=len(query)
            
                api_key = "25ab53f2036e4480e80564ab721c3ecf"
                base_url = "http://api.openweathermap.org/data/2.5/weather?" 
                #"City name : ") 
                city_name = query[q_len-1]
                city_name=city_name.capitalize()
                complete_url = base_url + "q=" + city_name +"&appid=" + api_key 
                #print(complete_url)
                response = requests.get(complete_url) 
                x = response.json() 
                if x["cod"] != "404": 
                    y = x["main"]
                    
                    current_temperature = y["temp"]-273.15
                    current_humidity = y["humidity"] 
                    z = x["weather"] 
                    weather_desc = z[0]["description"] 
                    #print(" Temperature = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
                    Entry1.delete("1.0",END)
                    city_display="             City : " + city_name+"\n"
                    temp_display="Temperature : "+str(int(current_temperature))+ "C \n"
                    temp_speak="Temperature of" + city_name + "is" + str(int(current_temperature)) + "degree Celcius"
                    hum_display="Humidity : "+ str(current_humidity) +"% \n"
                    hum_speak="Humidity of"+city_name+"is"+str(current_humidity)+"percent"
                    weat_display="Description : "+str(weather_desc)+"\n"
                    weat_speak="Weather is " + str(weather_desc)
                    Entry1.insert(END,city_display)
                    Entry1.insert(END,temp_display)
                    Entry1.insert(END,hum_display)
                    Entry1.insert(END,weat_display)
                    speak(temp_speak)
                    speak(hum_speak)
                    speak(weat_speak)
                else: 
                    speak(" City Not Found ,Say The name again")
                    
                breakloop=0
                time.sleep(5)
                
        

            elif "open wikipedia" in query: 
                pywhatkit.search("www.wikipedia.com")  

            # most asked question from google Assistant 
            elif "will you be my girlfriend" in query or "will you be my gf" in query: 
                speak("I'm not sure about, may be you should give me some time") 


            elif 'who is' in query:

                query =  query.replace("who is", "")
                results = wikipedia.summary( query, sentences=2)
                Entry1.delete("1.0", END)
                Entry1.insert(END, results)
                    #results
                speak(results)
            
            elif 'download video' in query or 'download a video' in query:
                flag=1
                breakloop=1
                Entry1.delete("1.0",END)
                Entry1.insert(END,"Please put the video link in the box below and press the button")
                speak("Please put the video link in the box below and press the button")
                
            

            elif "translate" in query: 
                
                query=query.replace("translate","")
                Entry1.delete("1.0",END)
                Entry1.insert(END,query)
                time.sleep(0.5)
                t=translate(query)
                try:
                    t=t.split("+")
                    Entry1.delete("1.0",END)
                    q="Sentence : "+t[0]+"\n"
                    Entry1.insert(END,q)
                    tr="Translated : "+t[1]+"\n"
                    Entry1.insert(END,tr)
                    trs=t[1]+"\n"
                    speak(trs)
                    time.sleep(10)

                except:       
                    
                    Entry1.delete("1.0",END)
                    Entry1.insert(END,t)
                    speak(t)
                    time.sleep(5)
                # Command go here 
                # For adding more commands 
            else:
                try:
                    Entry1.delete("1.0",END)
                    Entry1.insert(END,"Processing...")
                    app_id = "E3V7RK-6XKWVPQTQX"
                    client = wolframalpha.Client(app_id) 
                    #indx = query.lower().split().index('calculate') 
                    #query = query.split()[indx + 1:] 
                    res = client.query(query) 
                    answer = next(res.results).text 
                    
                    
                    Entry1.delete("1.0",END)
                    Entry1.insert(END,"Query: "+str(query)+"\n")
                    Entry1.insert(END,"The answer is " + str(answer)) 
                    speak("The answer is " + answer) 
                    time.sleep(2)
                except:
                    Entry1.delete("1.0",END)
                    Entry1.insert(END,"Sorry, I didn't get it. Speak it again")
                    speak("Speak it again, Please")
                    time.sleep(0.5)
                
            
            if breakloop==0:
                Entry1.delete("1.0",END)
                Entry1.insert(END,"Press \"Start\" Button for another query .")
        except:
            flag=0
            breakloop=0
            Entry1.delete("1.0",END)
            Entry1.insert(END,"Press \"Start\" Button for another query .")


##################### GUI ############################






######################################################

               
if __name__ == '__main__': 
    
    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = '#d9d9d9' # X11 color: 'gray85'
    _ana1color = '#d9d9d9' # X11 color: 'gray85'
    _ana2color = '#ececec' # Closest X11 color: 'gray92'
    pycwd=os.getcwd()+"\\siri.png"
    icon=PhotoImage(file=pycwd)
    win.iconphoto(False,icon)
    win.geometry("405x450+432+133")
    win.title("N.I.T.A")
    win.configure(background="#000000")
    win.configure(highlightbackground="#d9d9d9")
    win.configure(highlightcolor="black")
    win.resizable(False, False)
    
    Label1 = Label(win)
    Label1.place(x=0, y=0,  height=450, width=405)
    Label1.configure(activebackground="#f9f9f9")
    Label1.configure(activeforeground="black")
    Label1.configure(background="#d9d9d9")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(foreground="#000000")
    Label1.configure(highlightbackground="#d9d9d9")
    Label1.configure(highlightcolor="black")
    pic_cwd=os.getcwd()+"\\"+'aurora.jpg'
    #photo_location = 'aurora.jpg'
    global _img0
    _img0 = ImageTk.PhotoImage(file=pic_cwd)
    Label1.configure(image=_img0)
    Label1.configure(justify='right')
    Label1.configure(relief="raised")
    Label1.configure(text='''Label''')
    
    Entry1 = Text(win)
    Entry1.place(x=13, y=13, height=225, width=360)
    Entry1.configure(background="#121212")
    # Entry1.configure(disabledforeground="#a3a3a3")
    Entry1.configure(font="-family {Times New Roman} -size 14 ")
    Entry1.configure(foreground="#ffffff")
    Entry1.configure(highlightbackground="#d9d9d9")
    Entry1.configure(highlightcolor="white")
    Entry1.configure(insertbackground="white")
    Entry1.configure(selectbackground="#aed669")
    Entry1.configure(selectforeground="white")
    Entry1.configure(state=NORMAL)
    
    scrollb = ttk.Scrollbar(command=Entry1.yview)
    scrollb.place(x=373, y=13,height=224)
    Entry1['yscrollcommand'] = scrollb.set
    
    
    Entry2 = Entry(win)
    Entry2.place(x=40, y=400, height=30, width=244)
    Entry2.configure(background="black")
    Entry2.configure(disabledforeground="#a3a3a3")
    Entry2.configure(font="-family {Courier New} -size 10")
    Entry2.configure(foreground="#ffffff")
    Entry2.configure(highlightbackground="#d9d9d9")
    Entry2.configure(highlightcolor="white")
    Entry2.configure(insertbackground="white")
    Entry2.configure(selectbackground="#aed669")
    Entry2.configure(selectforeground="white")
    
    Button1 = Button(win)
    Button1.place(x=300, y=400,  height=34, width=57)
    Button1.configure(activebackground="#ececec")
    Button1.configure(activeforeground="#000000")
    Button1.configure(background="#427b9f")
    Button1.configure(command= Download)
    Button1.configure(disabledforeground="#a3a3a3")
    Button1.configure(foreground="#d2face")
    Button1.configure(highlightbackground="#d9d9d9")
    Button1.configure(highlightcolor="black")
    Button1.configure(pady="0")
    Button1.configure(text='''Done''')
    
    Button2 = Button(win)
    Button2.place(x=50, y=300,  height=64, width=87)
    Button2.configure(activebackground="#f9f9f9")
    Button2.configure(activeforeground="#000000")
    Button2.configure(background="#427b9f")
    Button2.configure(command= Start)
    Button2.configure(disabledforeground="#a3a3a3")
    Button2.configure(font="-family {Times New Roman} -size 16 ")
    Button2.configure(foreground="#d2face")
    Button2.configure(highlightbackground="#d9d9d9")
    Button2.configure(highlightcolor="black")
    Button2.configure(pady="0")
    Button2.configure(text='''Start''')
    
    Button2_1 = Button(win)
    Button2_1.place(x=270, y=300,  height=64, width=87)
    Button2_1.configure(activebackground="#ececec")
    Button2_1.configure(activeforeground="#000000")
    Button2_1.configure(background="#427b9f")
    Button2_1.configure(command= Stop)
    Button2_1.configure(disabledforeground="#a3a3a3")
    Button2_1.configure(font="-family {Times New Roman} -size 16")
    Button2_1.configure(foreground="#d2face")
    Button2_1.configure(highlightbackground="#d9d9d9")
    Button2_1.configure(highlightcolor="black")
    Button2_1.configure(pady="0")
    Button2_1.configure(text='''Stop''')
    
    
    
    
    
    
    
    
    
    
    wishthread=threading.Thread(target=wishMeThread)
    wishthread.start()
    #print(wishthread.is_alive())
    #wishthread.join    
    #time.sleep(6)
    




win.mainloop()
