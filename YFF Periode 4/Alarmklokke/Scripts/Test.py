# Lag en alarmklokke i Python. Du skal også lage en tekstfil der du legger inn flere lenker til YouTube-filmer. 
# Når alarmen går av så skal koden velge en tilfeldig video fra tekstfilen og spille den av. 

import time
from datetime import date
import datetime
import random
import webbrowser

# Setter variabelen "url" til en tilfeldig link fra listen
url = random.choice(list(open('Alarmklokke\Text Files\Ringtones.txt')))

# Tar Input til når alarmen skal spilles av
alarm01_Time = input("What time do you want the alarm to ring? Enter in Hour:Minute: ")
print(f"The alarm will ring at {alarm01_Time}")

# Spiller en tilfeldig alarm fra listen når alarmen går ut
def alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("The time is up!")
            webbrowser.open(url)
            break
alarm(alarm01_Time)