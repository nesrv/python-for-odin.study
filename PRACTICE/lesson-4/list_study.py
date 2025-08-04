# список

shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

print('Я должен сделать', len(shoplist), 'покупки.')
print('Покупки:')

for item in shoplist:
    print(item)

print("\nТеперь я должен купить рис")

shoplist.append('рис')

print('Теперь мой список покупок таков:', *shoplist)

print('Отсортирую-ка я свой список')
shoplist.sort()

print('Отсортированный список покупок выглядит так:', *shoplist)
print('Первое, что мне нужно купить, это', shoplist[0])

del shoplist[0]
shoplist.append('манго')

print('Теперь мой список покупок:', shoplist)

print('манго' in shoplist)

print(shoplist.count('манго'))

print(shoplist.index('манго'))
print(shoplist.index('манго', 2))

print(id(shoplist), id(shoplist[0]))

# Как избежать ошибки 
while 'манго' in shoplist:
    shoplist.remove('манго')

print(shoplist)

# while shoplist:
#     x  = shoplist.pop()
#     print(x)
shoplist[0] = 'яблоки'
print(shoplist)
print(id(shoplist), id(shoplist[0]))
shoplist.clear()
print(shoplist)

# print(id(shoplist))




