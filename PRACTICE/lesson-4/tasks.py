from statistics import mean


bals = '3 3 2 4 4 5 4 3 2 пять одын'
# найти средний балл и вывести его на экран с точностью до десятых
bals = bals.split()

# s = 0
# for x in bals:
#     s += int(x)
# avg = s/ len(bals)
# print(round(avg, 1))
# списковое включение

# bals = [int(x) for x in bals if x.isdigit()]
# print(bals)
# print(sum(bals) / len(bals))
# print(mean(bals))


# balls = "один один два три"
# balls = balls.split()
# new_balls = []

# for ball in balls:
#     if ball == "один":
#         new_balls.append(1)
#     elif ball == "два":
#         new_balls.append(2)
#     elif ball == "три":
#         new_balls.append(3)
        
# print(new_balls)


# +7(xxx)xxx-xx-xx
# +7(912)123-45-67
# Необходимо преобразовать ее в список lst 
# (посимвольно, то есть, элементами списка будут являться отдельные символы строки).
# Затем, удалить первый '+', число 7 заменить на 8 и убрать дефисы.


tlf = "+7(912)123-45-67"
tlf = tlf.replace("+7", "8").replace("-", "")
tlf = list(tlf)
print(tlf)
tlf ="".join(tlf)
print(tlf)
