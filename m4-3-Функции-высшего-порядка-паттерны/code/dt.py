from datetime import *
#
# t1 = time(9, 10)
# t2 = time(16, 50)

# print(t2 - t1)

# x = timedelta(t2-t1)

# print()

t1 = timedelta(hours=9, minutes=10)
t2 = timedelta(hours=15, minutes=50)

delta = timedelta(hours=4, minutes=00)

duration = t2-t1


print(duration > delta)
