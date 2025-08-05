# Pattern matching

## Конструкция match

Pattern matching (сопоставление шаблонов) представляет применение конструкции `match`, которая позволяет сопоставить выражение с некоторым шаблоном.

И если выражение соответствует шаблону, то выполняются определенные действия.

В этом смысле конструкция match похожа на конструкцию `if/else/elif`, которая выполняет определенные действия в зависимости от некоторого условия.

Однако функциональность `match` гораздо шире - она также позволяет извлечь данные из составных типов и применить действия к различным частям объектов.

```python
match выражение:
    case шаблон_1:
        действие_1
    case шаблон_2:
        действие_2
    ................
    case шаблон_N:
        действие_N
    case _:
        действие_по_умолчанию
```

## Пример 1

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


factorial(5)
```


## Пример использования match

```python
def factorial(n):
    match n:
        case 0 | 1:
            return 1
        case _:
            return n * factorial(n - 1)

factorial(5)
```

## Пример использования match (case _)

```python
def print_hello(language):
    match language:
        case "russian":
            print("Привет")
        case "english":
            print("Hello")
        case "german":
            print("Hallo")
        case _:
            print("Undefined")
 
print_hello("english")      
print_hello("german")       
print_hello("russian")      
```


## Пример использования match | 
### ( вертикальная черта)

```python
def print_hello(language):
    match language:
        case "russian":
            print("Привет")
        case "american english" | "british english" | "english":
            print("Hello")
        case _:
            print("Undefined")
 
 
print_hello("english")              
print_hello("american english")     
print_hello("spanish")                  
```


## Пример использования match. Код операции
### ( вертикальная черта)

```python
def operation(a, b, code):
    match code:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            return a * b
        case _:
            return 0
 
 
print(operation(10, 5, 1))      # 15
print(operation(10, 5, 2))      # 5
print(operation(10, 5, 3))      # 50
print(operation(10, 5, 4))      # 0 
```


## Пример использования match. 
### передача коллекций

```python
def get_color(*color):    
    match color:
        case 1, 1, 1:
            return "white"
        case 0, 0, 0:
            return "black"
        case 1, 0, 0:
            return "red"
        case 0, 1, 0:
            return "green"

        case _:
            raise ValueError("Неизвестный цвет")

res = get_color(0, 1, 0)
print(res)
```



## Пример использования match. 
### кортежи в pathern matching

```python
def print_data(user):
    match user:
        case "Олег", 37:
            print("Наш юзер")
        case "Олег", age:
            print(f"Возраст: {age}")
        case name, 22:
            print(f"Имя: {name}")
        case name, age:
            print(f"Имя: {name} возраст: {age}")


print_data(("Олег", 37))
print_data(("Олег", 28))
print_data(("Сергей", 22))
print_data(("Борис", 41))
print_data(("Олег", 33, "Google"))
```

 конструкция match сравнивает этот кортеж с рядом шаблонов.

 Первый шаблон предполагает, что кортеж `user` точно соответствует набору значений:

>  case "Олег", 37

Второй шаблон соответствует любому двухэлементному кортежу

>"Олег", age

и т.д.


## Списки в pathern matching


Подобным шаблоны также могут содержать либо конкретные значения, либо переменные, которые передаются элементы списков, либо символ прочерка _, если элемент списка не важен

* Первый шаблон предполагает, что элементы списка имеют определенные значения:

* Второй шаблон предполагает, что первый элемент списка должен быть равне строке "Олег", остальные два элемента могут иметь произвольные значения:

При этом значение второго элемента передается в переменную `second`, а значение третьего элемента не важно, поэтому вместо него применяется прочерк.

* Третий шаблон соответствует любому массиву из трех элементов. 

При этом его элементы передаются в переменные `first`, `second` и `third`:

```python
def print_people(people):
    match people:
        case ["Олег", "Сергей", "Борис"]:
            print("Наши люди")
        case ["Олег", second, _]:
            print(f"Второй юзер: {second}")
        case [first, second, third]:
            print(f"{first}, {second}, {third}")


print_people(["Олег", "Сергей", "Борис"])
print_people(["Олег", "Михаил", "Борис"])
print_people(["Алиса", "Вика", "Катя"])
print_people(["Олег", "Катя"])

```


В данном случае для соответствия любому из шаблонов массив должен был иметь три элемента. 

Но также можно определять шаблоны для массивов разной длины

```python
def print_people(people):
    match people:
        case [_]:
            print("Массив из одного элемента")
        case [_, _]:
            print("Массив из двух элементов")
        case [_, _, _]:
            print("Массив из трех элементов")
        case _:
            print("Непонятно")



