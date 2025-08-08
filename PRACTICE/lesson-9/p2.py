def count_paths(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    else:
        return count_paths(x+1, y) + count_paths(x+3, y)

    
result = count_paths(1, 9) * count_paths(9, 17)
print(f"Количество программ: {result}")
