#import subprocess

from engine.feature import *

# Initialize Eel with the web folder
eel.init('../www')
playAssistantSound()
from threading import Thread
def func1():
    time.sleep(1)
    Wish()
    #subprocess.call(r"C:\Users\rahul\PycharmProjects\Mainproject\devices.bat")
def func2():
    eel.start('index.html', size=(2100, 1200))
if __name__ == '__main__':
    Thread(target=func1).start()
    Thread(target=func2).start()
