
def is_string(lst):
    return all(isinstance(x, str) for x in lst)


cities = 'Москва Питер Орел Сочи'  # все города с большой буквы
cities = 'Анапа Анадырь Абакан Альметьевск'  # все с буквы А
dig = '1 2 22 33 44 55 111'  # в строке все числа
string = '1 a1 фb2  c3 abc100 10'  # в строке нет русских букв
string = '1 a1 фb2  c3 abc100 10'  # в строке нет знаков препинания
file_names = 'main.py run.py app.py flask.py'  # все файлы с расширением *.py
cities = 'Анапа \nАнадырь \nАбакан Альметьевск'  # в строк нет спецсимволов
quad = '10 25 49 81 100'  # в строке все полные квадраты


res = (city.istitle() for city in cities.split())
res = map(lambda x: x.istitle(), cities.split())
res = map(lambda x: x.isalnum(), string.split())
res = map(lambda x: x.isascii(), string.split())
res = map(lambda x: x.endswith('.py'), file_names.split())


print(*res)


print('432\n4'.isprintable())
