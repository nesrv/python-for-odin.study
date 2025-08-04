def my_sum(*a):
    s = 0
    for x in a:
        s += x
    return s


r = my_sum(1, 2, 3, 4, 5)
# print(r)


# def avg(*args, точность=4, значок="*"):
def avg(a,b, *args, **kwargs):  
    точность = kwargs.get("точность", 4)
    значок = kwargs.get("значок", "*")  
    x = sum(args) / len(args)
    x = round(x, точность)
    x = str(x)
    x = x.rjust(10, значок)
    return x


r = avg(10,20, 1, 1, 2, точность=2, значок="#" )
print(r)
