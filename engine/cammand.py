import datetime
import os
import random
import subprocess
import webbrowser
import eel
import pyautogui
import pyjokes
# ***************************
import pyttsx3
import pywikihow
import requests
# **********
import speech_recognition as sr
import wikipedia
from bs4 import BeautifulSoup
from requests import get
# ****************
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 174)
    eel.DisplayMessage(text)
    engine.say(text)
    print(text)
    eel.receiverText(text)
    engine.runAndWait()
def takecommand():
 while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        eel.DisplayMessage("listening....")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshould = 1
        audio = r.listen(source, timeout=31, phrase_time_limit=20)
    try:
        print("Recongnizing...")
        eel.DisplayMessage("Recongnizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")
        eel.DisplayMessage(query)

    except Exception as e:
        #speak("say that again plz...")
        return "none"
    return query
def close():
    pyautogui.press('esc')
    time.sleep(5)
    return True
def computational_intelligence(question):
    try:
        app_id='L7TVHJ-VA28A49KAQ'
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None
@eel.expose
def allCommands(message=1):
    if message==1:
        query = takecommand().lower()
        print(query)
        eel.senderText(query)
    else:
        query=message
        eel.senderText(query)
    try:
        if "on youtube" in query:
            speak(f"okay ,opening youtube...")
            from engine.feature import PlayYoutube
            PlayYoutube(query)
        elif "tell me news" in query:
            speak("place wait same time ,fetching the latest news")
            def news():
                try:
                    min_url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=fd6eca5e6b9c401ea744b1ee00ee447c"  # this is api key
                    main_page = requests.get(min_url).json()
                    articales = main_page["articles"]
                    head = []
                    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth",
                           "tenth"]
                    for ar in articales:
                        head.append(ar["title"])
                    for i in range(len(day)):
                        speak(f"today's {day[i]} news is:{head[i]}")
                except Exception as e:
                    speak("Api is Expire ")
            news()
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.feature import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    speak(f"okay ,sending message...")
                    flag = 'message'
                    speak("what message to send")
                    query = takecommand()
                    
                elif "phone call" in query:
                    speak(f"okay ,calling...")
                    flag = 'call'
                else:
                    flag = 'video call'
                    speak(f"okay ,video calling...")
                    
                whatsApp(ctontac_no, query, flag, name)
        elif "open notepad" in query or "start notepad" in query or "notepad open " in query or "run notepad" in query:
            speak(f"okay ,opening notepad...")
            subprocess.Popen(['notepad.exe'])
            # close notepad
        elif "close notepad" in query or "stop notepad" in query or "notepad close" in query or "notepad stop" in query:
            speak("okay ,closing notepad")
            os.system("TASKKILL /f /im notepad.exe")

        elif "hello" in query or "hey" in query or "hi" in query:
            speak("hello sir, may i help you with something.")

        elif "how are you" in query:
            speak("i am fine sir, what about you.")

        elif "also good" in query or "fine" in query:
            speak("that's great to hear from you.")

        elif "thank you" in query or "thanks" in query:
            speak("it's my pleasure .")

        elif "you can sleep" in query or "sleep now" in query:
            speak("okay , i an going to sleep you can call me anytime.")

        elif "open cammand prompt" in query or "open cmd" in query or "start cmd" in query or "run cmd" in query or "open the cmd" in query:
            speak(f"okay ,opening cammand promt...")
            os.system("start cmd")

        elif "open camera" in query or "start camera" in query:
            speak(f"okay ,opening camera...")
            # cap = cv2.VideoCapture(0)
            # while True:
            #     ret, img = cap.read()
            #     cv2.imshow('webcam', img)
            #     k = cv2.waitKey(50)
            #     if k == 27:
            #         break
            # cap.release()
            # cv2.destroyWindow()
            subprocess.run(["start", "microsoft.windows.camera:"], shell=True)
        elif "close camera" in query or "stop camera" in query:
            speak(f"okay ,closing camera...")
            os.system("taskkill /f /im WindowsCamera.exe")
        elif "open calculator" in query or "start calculator" in query or "run calculator" in query:
            speak(f"okay ,opening calculator...")
            subprocess.Popen(["calc"])
        elif "close calculator" in query or "stop calculator" in query:
            speak(f"okay ,closing calculator...")
            subprocess.run(["taskkill", "/f", "/im", "Calculator.exe"], shell=True)
        elif "open calender" in query or "start calender" in query:
            speak(f"okay ,opening calender...")
            subprocess.run("start outlookcal:", shell=True)
        elif "close calender" in query or "stop calender" in query:
            speak(f"okay ,closing calender...")
            try:
                subprocess.run(["taskkill", "/f", "/im", "HxCalendarAppImm.exe"], shell=True)
                # speak("Calendar closed successfully.")
            except Exception as e:
                speak(f"Failed to close Calendar: {e}")
        elif "open vs code" in query or "start vs code" in query or "open visual studio" in query:
            speak(f"okay ,opening vs code...")
            V_path = "C:\\Users\\rahul\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(V_path)
        elif "open excel" in query or "start excel" in query:
            speak(f"okay ,opening excel...")
            try:
                subprocess.Popen(['excel.exe'])
            except Exception as e:
                print(f"Failed to open Excel: {e}")

        elif "close excel" in query or "stop excel" in query:
            speak(f"okay ,closing excel...")
            try:
                subprocess.run(["taskkill", "/f", "/im", "EXCEL.EXE"], shell=True)
                # print("Excel closed successfully.")
            except Exception as e:
                print(f"Failed to close Excel: {e}")
        elif "close excel" in query:
            speak(f"okay ,closing excel...")
            try:
                os.startfile('excel')
                # print("Excel opened successfully.")
            except Exception as e:
                print(f"Failed to open Excel: {e}")
        elif "open word" in query:
            speak(f"okay ,opening word...")
            try:
                os.startfile('winword')
                # print("Microsoft Word opened successfully.")
            except Exception as e:
                print(f"Failed to open Microsoft Word: {e}")

        elif "close word" in query:
            speak(f"okay ,closing word...")
            try:
                subprocess.run(["taskkill", "/f", "/im", "WINWORD.EXE"], shell=True)
                # print("Microsoft Word closed successfully.")
            except Exception as e:
                print(f"Failed to close Microsoft Word: {e}")
        elif "close power point" in query:
            speak(f"okay ,closing power point...")
            try:
                subprocess.run(["taskkill", "/f", "/im", "POWERPNT.EXE"], shell=True)
                # print("Microsoft PowerPoint closed successfully.")
            except Exception as e:
                print(f"Failed to close Microsoft PowerPoint: {e}")
        elif "open power point" in query:
            speak(f"okay ,opening power point...")
            try:
                os.startfile('powerpnt')
            # print("Microsoft PowerPoint opened successfully.")
            except Exception as e:
                print(f"Failed to open Microsoft PowerPoint: {e}")
        elif "open wordpad" in query:
            speak(f"okay ,opening wordpad...")
            try:
                os.startfile('wordpad')
                # print("WordPad opened successfully.")
            except Exception as e:
                print(f"Failed to open WordPad: {e}")
        elif "close wordpad" in query:
            speak(f"okay ,opening wordpad...")
            try:
                subprocess.run(["taskkill", "/f", "/im", "wordpad.exe"], shell=True)
            # print("WordPad closed successfully.")
            except Exception as e:
                print(f"Failed to close WordPad: {e}")
        elif "open paint" in query:
            speak(f"okay ,opening paint...")
            try:
                os.startfile('mspaint')
            # print("Microsoft Paint opened successfully.")
            except Exception as e:
                print(f"Failed to open Microsoft Paint: {e}")
        elif "close paint" in query:
            speak(f"okay ,closing paint...")
            try:
                subprocess.run(["taskkill", "/f", "/im", "mspaint.exe"], shell=True)
            # print("Microsoft Paint closed successfully.")
            except Exception as e:
                print(f"Failed to close Microsoft Paint: {e}")
        elif "open gallery" in query or "open photos" in query:
            speak(f"okay ,opening gallery...")
            try:
                subprocess.Popen(["start", "ms-photos:"], shell=True)
            # print("Photo app opened successfully.")
            except Exception as e:
                print(f"Failed to open photo app: {e}")
        elif "close gallery" in query or "close photos" in query:
            speak(f"okay ,closing gallery...")
            try:
                subprocess.run(["taskkill", "/f", "/im", "Microsoft.Photos.exe"], shell=True)
                # print("Photo app closed successfully.")
            except Exception as e:
                print(f"Failed to close photo app: {e}")
        elif "close all apps" in query:
            speak(f"okay ,closing ...")
            import psutil
            for proc in psutil.process_iter():
                try:
                    proc.terminate()  # Terminate the process
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

        elif "start Python editor" in query:
            speak(f"okay ,start python ...")
            p_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.3.2\\bin\\pycharm64.exe"
            os.startfile(p_path)

        elif "play music" in query:
            speak(f"okay ,playing music...")
            music_dir = "C:\\Users\\rahul\\Music"
            Songs = os.listdir(music_dir)
            rd = random.choice(Songs)
            # for Song in random.choice(Songs):
            # if Song.endswith(".mp3"):
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            speak(f"okay ,finding ip...")
            ip = get('https://api.ipify.org').text
            speak(f"your ip adreess is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak(results)
            # print(results)
        elif "open youtube.com" in query:
            speak(f"okay ,opening youtube...")
            webbrowser.open("https://www.youtube.com/")

        elif "open facebook" in query:
            speak(f"okay ,opening facebook...")
            webbrowser.open("https://facebook.com/")

        elif "open java t point" in query:
            speak(f"okay ,opening java t point...")
            webbrowser.open("https://www.javatpoint.com/")

        elif "open w3school.com" in query or "open w3school" in query:
            speak(f"okay ,opening w3school.com...")
            webbrowser.open("https://www.w3schools.com/")

        elif "open stackoverflow.com" in query or "open stackoverflow" in query:
            speak(f"okay ,opening stackoverflow.com...")
            webbrowser.open("https://stackoverflow.com/")

        elif "open chatgpt" in query:
            speak(f"okay ,opening chatgpt...")
            webbrowser.open("https://chat.openai.com/")
        elif"open google" in query:
            speak(f"okay ,opening google...")
            webbrowser.open("https://www.google.com/")
        elif "open map" in query or "start map"in query:
            speak("okay,opening map")
            webbrowser.open("https://maps.google.com/")

        elif "hello google" in query:
            speak("sir ,what should be search on google")
            cm = takecommand()
            webbrowser.open(f"{cm}")

        elif "send message using Whatsapp" in query:
            import pywhatkit as kit
            message = "Hello, this is a test message."
            cm1 = takecommand().lower()
            min = 1
            hour = int(datetime.datetime.now().hour)
            min += int(datetime.datetime.now().minute)
            kit.sendwhatmsg("+919356601350", message, hour, min, 15, True, 2)
        elif "play song on youtube" in query:
            import pywhatkit as kit
            speak("tell me song name or video name")
            song = takecommand().lower()
            kit.playonyt(song)
        elif "send mail" in query:
            try:
                speak("what should you say?")
                content = takecommand().lower()
                to = "example@gmail.com"
                # call above function line no 46
                feature.sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry ,i am not able to send this mail")
        elif "close vs code" in query:
            speak("okay ,closing vs code")
            os.system("TASKKILL /f /im Code.exe")

        elif "close python editor" in query:
            speak("okay ,closing editor")
            os.system("TASKKILL /f /im pycharm64.exe")

        elif "close cmd" in query:
            speak("okay ,closing cmd")
            os.system("TASKKILL /f /im cmd.exe")

        elif "set alarm" in query:
            speak("please tell me the time to set alarm...,for example ,set alarm to 6 :30 a.m")
            nn = takecommand().lower()
            nn = nn.replace("set alarm to", "")
            nn = nn.replace(".", "")
            nn = nn.upper()
            from engine import MyAlarm
            MyAlarm.alarm(nn)
            # if nn==22:
            #     music_dir='E:\\music'
            #     Songs=os.listdir(music_dir)
            #     os.startfile(os.path.join(music_dir,Songs[0]))
        elif "tell me a joke" in query:
            # which language you have joke
            # speak("tell me a language")
            # cm2= takecommand().upper()
            joke = pyjokes.get_joke()
            speak(joke)
        elif "switch the window" in query:
            import time
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
            # close voice assistant
        elif "take a screenshot" in query or "take screenshot" in query:
            speak("tell me name for this screenshot..")
            name = takecommand().lower()
            speak("please hold the screen for few seconds, i am taking screenshot")
            import time
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            # Display the screenshot
            img.show()

        elif "turn on bluetooth" in query:
            import time
            # Press Windows key to open Start menu
            pyautogui.press('win')
            time.sleep(1)  # Wait for Start menu to open
            # Type "Bluetooth" to search for it
            pyautogui.typewrite('Bluetooth')
            time.sleep(1)  # Wait for search results to appear
            # Press Enter to open Bluetooth settings
            pyautogui.press('enter')
            time.sleep(2)  # Wait for Bluetooth settings to open
            toggle_switch_position = (1720, 179)
            pyautogui.click(toggle_switch_position)

        elif "turn off bluetooth" in query:
            import time
            # Press Windows key to open Start menu
            pyautogui.press('win')
            time.sleep(1)  # Wait for Start menu to open
            # Type "Bluetooth" to search for it
            pyautogui.typewrite('Bluetooth')
            time.sleep(1)  # Wait for search results to appear
            # Press Enter to open Bluetooth settings
            pyautogui.press('enter')
            time.sleep(2)  # Wait for Bluetooth settings to open
            toggle_switch_position = (1720, 179)
            pyautogui.click(toggle_switch_position)

        elif "turn on wifi" in query:
            import time
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.typewrite('WIFI')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(2)
            toggle_switch_position = (1720, 179)
            pyautogui.click(toggle_switch_position)

        elif "turn off wifi" in query or "off wifi" in query or "wifi off" in query:
            import time
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.typewrite('WIFI')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(2)
            toggle_switch_position = (1720, 179)
            pyautogui.click(toggle_switch_position)
        elif "open mail" in query:
            try:
                subprocess.Popen(["start", "mailto:"], shell=True)
            # print("Mail app opened successfully.")
            except Exception as e:
                print(f"Failed to open mail app: {e}")
        elif "close app" in query:

            try:
                # Press Alt+F4 keyboard shortcut to close the active window.
                pyautogui.hotkey('alt', 'f4')
            # print("app closed successfully.")
            except Exception as e:
                print(f"Failed to close mail app: {e}")

            # Wait for 2 seconds before attempting to close the mail app.

        elif "shut down the system" in query:
            try:
                os.system("shutdown /s /t 0")
            except Exception as e:
                print("An error occurred:", e)
        elif "restart the system " in query:
            try:
                # Restart the system immediately
                os.system("shutdown /r /t 0")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif "sleep the system" in query:
            # sleep the system immediately
            pyautogui.KEYBOARD_KEYS('win')
            pyautogui.press("L")
            # elif"read pdf" in query:
            # pdf_reader()
        elif "tell me temperature" in query:
            speak("tell me city name...")
            search = takecommand().lower()
            search1 = f"weather in {search}"
            url = f"https://www.google.com/search?q={search1}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f'current {search} is{temp}')
            print(temp)
        elif "meeting" in query:
            speak("Ok sir opening meeet")
            webbrowser.open("https://meeting/")

        elif "activate how to do mode" in query:
            speak("How to do mode is activated")
            while True:
                speak("please tell me what you want to know")
                how = takecommand().lower()
                try:
                    if "exit" in how or "close" in how:
                        speak("okay sir, how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = pywikihow.search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am not able to find this")
        elif "how much battery of system" in query or "please tell me battery details " in query:
            import psutil
            battary = psutil.sensors_battery()
            per = battary.percent
            speak(f"our system have {per} percent battery")
            if per >= 80:
                speak("we have power to continue our work")
            elif per >= 40 and per <= 80:
                speak("connect to charging ")
            elif per >= 10 and per <= 40:
                speak("please connect to charging")
            else:
                speak("we have very low power, please connect to charging thee system will shutdown very soon")
        elif "tell me internet speed" in query:
            import speedtest
            speak("please wait few second...")
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"we have {dl} bit per second downloading speed and {up} bit per second uploading speed.")
        elif "volume up" in query:
            pyautogui.press("volumeup", 7)
        elif "volume down" in query:
            pyautogui.press("volumedown", 7)
        elif "volume mute" in query:
            pyautogui.press("volumemute")
        elif "what is" in quary or "who is" in quary:
            question = quary
            answer = computational_intelligence(question)
            speak(answer)
        elif "open mobile camera" in query:
            speak("please install ip webcam in your phone and start")
            import urllib.request
            import cv2
            import numpy as np
            import time
            URL = "http://192.0.0.4:8080/shot.jpg"
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                img = cv2.imdecode(img_arr, -1)
                cv2.imshow('IPWEBcam', img)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    break
            cv2.destroyWindow()

    except:
        print("error")
    eel.ShowHood()

