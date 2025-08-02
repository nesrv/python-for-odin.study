import time


start = time.perf_counter()  # Наиболее точный таймер
# Код, время выполнения которого нужно измерить
{x ** 2 for x in range(10**7)}
end = time.perf_counter()
print(f"Время выполнения: {end - start:.4f} секунд")

start = time.perf_counter()  # Наиболее точный таймер
# Код, время выполнения которого нужно измерить
(x ** 2 for x in range(10**7))
end = time.perf_counter()
print(f"Время выполнения: {end - start:.4f} секунд")


start = time.perf_counter()  # Наиболее точный таймер
# Код, время выполнения которого нужно измерить
[x ** 2 for x in range(10**7)]
end = time.perf_counter()
print(f"Время выполнения: {end - start:.4f} секунд")

start = time.perf_counter()  # Наиболее точный таймер
# Код, время выполнения которого нужно измерить
{x ** 2 : x for x in range(10**7)}
end = time.perf_counter()
print(f"Время выполнения: {end - start:.4f} секунд")