import random

s = ['книга', 'месяц', 'ручка', 'шарик', 'олень', 'носок']

random_word = random.choice(s)
base_word = ['\u25A0'] * 5
lifes = 3

print(*base_word, ' \u2665 ' * lifes)

while 1:
    attempt = input('Назовите букву или слово целиком -> ')
    if attempt in random_word:
        ind = random_word.index(attempt)
        base_word[ind] = attempt
    else:
        print('Неправильно. Вы теряете жизнь')
        lifes -= 1

    print(*base_word, ' \u2665 ' * lifes)
    if ''.join(base_word) == random_word:
        break

print('Ты угадал слово')

