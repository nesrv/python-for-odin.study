# цикл for

# тип данных range

# r = range(10, -20, -2)

# print(r.__sizeof__())

# print("длина - ", len(r))
# print("0-вой элемент - ", r[0])
# print("макс элемент", max(r))
# print("сумма - ", sum(r))

# print(*r)  # * распаковывает range

# for x in r:
#     print(x, end=" ")

# print()

# печать = print

# for буква in "пайтон":
#     печать(буква)


for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
    if i == 50:
        print("не всё ок")
        break
else:
    print("все ок")
    
