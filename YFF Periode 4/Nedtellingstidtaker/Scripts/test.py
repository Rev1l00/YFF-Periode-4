import time
from playsound import playsound as ps
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x500")
window.title("Countdown")

time_string = StringVar()
time_string.set("00")

time_Text_Box = Entry(window, width=3, textvariable=time_string)
time_Text_Box.place(x = 220, y = 180)

#cd_time = int(input("How long do you want to count down?: "))

def countdown(t):
    while t > -1:
        t -= 1
        t.set(t)
        window.update()
        time.sleep(1)
    print("Time is up!")
    ps("Nedtellingstidtaker\Sound_effects\FM9B3TC-alarm.mp3")

countdown(time_string)