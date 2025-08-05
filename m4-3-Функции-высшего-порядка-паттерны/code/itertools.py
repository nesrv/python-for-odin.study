from itertools import *
alphabet = '1234'
ap = []
for i in product(alphabet, repeat=5):
    if i.count('1') == 2:
        ap.append(i)
print(len(ap))

# =========================================================

from itertools import product
count = 0
for p in product("ПЯТНИЦА", repeat=5):
    if p.count("Я") == 1 and p[0]!="Н":
        count+=1
print(count)


# =========================================================

alphabet = "ГОД"
con = "ГД"
ar = product(alphabet, repeat=6)  # Размещение с повторением
arl = []
for i in ar:
    arl.append(list(i))
count = 0
for e in arl:
    if e[0] in con:
        count += 1
print(count)


# =========================================================

all_list = [[1, 3, 4], [6, 7, 9], [8, 10, 5]]
print("The original lists are : " + str(all_list))
res = list(product(*all_list))
print("All possible permutations are : " + str(res))


# =========================================================

from itertools import *


class pairMaker:

    def __init__(self, men=None, women=None):
        self.men = men
        self.women = women
        self.pairs = []

    def __call__(self, *args, **kwargs):
        self.pairs = list(product(args[0], args[1]))

    def __repr__(self):
        return str(self.pairs)

    def counter(self):
        return len(self.pairs)

men = ['Иван', 'Сергей']
women = ['Мария', 'Анна', 'Зоя']
#

pairs = pairMaker()
pairs(men, women)

print(pairs) # ('Иван', 'Мария'), ('Иван', 'Анна'), ('Иван', 'Зоя'), ('Сергей', 'Мария'), ('Сергей', 'Анна'), ('Сергей', 'Зоя')
print(pairs.counter()) # 6

# data = tuple(product('АВЕСТ', repeat=5))
# res = data.index(('С', 'В', 'Е', 'Т', 'А'))
# print(res + 1)

class CardDeck:
    def __init__(self):
        self.length = 52
        self.index = 0
        self.__SUITS = ['Пик', 'Бубей', 'Червей', 'Крестей']
        self.__RANKS = [*range(2, 11), 'J', 'Q', 'K', 'A']

    def __len__(self):
        return self.length

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        else:
            suit = self.__SUITS[self.index // len(self.__RANKS)]
            rank = self.__RANKS[self.index % len(self.__RANKS)]
            self.index += 1
            return f'{rank} {suit}'

    def __iter__(self):
        return self


deck = CardDeck()
while True:
    print(next(deck))
