import schedule
from pynput.mouse import Controller, Button
import keyboard
from time import sleep


def join(subject):
    subject = str(subject)
    print("joined", subject)
    webbrowser.open(subject)
    sleep(10)
    mouse.position = (430, 272)
    mouse.press(button.left)
    mouse.release(button.left)
    sleep(0.1)
    keyboard.press('ctrl')
    sleep(0.1)
    keyboard.press('shift')
    sleep(0.1)
    keyboard.press('tab')
    sleep(0.1)
    keyboard.release('tab')
    sleep(0.1)
    keyboard.release('shift')
    sleep(0.1)
    keyboard.release('ctrl')
    sleep(0.1)
    keyboard.press_and_release('ctrl + w')
    sleep(0.1)


info = open("everyday joiner.txt", 'r+', encoding='ascii')
info = info.readlines()
infostr = ''
for i in range(len(info)):
    infostr += info[i]
infostr = infostr.replace(' ', '')
info = infostr
info = info.split('\n')
schedule.every().day.at(info[0]).do(join, info[1])


while True:
    schedule.run_pending()
