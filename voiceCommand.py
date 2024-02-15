import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import openai
import pyjokes
import random
import os
import smtplib
import subprocess
import ecapture
import ecapture as ec
import pyaudio
import csv
from tkinter import *
import speedtest


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")
    
    speak("I am bhaarrvishya , plese tell me how may I help you")

'''
def chat(chatStr):
    #print(chatStr)
    openai.api_key = "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"
    chatStr += f"Utkarsh: {chatStr}\n Jarvis: "
    response = openai.ChatCompletion.create(
        model="text-davinci-003",
        prompt=chatStr,
    )
    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]



def ai(prompt):
    openai.api_key = "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"
    text = f"OpenAI response for Prompt: {prompt} \n ********************\n\n"
    try:
        response = openai.ChatCompletion.create(
            model="text-davinci-003",
            prompt=prompt,
        )
        # print(response["choices"][0]["text"])
        text += response["choices"][0]["text"]
        if not os.path.exists("Openai"):
            os.mkdir("Openai")

        # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
        with open(f"Openai/{''.join(prompt.split('search')[1:]).strip()}.txt", "w") as f:
            f.write(text)

    except openai.error.RateLimitError as e:
    # Handle the rate limit error here, you might want to retry after some time or notify the user.
        print("Rate limit exceeded. Please wait and try again later.")
'''

