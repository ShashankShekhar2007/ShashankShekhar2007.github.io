from pygame import mixer
from time import time
from datetime import datetime
water_seconds = int(input('You want to drink water at every (in minutes): '))
eyes_seconds = int(input('You want to do exercise of your eyes at every (in minutes): '))
exercise_seconds = int(input('You want to do exercise at every (in minutes): '))
def player(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(loops=15)
    while True:
        x = input("Please Enter 'stop' to stop the reminder: ")
        if x.lower() == stopper:
            mixer.music.stop()
            break
def log( msg):
    with open('Physical_Details', "a") as o:
        o.write(f'You {msg} at: {datetime.now()}' + '\n')
if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    while True:
        if time() - init_water > water_seconds*60:
            player('water.mp3', 'stop')
            log('drank water')
            init_water = time()
        if time() - init_eyes > eyes_seconds*60:
            player('eyes.mp3', 'stop')
            log('did exercise of eyes')
            init_eyes = time()
        if time() - init_exercise > exercise_seconds*60:
            player('exercise.mp3', 'stop')
            log('did exercise')
            init_exercise = time()