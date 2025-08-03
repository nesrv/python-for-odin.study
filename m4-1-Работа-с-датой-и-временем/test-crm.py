from datetime import datetime

log = '''
Егор Тимофеев, 09:10, 16:50
Марина Абрамова, 12:00, 15:59
Никита Круглов, 09:10, 12:45
Анна Семенова, 08:10, 12:30
Юлия Сафонова, 10:10, 10:50
Михаил Колесников, 11:10, 12:10
'''

for line in log.strip().split('\n'):
    name, start, end = line.split(', ')
    start_time = datetime.strptime(start, '%H:%M')
    end_time = datetime.strptime(end, '%H:%M')
    
    work_duration = end_time - start_time
    work_hours = work_duration.seconds / 3600
    
    if work_hours > 4:
        print(f"{name}: {work_hours:.1f} часов")