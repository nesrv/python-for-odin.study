import winsound
import time

# Ноты и их частоты (в Гц)
notes = {
    'C3': 130, 'C#3': 138, 'D3': 146, 'D#3': 155, 'E3': 164, 'F3': 174, 'F#3': 185,
    'G3': 196, 'G#3': 207, 'A3': 220, 'A#3': 233, 'B3': 246,
    'C4': 261, 'C#4': 277, 'D4': 293, 'D#4': 311, 'E4': 329, 'F4': 349, 'F#4': 369,
    'G4': 392, 'G#4': 415, 'A4': 440, 'A#4': 466, 'B4': 493,
    'C5': 523, 'C#5': 554, 'D5': 587, 'D#5': 622, 'E5': 659, 'F5': 698, 'F#5': 739,
    'G5': 784, 'G#5': 830, 'A5': 880, 'A#5': 932, 'B5': 987
}

# Похоронный марш Шопена (упрощенная версия)
funeral_march = [
    (notes['B3'], 800), (notes['B3'], 800), (notes['B3'], 800), (notes['B3'], 800),
    (notes['C4'], 800), (notes['D4'], 800), (notes['C4'], 800), (notes['B3'], 800),
    (notes['A3'], 800), (notes['A3'], 800), (notes['A3'], 800), (notes['A3'], 800),
    (notes['B3'], 800), (notes['C4'], 800), (notes['B3'], 800), (notes['A3'], 800),
    
    (notes['G3'], 800), (notes['G3'], 800), (notes['G3'], 800), (notes['G3'], 800),
    (notes['A3'], 800), (notes['B3'], 800), (notes['A3'], 800), (notes['G3'], 800),
    (notes['F3'], 800), (notes['F3'], 800), (notes['F3'], 800), (notes['F3'], 800),
    (notes['G3'], 800), (notes['A3'], 800), (notes['G3'], 800), (notes['F3'], 800),
    
    (notes['E3'], 800), (notes['E3'], 800), (notes['E3'], 800), (notes['E3'], 800),
    (notes['F3'], 800), (notes['G3'], 800), (notes['F3'], 800), (notes['E3'], 800),
    (notes['D3'], 800), (notes['D3'], 800), (notes['D3'], 800), (notes['D3'], 800),
    (notes['E3'], 800), (notes['F3'], 800), (notes['E3'], 800), (notes['D3'], 800),
]

def play_funeral_march():
    print("Играем Похоронный марш Шопена...")
    
    for frequency, duration in funeral_march:
        winsound.Beep(frequency, duration)
        time.sleep(0.05)
    
    print("Мелодия завершена.")

# Альтернативная версия - более медленная и торжественная
def play_funeral_march_slow():
    print("Играем медленную версию Похоронного марша...")
    
    slow_march = [
        (notes['B3'], 1200), (notes['B3'], 1200), 
        (notes['B3'], 1200), (notes['B3'], 1200),
        (notes['C4'], 1200), (notes['D4'], 1200), 
        (notes['C4'], 1200), (notes['B3'], 1200),
        
        (notes['A3'], 1200), (notes['A3'], 1200), 
        (notes['A3'], 1200), (notes['A3'], 1200),
        (notes['B3'], 1200), (notes['C4'], 1200), 
        (notes['B3'], 1200), (notes['A3'], 1200),
        
        (0, 600),  # пауза
    ]
    
    for frequency, duration in slow_march:
        if frequency > 0:
            winsound.Beep(frequency, duration)
        else:
            time.sleep(duration / 1000)
        time.sleep(0.1)
    
    print("Мелодия завершена.")

# Простая версия для быстрого запуска
def play_simple_funeral_march():
    """Упрощенная версия похоронного марша"""
    simple_melody = [
        (246, 800), (246, 800), (246, 800), (246, 800),  # B3
        (261, 800), (293, 800), (261, 800), (246, 800),  # C4, D4, C4, B3
        (220, 800), (220, 800), (220, 800), (220, 800),  # A3
        (246, 800), (261, 800), (246, 800), (220, 800),  # B3, C4, B3, A3
        (196, 800), (196, 800), (196, 800), (196, 800),  # G3
        (220, 800), (246, 800), (220, 800), (196, 800),  # A3, B3, A3, G3
    ]
    
    print("Играем упрощенный похоронный марш...")
    for freq, dur in simple_melody:
        winsound.Beep(freq, dur)
        time.sleep(0.03)
    
    print("Мелодия завершена.")

# Запуск мелодии
if __name__ == "__main__":
    print("=" * 50)
    play_simple_funeral_march()
    
    print("=" * 50)
    time.sleep(2)
    play_funeral_march()
    
    print("=" * 50)
    time.sleep(2)
    play_funeral_march_slow()