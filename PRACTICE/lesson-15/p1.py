import winsound
import time


winsound.PlaySound('SystemAsterisk', winsound.SND_ALIAS)
winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
winsound.PlaySound('SystemQuestion', winsound.SND_ALIAS)


melody = [
        (262, 400), (262, 400), (294, 800), (262, 800), (349, 800), (330, 1600),
        (262, 400), (262, 400), (294, 800), (262, 800), (392, 800), (349, 1600),
        (262, 400), (262, 400), (523, 800), (440, 800), (349, 800), (330, 800), (294, 800),
        (466, 400), (466, 400), (440, 800), (349, 800), (392, 800), (349, 1600)
    ]

    
for freq, dur in melody:
    winsound.Beep(freq, dur)
    time.sleep(0.02)
    
