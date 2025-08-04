import random

word = random.choice(['домофон'])
lives = 3
guessed = ['_'] * len(word)

print(''.join(guessed), '❤️' * lives)

while lives > 0 and '_' in guessed:
    letter = input("Введите букву: ")    
    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                guessed[i] = letter
    else:
        lives -= 1
    
    print(''.join(guessed), '❤️' * lives)

print("Вы выиграли!" if '_' not in guessed else "Вы проиграли!")
