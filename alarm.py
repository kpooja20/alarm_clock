from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarms (seconds):
    time_elapsed = 0

    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left//60 
        seconds_left = time_left%60
        print(f"{CLEAR_AND_RETURN}alarm will sound in:{minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm-clock-short-6402.mp3")    

minutes = int(input("how many minutes to wait"))
seconds = int(input("how many seconds to wait"))
total_seconds = minutes*60 +seconds

alarms(total_seconds)