print_people(["Олег"])
print_people(["Олег", "Михаил"])
print_people(["Алиса", "Вика", "Катя"])
print_people("Олег")

```

### Коллекции неопределенной длины

Если необходимо сравнивать выражение с массивом неопределенной длины, то можно определить значения/переменные только для обязательных элементов массива, а на необязательные ссылаться с помощью символа `*` (звездочки):

```python
def print_people(people):
    match people:
        case [first, *other]:
            print(f"Первый: {first}; остальные: {','.join(other)}")
```

В примере выше применяется параметр `*other`, который соответствует всем остальным элементам. 

То есть шаблон `[first, *other]` соответствует любому массиву, который имеет как минимум один элемент, и этот элемент будет помещаться в параметр `first`. 

Все остальные элементы помещаются в параметр `other`, который представляет массив значений.

Если нам параметр с символом * (other) не важен, но мы по прежнему хотим, чтобы шаблон соответствовал массиву с одним и большим количеством элементов, мы можем использовать подшаблон `*_`:

```python
def print_people(people):
    match people:
        case [first, *_]:
            print(f"Первый: {first}")
```


### Альтернативные значения

Если необходимо сравнивать выражение с массивом неопределенной длины, то можно определить значения/переменные только для обязательных элементов массива, а на необязательные ссылаться с помощью символа * (звездочки):

```python
def print_people(people):
    match people:
        case ["Олег" | "Михаил" | "Сергей",  "Катя"]:
            print("Наши люди", people, )
        case [first, second, third]:
            print(f"{first}, {second}, {third}")


print_people(["Олег",  "Катя"])
print_people(["Михаил", "Катя"])
print_people(["Олег"])
print_people(["Сергей", "Михаил"])
print_people(["Алиса", "Вика", "Катя"])
print_people("Олег")
```

В данном случае первый шаблон соответствует массиву из трех элементов, где первый элемент равен или "Олег", или "Михаил" или "Сергей".

Также можно задать альтернативные значения для отдельных элементов, но и альтернативные массивы:

```python
def print_people(people):
    match people:
        case ["Игорь", "Егор", "Елена"] | ["Гоша", "Егор", "Елена"]:
            print("Игорь/Гоша, Егор, Елена")
        case [first, second, third]:
            print(f"{first}, {second}, {third}")


print_people(["Игорь", "Егор", "Елена"])
print_people(["Гоша", "Егор", "Елена"])


print_people(["Сергей", "Михаил"])
print_people(["Алиса", "Вика", "Катя"])
```

В данном случае первый шаблон будет соответствовать двум массивам 
> ["Игорь", "Егор", "Елена"] | ["Гоша", "Егор", "Елена"]

## Словари в pattern matching

`Pattern matching` позволяет проверить наличие в словаре определнных ключей и значений:

```python
def look(words):
    match words:
        case {"red": "красный", "blue": "синий"}:
            print("Слова red и blue есть в словаре")
        case {"red": "красный"}:
            print("Слово red есть в словаре, а слово blue отсутствует")
        case {"blue": "синий"}:  
            print("Слово blue есть в словаре, а слово red отсутствует")
        case {}:
            print("Слова red и blue в словаре отсутствует")
        case _:
            print("Это не словарь")


look({"red": "красный", "blue": "синий", "green": "зеленый"})
look({"red": "красный", "green": "зеленый"})
look({"blue": "синий", "green": "зеленый"})  
look({"green": "зеленый"})
look("yelllow") 
```

Здесь предполагается, что в функцию look передается словарь. 
* Первый шаблон соответствует словарю, в котором есть два элемента со следующими ключами и значениями: `"red": "красный"` и `"blue": "синий"`.

* Второй шаблон `({"red": "красный"})` соответствует любому словарю, где есть элемент "red": "красный". 

* Третий шаблон `({"blue": "синий"})` соответствует любому словарю, где есть элемент "blue": "синий"

* Четвертый шаблон - `case {}` соответствует в принципе любому словарю.

* Последний шаблон соответствует любому значению и применяется на случай, если в функцию передан не словарь.


## Передача набора значений в словари

С помощью вертикальной черты | можно определить альтернативные значения:

```python
def look(words):
    match words:
        case {"red": "красный" | "алый" | "червонный"}:
            print("Слово red есть в словаре")
        case {}:
            print("Слово red в словаре отсутствует или имеет некорректное значение")