def takeCommand():
    '''it takes input from microphone and returns a string output using speech recognition module '''
    r=sr.Recognizer()    #Recognizer is a class
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1    #Its a parameter which can be adjusted,by right clicking on it we can see other parameters as well.
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')    #recognize_bing , recognize_google_cloud , etc
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)   

        print("Say that again please...")
        return "none"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

    # logic for executing tasks based on query
        if 'about yourself' in query:
            speak('My name is bharvishya. It comprises of two words that is Bharat and Bhavishya. Which means Indias future')
        elif 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")    #it replaces the word wikipedia with a blank and searches it in on wikipedia
            results = wikipedia.summary(query, sentences=2)    
            speak("according to wikipedia")
            #print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'search' in query:
            query = query.replace("search", "")           
            webbrowser.open(query)

        elif 'open chatGPT' in query:
            webbrowser.open("https:\\//chat.openai.com\/chat")    

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'show my linkedin' in query:
            webbrowser.open("https://www.linkedin.com/in/utkarsh-gupta-650605253/")

        elif 'open my github' in query:
            webbrowser.open("https://github.com/utkarsh0210")

        elif 'open webkiosk' in query:
            webbrowser.open("webkiosk.juet.ac.in")

        elif 'download video' in query:
            from pytube import YouTube
            link_video = input("Enter the link of video : ")
            yt_1 = YouTube(link_video)
            print(yt_1.title)
            #print(yt_1.thumbnail_url)

            vd = yt_1.streams.all() 
            vid = list(enumerate(vd))
            for i in vd:
                print(i)
            print()
            strm = int(input("Enter your choice : "))
            vd[strm].download()
            print(" Successfully downloaded ")

        elif 'scanner' in query:
            import qrcode as qr
            git_img = qr.make("https://github.com/utkarsh0210")
            git_img.save("Github.png")

            linkedin_img = qr.make("https://www.linkedin.com/in/utkarsh-gupta-650605253/")
            linkedin_img.save("LinkedIn.png")

        elif 'display movies' in query:
            speak("Enjoy your time sir!!")
            moviepath = "E:\MojMasti\movies"
            os.startfile(moviepath)

        elif 'play some music' in query:
            speak("Here you go with music")
            musicpath = "E:\MojMasti\music"
            songs=os.listdir(musicpath)    #listdir func lists down all the content in this directory
            os.startfile(os.path.join(musicpath,songs[random.randint(1,10)]))

        elif 'shuffle it' in query:
            musicpath = "E:\MojMasti\music"
            songs=os.listdir(musicpath)
            os.startfile(os.path.join(musicpath,songs[random.randint(1,10)]))

        elif "who are you" in query:
            speak("I am your virtual assistant created by Utkarsh")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif 'screen recording' in query:
            import cv2
            import pyautogui
            from win32api import GetSystemMetrics
            import numpy as np
            import time
            width = GetSystemMetrics(0)
            height = GetSystemMetrics(1)
            dim = (width,height)
            f= cv2.VideoWriter_fourcc(*"XVID")
            output = cv2.VideoWriter("test.mp4",f,30.0,dim)
            now_start_tine = time.time()
            dur=10
            end_time = now_start_tine + dur
            while True:
                image = pyautogui.screenshot()
                frame_1 = np.array(image)
                frame = cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)
                output.write(frame)
                c_time = time.time()
                if c_time > end_time :
                    break
            output.release()
            speak("Recording Ended")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\utkun\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    #double back slash for escape sequence
            os.startfile(codePath)

        #GUI functions/commands
        
        elif 'internet speed' in query :
            def speedcheck():
                s=speedtest.Speedtest()
                s.get_servers()
                down = str(round(s.download()/(10**6),3))+"Mbps"
                up = str(round(s.download()/(10**6),3))+"Mbps"
                lab_d.config(text=down)
                lab_u.config(text=up)

            sp=Tk()
            sp.title(" Internet Speed Test ")
            sp.geometry("500x400")
            sp.config(bg="black")

            lab = Label(sp,text="Internet Speed Test",font=("Time New Roman",30),bg="black",fg="white")
            lab.place(x=75,y=10)

            lab= Label(sp,text="Download Speed ",font=("Time New Roman",20),bg="black",fg="white")
            lab.place(x=90,y=80)

            lab_d = Label(sp,text="00",font=("Time New Roman",20),bg="black",fg="white")
            lab_d.place(x=90,y=120)

            lab = Label(sp,text="Upload Speed",font=("Time New Roman",20),bg="black",fg="white")
            lab.place(x=90,y=160)

            lab_u = Label(sp,text="00",font=("Time New Roman",20),bg="black",fg="white")
            lab_u.place(x=90,y=200)

            button = Button(sp,text = "CHECK",font=("Time New Roman",20),bg="red",relief=RAISED,command=speedcheck())
            button.place(x=175,y=280,height = 40)
            time.sleep(4)
            sp.mainloop()


        elif 'to do list' in query:
            root=Tk()
            root.title("To-Do App")
            root.geometry("400x650+400+100")
            root.resizable(False,False)
            task_list=[]

            def addTask():
                task = task_entry.get()
                task_entry.delete(0,END)
                if task:
                    with open("tasklist.txt",'a') as taskfile:
                        taskfile.write(f"\n{task}")
                    task_list.append(task)
                    listbox.insert(END,task)

            def deleteTask():
                global task_list
                task=str(listbox.get(ANCHOR))
                if task in task_list:
                    task_list.remove(task)
                    with open("taskfile.txt",'w') as taskfile:
                        for task in task_list:
                            taskfile.write(task+"\n")
                    listbox.delete(ANCHOR)

            def openTask():
                try:
                    global task_list
                    with open("tasklist.txt","r") as taskfile:
                        tasks=taskfile.readlines()
                    
                    for task in tasks:
                        if task!='\n':
                            task_list.append(task)
                            listbox.insert(END,task)
                except:
                    file=open('tasklist.txt','w')
                    file.close()

            #icon
            icon = PhotoImage(file="task.png")
            root.iconphoto(False,icon)

            #top bar
            topImage = PhotoImage(file="topbar.png")
            Label(root,image=topImage).pack()

            dockImage = PhotoImage(file="dock.png")
            Label(root,image=dockImage,bg="#32405b").place(x=30,y=25)

            noteImage = PhotoImage(file="task.png")
            Label(root,image=noteImage,bg="#32405b").place(x=30,y=25)

            heading = Label(root,text="TASKS",font=('algerian',32),fg="white",bg="#32405b")
            heading.place(x=130,y=20)

            #main
            frame = Frame(root,width=400,height=50,bg="white")
            frame.place(x=0,y=180)

            task = StringVar()
            task_entry = Entry(frame,width=20,bd=0)
            task_entry.place(x=10,y=7)
            task_entry.focus()

            button = Button(frame,text="ADD",font=('arial',12),width=5,bg="#5a95ff",fg="white",bd=0,command=addTask)
            button.place(x=350,y=12)

            #listbox
            frame1 = Frame(root,bd=3,width=700,height=280,bg="#32405b")
            frame1.pack(pady=(160,0))

            listbox = Listbox(frame1,width=60,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
            listbox.pack(side=LEFT,fill=BOTH,padx=2)
            scrollbar = Scrollbar(frame1)
            scrollbar.pack(side=RIGHT,fill=BOTH)

            listbox.config(yscrollcommand=scrollbar.set)
            scrollbar.config(command=listbox.yview)

            openTask()

            #delete
            Delete_icon = PhotoImage(file="delete.png")
            Button(root,image=Delete_icon,bd=0,cursor="hand2",command=deleteTask).pack(side=BOTTOM,pady=13)
            root.mainloop()

        elif 'camera' in query or 'photo' in query:
            ec.capture(0, "jarvis camera","img.jpg")

        elif 'open notes' in query:
            speak("what should i write sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            file.write(note)
        
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop Bharvishya")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif 'how are you' in query:
            speak("I am fine, Thank you for asking")
            speak("How are you, Sir")
 
        elif 'i am fine' in query:
            speak("It's good to know that you are fine")

        elif 'open snipping tool' in query:
            snip_tool = open("%windir%\\system32\\SnippingTool.exe")

        elif 'open whatsapp' in query:
            what_sapp = open("C:\\Users\\utkun\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
            what_sapp=csv.reader(what_sapp)
            
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "who made" in query or "who created" in query: 
            speak("I have been created by Utkarsh.")

        elif "morning" in query:
            speak("A warm good" +query+"to you too")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "why you came to world" in query:
            speak("Thanks to Utkarsh, further It's a secret")

        elif 'shutdown' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        '''
        elif 'search'.lower() in query.lower():
            ai(prompt=query)  
        else:
            chat(chatStr=query)
'''
