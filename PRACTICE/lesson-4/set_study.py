# множество
# изменяемое, уникальные значения
# неупорядоченная структура
# нет индексов
# что может хранить множество - неизменяемые типы
# list & set

mn = set()
mn = {0,1,2,4,3,2,3, False, True, (1,2,3)}
print(mn)

mn.add(101)
mn.add(101)

print(mn)

mn.update([6,7,8,9,10,"hello"])

print(mn)

mn.remove("hello")
# mn.remove("hello")
mn.discard("hello")
mn.discard("hello")

mn.pop()
mn.clear()
print(mn)

print(mn[0])
print(mn[-1])

