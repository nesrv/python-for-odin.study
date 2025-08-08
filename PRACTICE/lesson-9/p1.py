
x = 0
# x = 123,123

print("Начало ...")

try:
    open("file.txt") 
    res = 10 / x    
except Exception as e:
    print (e)
    
    
# else:
#     print("Все хорошо")
# finally:
#     print("Конец")

print("Конец ...")

