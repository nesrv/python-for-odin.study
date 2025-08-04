# print("Hello", "World", sep=' !!! ', file=open('test.txt', 'w'))

def sum2(a, b):
    return a + b


c = sum2(1, 2)
print(c)
result = sum2(sum2(4, -2), 7) + 12  # ?
print(result)


def my_abs_Galina(x):
    if x < 0:
        x*(-1)
    return x

def my_abs_Dmitry(x):
    return x if x > 0 else -x


def my_abs_Alex(x):
    return int(str(x).lstrip("-"))


x = my_abs_Galina(-10)
print(x)
