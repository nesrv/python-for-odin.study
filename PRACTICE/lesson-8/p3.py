# cities = 'Анапа Анадырь Москва Абакан Альметьевск Омск'
# cities = cities.split()

# for city in cities:
#     if city[0] == 'А':
#         print(city)

# cities = filter(lambda x: x[0] == 'А', cities)

# cities = list(filter(lambda city: city.startswith('А'), cities))

# print(cities)

# # endswith

# file_names = 'main.py run.py main.bat app.py fastapi.py command.com'.split()
# file_names = list(filter(lambda x: x.endswith(".py"), file_names))
# print (file_names)

# # Проверка отсутствия русских букв
# string = '1 a1 фb2 Петя ab Маша100 abc100 10'.split()

# # res = map(lambda x: x.isalpha(), string)

# # res = filter(str.isascii, string)
# # res = filter (lambda x: not x.isascii(), string)
# # print(*res)


quad = '5 10 25 30 49 81 100'

# Проверяем, является ли число полным квадратом


def is_quad(x):
    return int(x**0.5)**2 == x

# Фильтруем полные квадраты


quad = list(map(int, quad.split()))
perfect_squares = filter(is_quad, quad)
# print("Полные квадраты:", *perfect_squares)  # ['25', '49', '81', '100']


# reduce 

lst = [1,2,3,4,5]

from functools import reduce

# res = reduce(lambda s, x: s * x, lst)

# print(res)

rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
    
]

# square_rooms = map(lambda room: room["length"] * room["width"], rooms)
# # print(sum(square_rooms))

# total_square = reduce(lambda s, x: s + x, square_rooms)

# def square(square  , room):
#     return room["length"] * room["width"]


# total_square = reduce(lambda square  , room: square + room["length"] * room["width"], rooms, 0)
# print (total_square)



# сделать задачу в одну строчку !


# Отфильтровать (исключить) все предметы с весом менее 500

items_data = [
    "зонт=1000",
    "палатка=10000", 
    "спички=22",
    "котелок=543"
]
# print(result)  # зонт палатка котелок

items_data = map(lambda x: x.split("="), items_data)
items_data = dict(filter(lambda x: int(x[1]) >= 500, items_data))

print(*items_data)