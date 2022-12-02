import pygame
import random
import webbrowser
import datetime
import time
pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
pygame.display.set_caption("Write when you want the alarm to ring.")

font = pygame.font.SysFont(None, 100)
text = ""
input_active = True

run = True
while run:
    current_time = datetime.datetime.now().strftime("%H:%M")
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            input_active = True
            text = ""
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False
                pygame.display.set_caption(f"The alarm will ring at: {text}")
                alarm_time = text
                url = random.choice(list(open('Alarmklokke\Text Files\Ringtones.txt')))
                current_time = datetime.datetime.now().strftime("%H:%M")
                if current_time == alarm_time:
                    webbrowser.open(url, autoraise=True)
                break
            elif event.key == pygame.K_BACKSPACE:
                text =  text[:-1]
            else:
                text += event.unicode

        window.fill(1)
        text_surf = font.render("Alarm: " + text, True, (255, 255, 255))
        current_time_text = font.render("Clock: " + current_time, True, (255, 255, 255))
        window.blit(text_surf, text_surf.get_rect(center = window.get_rect().center))
        window.blit(current_time_text, current_time_text.get_rect(top = window.get_rect().top))
        pygame.display.flip()
time.sleep(10)
pygame.quit()
exit()