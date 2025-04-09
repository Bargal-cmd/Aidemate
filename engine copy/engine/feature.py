import datetime
import pipes
import sqlite3
import subprocess
import time
import eel
import pyautogui
from playsound import playsound
from cammand import speak
from engine.helper import *

#****************
conn = sqlite3.connect("../aidemate.db")
cursor = conn.cursor()

@eel.expose
def playAssistantSound():
    music_dir = "../www/assets/audio/start_sound.mp3"
    playsound(music_dir)
def PlayYoutube(query):
    import pywhatkit as kit
    search_term =extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def findContact(query):
    
    words_to_remove = ["aidemate", 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
    query = remove_words(query, words_to_remove)
    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?",
                       ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak('not exist in contacts')
        return 0, 0
def whatsApp(mobile_no, message, flag, name):
    if flag == 'message':
        target_tab = 14
        message1 = "message send successfully to "+name
    elif flag == 'call':
        target_tab = 9
        message = ''
        message1 = "calling to "+name

    else:
        target_tab = 8
        message = ''
        message1 = "staring video call with "+name


    # Encode the message for URL
    encoded_message = pipes.quote(message)
    print(encoded_message)
    # Construct the URL
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # Construct the full command
    full_command = f'start "" "{whatsapp_url}"'

    # Open WhatsApp with the constructed URL using cmd.exe
    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)
    
    pyautogui.hotkey('ctrl', 'f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')

    pyautogui.hotkey('enter')
    speak(message1)
#**************************************
def Wish():
    hour = int(datetime.datetime.now().hour)
    # print(hour)
    if hour >= 0 and hour <= 12:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Good morning...its {current_time}")
    elif hour > 12 and hour < 18:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"good afternoon...its{current_time}")
    else:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"good evening...its{current_time}")
    speak("i am ady sir ,plz tell me how can i help you")


def shared():
    return None