look({"red": "красный", "green": "зеленый"})
look({"red": "алый", "green": "зеленый"})
look({"green": "зеленый"})
```

В данном случае шаблон `{"red": "красный" | "алый" | "червонный"}` соответствует словарю, в котором есть элемент с ключом `"red"` и значением `"красный"` или `"алый"` или `"червонный"`.

Также можно задать альтернативный набор словарей:

```python
def look(words):
    match words:
        case {"red": "красный"} | {"blue": "синий"} :
            print("либо red, либо blue есть в словаре")
        case {}:
            print("надо проверить слова red и blue")
 
 
look({"red": "красный", "green": "зеленый"})  # либо red, либо blue есть в словаре
look({"blue": "синий", "green": "зеленый"}) # либо red, либо blue есть в словаре
look({"green": "зеленый"})    # надо проверить слова red и blue
```


Первый шаблон - `{"red": "красный"} | {"blue": "синий"} `соответствует словарю, в котором есть либо элемент `{"red": "красный"}`, или `{"blue": "синий"}`, или оба.

Если нам важны сами ключи, но не важно значение ключей, то вместо конкретных значений можно передать шаблон _:

```python
def look(words):
    match words:
        case {"red": _, "blue": _}:
            print("Слова red и blue есть в словаре")
        case {}:
            print("red и/или blue отсутствуют в словаре")
 
 
look({"red": "красный", "blue": "синий"})   # Слова red и blue есть в словаре
look({"red": "алый", "blue": "синий"}) # Слова red и blue есть в словаре
look({"red": "красный", "green": "зеленый"})  # red и/или blue отсутствуют в словаре

```

### Получение значений по ключам

`Pattern matching` позволяет получить значения элементов в переменные в виде:

> {ключ: переменная}
```python
def look(words):
    match words:
        case {"red": red, "blue": blue}:
            print(f"red: {red}  blue: {blue}")
        case {}:
            print("надо проверить слова red и blue")
 
 
look({"red": "красный", "blue": "синий"})    # red: красный  blue: синий
look({"red": "алый", "blue": "синий"})    # red: алый  blue: синий
```


В первом шаблоне значение элемента с ключом `"red"` попадает в переменную `red`, а элемента с ключом `"blue"` - в переменную `blue`.

## Получение всех значений

С помощью символов `**` (двойная звездочка) можно получить остальные элементы словаря:

```python
def look(words):
    match words:
        case {"red": red, **rest}:
            print(f"red: {red}")
            for key in rest:        # rest - тоже словарь
                print(f"{key}: {rest[key]}")
 
 
look({"red": "красный", "blue": "синий", "green": "зеленый"})
# red: красный
# blue: синий
# green: зеленый

```
Здесь шаблон `{"red": red, **rest}` соответствует любому словарь, в котором есть элемент с ключом "red". Все остальные элементы словаря помещаются в параметр `rest`, который сам в свою очередь представляет словарь.


Какая разница между `__str__ и __repr__`

```python
print(repr(2 / 3))
print(str(2 / 3))
```

а сейчас?

```python
import datetime
td = datetime.datetime.now()
print(td.__str__())
print(td.__repr__())
```

### pattern matching и классы

Python позволяет использовать в pattern matching в качестве шаблонов объекты классов. Рассмотрим на примере:

### Следующий пример


```python
class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point2D({repr(self.x)}, {repr(self.y)})"

p = Point2D(1,2) # (1, 2)
print(p)
```

Как вызвать метод __repr__?


### Далее. Использование matching в классах

```python
class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f" x = {self.x}, y = {self.y}"

    def describe_point(point):
        match point:
            case Point2D(x=0, y=0):
                desc = "в начале координат"
            case Point2D(x=0, y=y):
                desc = f"на вертикальной оси, {y = }"
            case Point2D(x=x, y=0):
                desc = f"на горизонтальной оси, {x = }"
            case Point2D(x=x, y=y) if x == y:
                desc = f"по линии x = y, при этом x = y = {x}"
            case Point2D(x=x, y=y) if x == -y:
                desc = f"по линии x = -y, где x = {x} и y = {y}"
            case Point2D(x=x, y=y):
                desc = f"c координатами {point}"

        return "Точка : " + desc


p0= Point2D(0, 0)
p1 = Point2D(5, 0)
p2 = Point2D(0, 3)
p3 = Point2D(-3, -3)
p4 = Point2D(1, 2)
print(p0.describe_point())
print(p1.describe_point())
print(p2.describe_point())
print(p3.describe_point())
print(p4.describe_point())

