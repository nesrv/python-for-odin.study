def sum_list(lst):
    s = 0
    for x in lst:
        if type(x) == int:
            s += x
        else:
            s += sum_list(x)
    return s


lst = [1, 2, [1, 2, 3],  4,
       [1, 2, 3, [1, 2, 3, [1, 2, 3]]]
       ]

print(sum_list(lst))

# x = [1, 2, 3]

# print(sum(x))
