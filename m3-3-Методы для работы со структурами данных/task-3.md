# Задачи на множества

__Задача 2.__ Вводятся два списка целых чисел каждый с новой строки (в строке наборы чисел через пробел). 

Необходимо выбрать и отобразить на экране уникальные числа, присутствующие и в первом и во втором списках одновременно. 

Результат выведите на экран в виде строки чисел, записанных по возрастанию через пробел, используя команду (здесь s - это множество):

print(*sorted(s))

### Входные данные:
```
8 11 12 15 -2
4 11 10 15 -5 1 -2
```
### Выходные данные:
```
-2 11 15
```

__Задача 3.__ Вводятся два списка целых чисел каждый с новой строки (в строке наборы чисел через пробел). 

Необходимо выбрать и отобразить на экране уникальные числа, присутствующие в первом списке, но отсутствующие во втором. 

Результат выведите на экран в виде строки чисел, записанных по возрастанию через пробел.

### Входные данные:
```
8 5 3 5 -3 1
1 2 3 4
```
### Выходные данные:
```
-3 5 8
```



__Задача 5.__ На вход программе подаются две строки, состоящие из цифр.

Необходимо определить, верно ли, что в записи этих двух строк используются все десять цифр?



## Задания на zip

__Задание 1__ Вводятся два списка целых чисел. Необходимо попарно перебрать их элементы и перемножить между собой. При реализации программы используйте функции zip и map. Выведите на экран первые три значения, используя функцию next. Значения выводятся в строчку через пробел. (Полагается, что три выходных значения всегда будут присутствовать).

### Входные данные:

```
-7 8 11 -1 3
1 2 3 4 5 6 7 8 9 10
```

### Выходные данные:
```
-7 16 33
```

__Задание 2__ Чек из супермаркета

Дан список покупок в виде словаря с вложенными списками:

```python
receipt = {
    'Наименование': ['HORTEX Фасоль стручк. б/зам', 'Яблоки КРИПС ПИНК отборные', 'ДОБ.НЕК.БОД.ЦИТ.ап/гр/ман/ли', 'СВЯТ.ИСТ.Вода прир.пит.негаз. ПЭТ 5л', 'СПк Свинина с грибами зап. 1к', 'МЯГК ВАФ С ВАР СГ ЯШ', 'КАРТОФЕЛЬ БЕЛЫЙ РАНН', 'ЧУДО Мол.ВАН.стер.фр.2% 200г', 'Пакет майка', 'GOUR.Корм MON PETIT.кош.кур.', 'Ф-Н.Пюре и/яб/абр со сл/сах', 'MATTI Мюсли ОРЕХ/ЯБЛОКО 250г', 'ХЛ.ДОМ Кекс Яг. Лук.нач.ч.см', 'GREENF.Чай GOLD.CEYL.чер.', 'Куриное Филе ПЕТЕЛ.на подл'],
    'Кол-во': [1, 0.466, 2, 1, 0.178, 2, 0.57, 5, 1, 10, 6, 1, 1, 1, 0.758],
    'Цена': [124.9, 129.9, 189.9, 104.9, 699.0, 37.6, 44.9, 44.9, 6.9, 23.9, 57.9, 129.9, 89.9, 119.9, 355.01],
    'Цена со скидкой': [124.9, 129.9, 109.9, 104.9, 699.0, 37.6, 44.9, 44.9, 6.9, 17.9, 34.9, 69.9, 59.9, 69.9, 279.89],
}
```

Каждый список в словаре соответствует колонке таблицы:

Наименование                         | Кол-во |  Цена  | Цена со скидкой
-------------------------------------|-------:|-------:|----------------:
HORTEX ФАСОЛЬ СТРУЧК. Б/ЗАМ          |      1 | 124.90 | 124.90
ЯБЛОКИ КРИПС ПИНК ОТБОРНЫЕ           |  0.466 | 129.90 | 129.90
ДОБ.НЕК.БОД.ЦИТ.АП/ГР/МАН/ЛИ         |      2 | 189.90 | 109.90
СВЯТ.ИСТ.ВОДА ПРИР.ПИТ.НЕГАЗ. ПЭТ 5Л |      1 | 104.90 | 104.90
СПК СВИНИНА С ГРИБАМИ ЗАП. 1К        |  0.178 | 699.00 | 699.00
МЯГК ВАФ С ВАР СГ ЯШ                 |      2 |  37.60 |  37.60
КАРТОФЕЛЬ БЕЛЫЙ РАНН                 |  0.570 |  44.90 |  44.90
ЧУДО МОЛ.ВАН.СТЕР.ФР.2% 200Г         |      5 |  44.90 |  44.90
ПАКЕТ МАЙКА                          |      1 |   6.90 |   6.90
GOUR.КОРМ MON PETIT.КОШ.КУР.         |     10 |  23.90 |  17.90
Ф-Н.ПЮРЕ И/ЯБ/АБР СО СЛ/САХ          |      6 |  57.90 |  34.90
MATTI МЮСЛИ ОРЕХ/ЯБЛОКО 250Г         |      1 | 129.90 |  69.90
ХЛ.ДОМ КЕКС ЯГ. ЛУК.НАЧ.Ч.СМ         |      1 |  89.90 |  59.90
GREENF.ЧАЙ GOLD.CEYL.ЧЕР.            |      1 | 119.90 |  69.90
КУРИНОЕ ФИЛЕ ПЕТЕЛ.НА ПОДЛ           |  0.758 | 355.01 | 279.89

а) Используя функцию ```zip()```, обойдите попарно списки с ценой со скидкой и количеством. Посчитайте суммарную стоимость корзины. Цена в колонке указана за одну единицу товара.

б) Посчитайте суммарную сумму скидки в рублях для всей корзины целиком.

★ в) Найдите товар с самой большой скидкой в *процентах*. Выведите на экран наименование товара размер его скидки в рублях и процентах.

