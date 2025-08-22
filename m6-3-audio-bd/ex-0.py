import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)

import winsound
import time

def play_simple_happy_birthday():
    # Простая версия Happy Birthday
    melody = [
        (262, 400), (262, 400), (294, 800), (262, 800), (349, 800), (330, 1600),
        (262, 400), (262, 400), (294, 800), (262, 800), (392, 800), (349, 1600),
        (262, 400), (262, 400), (523, 800), (440, 800), (349, 800), (330, 800), (294, 800),
        (466, 400), (466, 400), (440, 800), (349, 800), (392, 800), (349, 1600)
    ]
    
    for freq, dur in melody:
        winsound.Beep(freq, dur)
        time.sleep(0.02)

play_simple_happy_birthday()