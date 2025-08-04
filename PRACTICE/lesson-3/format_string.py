# f-строка 
s1 = "Я люблю"
s2 = "язык Python"
s3 = s1 + " " + s2
print(s3)

s4 = f'{s1 * 2} {s2.upper()} {len(s1)}'
print(s4)

x = 2/3

print(f'{x:.3f}')
print(f'{7:b}')
print(f'{7:e}')

# format

age=18; name="Александр"; 
s1 = "Меня зовут {0}. Мне {1} лет {0}".format(name, age)
print(s1)

s2 = "Меня зовут {name}. Мне {age} лет".format(name=name, age=age)
print(s2)

x =  "%s — главное достоинство программиста. \n\t\t(%s)"
print(x % ("Знание пайтон", "А.Егоров"))







