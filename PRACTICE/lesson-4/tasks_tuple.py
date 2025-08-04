s = 'Мама мыла раму а потом мыла кота и еще мыла пол'

s = s.lower().split()
# списковое влючение

s = [x for x in s if len(x) > 1]

# print(*s)

# s = set(s)
# print(len(s))

# подсчитать число уникальных слов
# как не считать предлоги и союзы ?


x = '8 11 12 15 -2'.split()
y = '4 11 10 15 -5 1 -2'.split()
z = '4 11 10'.split()

x = set(x)
y = set(y)
z = set(z)

# print(x & y)
# print(x ^ y)
# print(z < y)

# Анаграммой называют пару слов, 
# которые состоят из одного и того же набора бук

# - апорт-тропа
# - дежурство - дружество

# s1= 'апорт'
# s2= 'тропы'

# print ('анаграмма +' if set(s1) == set(s2) else 'не анаграмма')

# Необходимо написать программу для проверки пароля на безопасность, 
# в данном случае необходимо соблюсти хотя бы три критерия:
# * Длина пароля не менее 5 символов
# * Содержит буквы латинского алфавита как в верхнем, так и в нижнем регистре
# * Хотя бы одну цифру от 0 до 9
# * Хотя бы один спец.символ: "@,#,%,&

from string import ascii_lowercase, ascii_uppercase, digits

passw = 'aBbcd0@'

if len(passw) > 5 \
    and set(passw) & set(ascii_lowercase) \
        and set(passw) & set(ascii_uppercase) \
            and set(passw) & set(digits)   \
                and set(passw) & set('@#%&'):
    
    print('ok')
else:
    print('not ok')