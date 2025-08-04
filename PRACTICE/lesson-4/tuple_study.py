# кортеж tuple

x = tuple()
x = (1,2, 'кортеж')

print(id(x))

x += 1,2 # перегрузка, а не добавление !

print(x)

print(id(x))

x = x * 2

print(x)
print(id(x))

x = tuple("корртеж")
print(x)

print(x.count('р'))
print(x.index('р'))
print(x.index('р'))

x = tuple("кортеж")
y = list("кортеж")
print(x.__sizeof__())
print(y.__sizeof__())


