import sounddevice as sd
from scipy.io.wavfile import write, read
import numpy as np

sample_rate = 44100  # Частота дискретизации (Гц)
duration = 5         # Длительность записи (секунды)

print("Запись началась... Говорите!")


recording = sd.rec(
    int(duration * sample_rate),  # Общее количество сэмплов
    samplerate=sample_rate,
    channels=1,                   # 1 канал (моно), 2 - стерео
    dtype=np.int16                # Тип данных для сэмплов
)

sd.wait()
print("Запись завершена!")

filename = "my_recording.wav"
write(filename, sample_rate, recording)

print(f"Файл сохранен как {filename}")


sample_rate, audio_data = read("my_recording.wav")

sd.play(audio_data, sample_rate)
# Ждем окончания воспроизведения
sd.wait()

import matplotlib.pyplot as plt
# Создаем массив временных отметок
time = np.arange(0, len(audio_data)) / sample_rate

plt.figure(figsize=(10, 4))
plt.plot(time, audio_data, linewidth=0.5)
plt.title("Визуализация аудиозаписи")
plt.xlabel("Время (секунды)")
plt.ylabel("Амплитуда")
plt.grid(True)
# Сохраняем картинку
plt.savefig('audio_waveform.png')
plt.show()
