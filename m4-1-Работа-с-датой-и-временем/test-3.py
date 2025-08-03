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
    start_h, start_m = map(int, start.split(':'))
    end_h, end_m = map(int, end.split(':'))
    
    start_minutes = start_h * 60 + start_m
    end_minutes = end_h * 60 + end_m
    work_hours = (end_minutes - start_minutes) / 60
    
    if work_hours > 4:
        print(f"{name}: {work_hours:.1f} часов")