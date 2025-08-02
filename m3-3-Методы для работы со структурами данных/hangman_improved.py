import random


# 🟩 ⬛ 🟥

words = ['кот', 'дом', 'лес', 'мяч', 'сон', 'луч', 'дым', 'лед']
word = random.choice(words)
guessed = ['_'] * len(word)
lives = 6

print(f"Слово: {' '.join(guessed)} | Жизни: {'❤️' * lives}")

while lives > 0 and '_' in guessed:
    letter = input('Буква: ').lower()
    
    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                guessed[i] = letter
        print('✅ Есть такая буква!')
    else:
        lives -= 1
        print('❌ Нет такой буквы')
    
    print(f"Слово: {' '.join(guessed)} | Жизни: {'❤️' * lives}")

if '_' not in guessed:
    print('🎉 Победа!')
else:
    print(f'💀 Проигрыш! Слово: {word}')