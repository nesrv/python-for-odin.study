
import time

start = time.perf_counter()
# [x ** 2 for x in range(10**7)] # генерация списка
# {x ** 2  for x in range(10**7)} # генерация множества
# {x : x ** 2  for x in range(10**7)} # генерация ?

( x ** 2  for x in range(10**7)) # генератор
end = time.perf_counter()

print(f"Время выполнения: {end - start:.4f} секунд") 
# 1.23 []
# 5.06 set
# 1.98 dict
# 0.000 ?
# i5-6600


log = '''
Егор Тимофеев, 09:10, 16:50
Марина Абрамова, 12:00, 15:59
Никита Круглов, 09:10, 12:45
Анна Семенова, 08:10, 12:30
Юлия Сафонова, 10:10, 10:50
Михаил Колесников, 11:10, 12:10
'''

from datetime import datetime

log = log.strip().splitlines()
# print(log, sep='\n')
# кто провел на работе больше 4 часов

for row in log:
    name, st, end = row.split(', ')   
    st = datetime.strptime(st,'%H:%M' )
    end = datetime.strptime(end,'%H:%M' )
    hours = (end - st).seconds / 3600
    if hours > 4:
        print(f"{name}: {hours:.1f} часов")
        
    # start_min =  st_h * 60 + st_m
    # end_min = end_h * 60 + end_m
    # if (delta := end_min - start_min) > 240:
    #     print (name, delta)
    