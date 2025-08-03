# Функции высшего порядка и функциональные паттерны

### lambda
### map
### reduce
### filter
### хранение функций в словарях





### Функция filter

```python
S.sort( key = lambda x: (x[1]/x[0], -x[1]) )
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

# функция, которая проверяет числа
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False
```

# Применение filter() для удаления нечетных чисел

```python
out_filter = filter(filter_odd_num, numbers)

print("Тип объекта out_filter: ", type(out_filter))
print("Отфильтрованный список: ", list(out_filter))
```
еще пример
```python
lst = ("Москва", "Рязань1", "Смоленск", "Тверь2", "Томск")
b = filter(str.isalpha, lst)

def f(s):
    return s[-1] =="а"

c = filter(f, lst)
print(*b)
print(*c)
```

### Задача 2. Отфильтровать стоп-слова (союзы и предлоги) из строки.

Аналогичным образом можно отфильтровать списки более сложных объектов:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
         
people = [ Person("Tom", 38), Person("Kate", 31), Person("Bob", 42), 
        Person("Alice", 34),  Person("Sam", 25) ]
 
# фильтрация элементов, у которых age > 33
view = filter(lambda p: p.age > 33, people)
  
for person in view:
    print(f"Name: {person.name} Age: {person.age}")
```

В данном случае фильтруем список объектов Person, поэтому в функцию-условие/лямбда-выражение в качестве параметра передается каждый объект `Person` из списка. 

Каждый объект `Person` хранит имя `(Name)` и возраст `(Age)`, и здесь выбираем всех `Person`, у которых возраст больше `33`.

## reduce

Последняя функция из нашей тройки — `reduce()` (говорят "свертка"), который используется для агрегации данных.

Под агрегацией понимается операция, вычисляющая значение, зависящее от всего набора данных. С помощью функции reduce можно последовательно применить операции к элементам списка, чтобы получить единственное значение.

```python
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5]
result = reduce(add, numbers, 0)
print(result)
# 15

result = reduce(multiply, numbers, 1)
print(result)
```

Внутри `reduce` можно использовать и лямбда функции


Аналогичным образом можно получить и выполнить другие функции.


Например, передача лямбда-выражения в качестве параметра:

```python
def do_operation(a, b, operation):
    return operation(a, b)



x1 = do_operation(5, 4, lambda a, b: a + b)
x2 = do_operation(5, 4, lambda a, b: a * b)

print(x1, x2)
```
Бессмысленный пример, но это основа для понимания декораторов и замыканий функций в дальнейшем!

В данном случае нам нет необходимости определять функции, чтобы передать их в качестве параметра, как в прошлом примере.
То же самое касается и возвращение лямбда-выражений из функций:

```python
def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b


operation = select_operation(1)  # operation = sum
print(help(operation)) 
```

Результат:
> <lambda> lambda a, b

Теперь в переменной operation лежит lambda функция
```python
print(operation(10, 6))  # 16

operation = select_operation(2)  # operation = subtract
print(operation(10, 6))  # 4

operation = select_operation(3)  # operation = multiply
print(operation(10, 6))  # 60
```
