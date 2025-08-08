from itertools import product, permutations, combinations

# content = "🧀🍄🍖"

# # Все возможные комбинации из 2 ингредиентов (порядок не важен) 
# combos_2 = product(content, repeat=2)
# print(*combos_2, sep="\n")

# # расположить 3 ингредиента на пицце (порядок важен)

# print('------')

# combos_3 = permutations(content, 2)
# print(*combos_3, sep="\n")


# print('------')
# combos_4 =  combinations(content, 2)
# print(*combos_4, sep="\n")

from random import shuffle, sample
import time

suits = "♠♥♦♣" # Пики, Червы, Бубны, Трефы 
values = ('6','7','8','9','10','J','Q','K','A')

cards = list(product(suits, values))
shuffle(cards)
# извлечь 5 карт

while True:
    time.sleep(0.1)
    sample_cards = sample(cards, 5)
    print(*sample_cards)
    res = filter(lambda x: x[0] == '♦', sample_cards)
    if len(list(res)) == 3:
        print("Победа !")
        break


    # если выпало 3 буби - победа ! 
    # стоп игра
    


# print(*cards, sep="\n")