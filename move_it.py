import time
import os

all_animation = [" Move it", "    Move it", "     Move it", "           Move it", "             Move it", "                 Move it", "                     Move it", "                         Move it", "                         Move it", ]
counter = 0
total_animation = len(all_animation)
# print(all_animation)
print(total_animation)
def Make_It_Move():
    global counter
    while counter < total_animation:
        print(all_animation[counter])
        time.sleep(.2)
        os.system('cls||clear')
        counter = counter + 1
    counter = 0
    Make_It_Move()
# webbrowser.open

Make_It_Move()