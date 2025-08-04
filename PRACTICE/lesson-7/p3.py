#  Необходимо определить, является ли это слово палиндромом
#  (одинаково читается вперед и назад, например, АННА)
#  с помощью функции. Если палиндром, на экран вывести True, иначе - False.


# def get_palindrome(word):
#     word = word.lower()
#     print("YES" if word == word[::-1] else "NO")


# get_palindrome("Анна")
# get_palindrome("шалаШ")
# get_palindrome("привет")


# Объявите функцию для проверки числа на нечетность
# (возвращается True, если переданное число нечетное и False, если число четное)

def is_odd(x):
    return x % 2 != 0


# print(is_odd(3))
# st = [8, 11, -15, 3, 2, 10]
# st = [x for x in st if is_odd(x)]
# print(st)
# [11, -15, 3]


# Объявите функцию с именем is_triangle, которая принимает
# три стороны треугольника (целые числа) и проверяет,
# можно ли из переданных аргументов составить треугольник.
#  длина третьей стороны всегда должна быть меньше суммы двух других

def is_triangle(a, b, c):
    return a+b > c and a+c > b and b+c > a


print(is_triangle(3, 4, 5))
print(is_triangle(3, 4, 8))


def tr(a, b, c):
    return max(a, b, c) < ((a+b+c)-max(a, b, c))


print(tr(3, 4, 5))
print(tr(1, 1, 2))
