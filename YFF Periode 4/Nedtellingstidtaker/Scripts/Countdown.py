# Lag en nedtellingstidtaker i Python. Når nedtellingstidtakeren er ferdig så skal den vise en beskjed, og i tillegg skal den spille av en lyd som forteller at nedtellingen er over.

import time
from playsound import playsound as ps

# Setter variabelen "cd_time" til inputen av hvor lenge nedtellingen skal vare
cd_time = int(input("How long do you want to count down?: "))

# Teller ned til fra hvor mye inputen var og spiller en alarm lyd effekt
def countdown(t):
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
    print("Time is up!")
    ps("Nedtellingstidtaker\Sound_effects\FM9B3TC-alarm.mp3")
countdown(cd_time)