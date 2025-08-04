
R,G,B = 1,1,1

R,G,B = map(int,(input().split()))

match R,G,B:
    case 1, 0, 0:    print("Красный")
    case 0, 1, 0:    print("Зеленый")
    case 0, 0, 1:    print("Синий")
    case 1, 1, 0:    print("Желтый")
    case 1, 0, 1:    print("Пурпурный")
    case 0, 1, 1:    print("Бирюзовый")
    case 1, 1, 1:    print("Белый")
    case 0, 0, 0:    print("Черный")


    


    
    