```


### guards или ограничения шаблонов


Guard или ограничения шаблонов позволяют установить дополнительные условия, которым должно соответсвовать выражение. 

Ограничение задается сразу после шаблона с помощью ключевого слова if, после которого идет условие ограничения:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
 
def enter(person):
    match person:
        case Person(name=name, age=age) if age < 18:
            print(f"{name}, доступ запрещен")
        case Person(name=name):
            print(f"{name}, добро пожаловать!")
 
 
enter(Person("Tom", 37))        # Tom, добро пожаловать!
enter(Person("Sam", 12))        # Sam, доступ запрещен

```

первый шаблон cоответствует любому объекту Person, у которого атрибут age меньше 18.
 Собственно часть if age < 18 и представляет ограничение. 
 Соответственно, если у пользователя возраст меньше 18, то будет выводьтся одно сообщение, если больше 18, то другое.

Подобным образом можно вводить дополнительные ограничения:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
 
def enter(person):
    match person:
        case Person(name=name, age=age) if age < 18:
            print(f"{name}, доступ запрещен")
        case Person(name=name, age=age) if age < 22:
            print(f"{name}, доступ  ограничен")
        case Person(name=name):
            print(f"{name}, у вас полноценный доступ!")
 
 
enter(Person("Tom", 37))        # Tom, у вас полноценный доступ!
enter(Person("Bob", 20))        # Bob, доступ  ограничен
enter(Person("Sam", 12))        # Sam, доступ запрещен
```

Условия ограничений могут быть более сложными и составными по структуре:

```python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 

def check_data(data):
    match data:
        case name, age if name == "admin" or age not in range(1, 101):
            print("Некорректные значения")
        case name, age:
            print(f"Данные проверены. Name: {name}  Age: {age}")
 
 
check_data(("admin", -45))      # Некорректные значения
check_data(("Tom", 37))         # Данные проверены. Name: Tom  Age: 37
 
 
enter(Person("Tom", 37))        # Tom, у вас полноценный доступ!
enter(Person("Bob", 20))        # Bob, доступ  ограничен
enter(Person("Sam", 12))        # Sam, доступ запрещен
```

В данном случае функция получает кортеж data. 

Оба шаблона в конструкции match соответствуют двухэлементному кортежу. 

Но первый шаблон также применяет ограничение name == "admin" or age not in range(1, 101), 
в соответствии с которым первый элемент кортежа должен иметь значение "admin", а второй должен находиться вне диапазона 1-101.


### Установка псевдонимов и паттерн AS

Оператор as позволяет установить псевдоним для значения шаблона или для всего шаблона. 
Простейший пример:

```python
def print_person(person):
    match person:
        case "Tom" | "Tomas" | "Tommy" as name:
            print(f"Name: {name}")
        case _:
            print("Undefined")
 
 
print_person("Tom")     # Name: Tom
print_person("Tomas")   # Name: Tomas
print_person("Bob")     # Undefined

```

Здесь первый шаблон соответствует трем строкам: "Tom" | "Tomas" | "Tommy". 

После набора значений идет оператор as, после которого указывается псевдоним. 
И вне зависимости от того, какая именно строка передана, она окажется в переменной name.

Псевдоним можно применять как для отдельного значения шаблона, так и для всего шаблона:
```python
def print_person(person):
    match person:
        case ("Tom" | "Tomas" as name, 37 | 38 as age):   # псевдонимы для отдельных значений
            print(f"Tom| Name: {name}  Age: {age}")
        case ("Bob" | "Robert", 41 | 42) as bob:          # псевдоним для всего шаблона
            print(f"Bob| Name: {bob[0]}  Age: {bob[1]}")
        case _:
            print("Undefined")
 
 
print_person(("Tomas", 38))     # Tom| Name: Tomas  Age: 38
print_person(("Robert", 41))    # Bob| Name: Robert  Age: 41
```

Обычно псевдонимы более применимы в каких-то более сложных по структуре данных. 
Например:

```python
class Person:
    __match_args__ = ("name", "age")
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
 
def print_family(family):
    match family:
        case (Person() as husband, Person() as wife):
            print(f"Husband. Name: {husband.name}  Age: {husband.age}")
            print(f"Wife. Name: {wife.name}  Age: {wife.age}")
        case _:
            print("Undefined")
 
 
print_family((Person("Tom", 37), Person("Alice", 33)))
# Husband. Name: Tom  Age: 37
# Wife. Name: Alice  Age: 33
 
print_family((Person("Sam", 28), Person("Kate", 25)))
# Husband. Name: Sam  Age: 28
# Wife. Name: Kate  Age: 25
```

Здесь функция print_family принимает кортеж, который должен состоять из двух элементов Person. 
В первом шаблоне определяем для первого элемента псевдоним husband, а для второго - псевдоним wife. 
Затем, используя эти псевдонимы, мы можкем обращаться к их атрибутам.