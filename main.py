import time, subprocess, os
from pynput.keyboard import Key, Controller

keyboard = Controller()

subprocess.call(['C:\Riot Games\League of Legends\LeagueClient.exe'])
time.sleep(5)
#Please enter your own league of legends password as a string.
keyboard.type(LEAGUEPASSWORD)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(20)
os.system("start mousecontroller.exe")