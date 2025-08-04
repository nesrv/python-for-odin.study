# print("Hello", "World", sep=' !!! ', file=open('test.txt', 'w'))

import time


def sum2(a, b):
    return a + b


# c = sum2(1, 2)
# print(c)
# result = sum2(sum2(4, -2), 7) + 12  # ?
# print(result)


def my_abs_Galina(x):
    if x < 0:
        x = x*(-1)
    return x

def my_abs_Dmitry(x):
    return x if x > 0 else -x


def my_abs_Alex(x):
    return int(str(x).lstrip("-"))

def my_abs(x):
    return abs(x)


t0 = time.time()
for _ in range(10**7):
    x =  my_abs(-10)

t1= time.time()
print(t1-t0) # 1.89 # 1.84  # 4.33 # 1.87


print(x)

# x =  my_abs_Dmitry(-10)
# print(x)

# x =  my_abs_Alex(-10)
# print(x)

