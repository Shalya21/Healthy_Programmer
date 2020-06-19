from datetime import datetime
from time import time

from pygame import mixer


# function to play mp3 file

def music(mp3_file_name, stopper):
    mixer.init()
    mixer.music.load(mp3_file_name)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


# function to make a log file

def log_file(message):
    with open("Healthy_log.txt", "a") as f:
        f.write(f"{message} {datetime.now()} \n")


if __name__ == '__main__':
    print(
        "WELCOME TO OFFICE.\nPLEASE TAKE CARE OF YOUR HEALTH AND DO REMEMBER TO TAKE SMALL BREAKS.\n HAVE A NICE DAY.")
    water = time()  # initialized the water time
    eye = time()  # initialized the eye exercise time
    exercise = time()  # initialized the physicsal exercise time
    water_time = 10  # water reminder
    eye_time = 20  # eye exercise reminder
    exercise_time = 30  # physical exercise reminder
    while True:
        if time() - water > water_time:
            print("It's time to drink water ...")
            print("Please type 'drank' if you have drunk the water")
            music("water.mp3", "drank")
            water = time()  # initializing the time again
            log_file("Drank water at")

        if time() - eye > eye_time:
            print("It's time to do some exercise...")
            print("Please type 'done' if you have done the eye exercise")
            music("water.mp3", "done")
            eye = time()
            log_file("Eye exercise at")

        if time() - exercise > exercise_time:
            print("It's time for physical exercise...")
            print("Please type 'done' if you have done the physical exercise")
            music("water.mp3", "done")

            exercise = time()
            log_file("Physical Exercise at")
