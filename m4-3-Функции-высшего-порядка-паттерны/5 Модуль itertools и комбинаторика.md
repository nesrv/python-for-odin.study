## Комбинаторика в Python

Предположим, что имеется n разных начинок для пиццы:

```python
from math import *
from itertools import *


content = "🍕🧀🍄🍖"

pizza = combinations(content,2)

print(*pizza)

count_pizza = comb(4,2)
print(count_pizza)

```
## itertools

Модуль itertools стандартизирует основной набор быстрых эффективных по памяти инструментов, которые полезны сами по себе или в связке с другими инструментами. 

Вместе они формируют «алгебру итераторов», которая позволяет лаконично и эффективно создавать специализированные инструменты на чистом Python.

Модуль `itertools` находится в стандартной библиотеке Python.

Модуль представляет следующие типы итераторов: 


*Комбинаторные генераторы.
*Бесконечные итераторы;
*Конечные итераторы;




Комбинаторные генераторы:

```python

content = "🍕🧀🍄🍖"

# сочетания перестановки размещения

pizza1 = combinations(content,2)
pizza2 = permutations(content,2)
pizza3 = product(content,repeat=2)
pizza4 = combinations_with_replacement(content,2)

print(*pizza1) # коминации без повторов
print(*pizza2) # перестановки  (сочетания без повторов)
print(*pizza3) # сочетания (все возможные сочетания)
print(*pizza4) #  сочетаний элементов с повторением

print(comb(4,2))
print(perm(4,2))


l1 = (product('ab',repeat=2)) 
l2 = (permutations('ab',2)) 
l3 = (combinations('ab',2)) 
print(*l1)
print(*l2)
print(*l3)
```

### chain()

эта функция объединяет указанные итерируемые объекты в один итерируемый объект. 
Она возвращает итератор, в котором последовательно выполняется перебор элементов каждого итерируемого объекта.

Ввод:
```python
import itertools

colors = ['red', 'green', 'blue']
sizes = ['small', 'medium', 'large']

for item in itertools.chain(colors, sizes):
    print(item)
```


Вывод:
```
red
green
blue
small
medium
large
```


### cycle()

эта функция возвращает итератор, который производит элементы конкретного итерируемого объекта многократно и бесконечно.

Ввод:
```python
import itertools

colors = ['red', 'green', 'blue']

for color in itertools.cycle(colors):
    print(color)
```
Вывод:
```
red
green
blue
red
green
blue
red
...
```