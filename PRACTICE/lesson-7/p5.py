# 5! = 1 * 2 * 3 * 4 * 5 = 120
# F(n) = F(n-1) * n


def F(n):
    if n == 1: 
        return 1
    return F(n-1) * n

res = F(5)
print(res)



# 1,1, 2,3,5,8,12, 21 - Фиббоначи

# F(1) = 1, F(2) = 1
# F(n) = F(n-1) + F(n-2)

def fib(n):    
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(8))

# datetime @ lambda

