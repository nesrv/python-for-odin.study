# d = {}
# d = dict()
# #

# print(type(d))
# d = {
#     "один": 1,
#     "два": 2,
#     "три": 3,
#     0: "zero"
# }

# # print(d)
# # print(d["один"])
# # print(d[0])

# s = "один два два один три".split() # [1 2 2 1 3]
# res = [d[x] for x in s] ## в 1 строчку

# # for word in s:
# #     # print(word, d[word])
# #     res.append(d[word])
    
# print(res)
# print(sum(res))

# s = "один два два один три один".split() 

# # посчитать частоту встречаемости слов
# # {
# #     "один": 3,
# #     "два": 2,
# #     "три": 1
# # }
# d = {}
# for x in s:
#     d[x] = s.count(x)    
# print(d)

# # c = d["пять"]
# d["пять"] = 125
# c = d.get("пять", "нет таких чисел")
# print(c)
# print(d.values())
# print(sum(d.values()))
# print(d.keys())
# print(d.items())

# tlf = "+71234567890 +71234567854 +61234576890 +52134567890 +21235777890 +21234567110 +71232267890".split()
# '''
# tlf = {
#     "+7" : [+71234567890, +71234567854, +71234576890, +71232267890],
#     "+2" : [+21234567110],
#     ...
#  ]
# }
# '''

# dict_tlf = {}

# for t in tlf:
#     dict_tlf[t[:2]] = []

# for t in tlf:
#     dict_tlf[t[:2]].append(t)

# # способ от А.С.
# # for i in tlf:
# #     dict_tlf.setdefault(i[:2], []).append(i)
    
# print(*dict_tlf.items(), sep="\n")

s = '''
Главная home
Python learn-python
Java learn-java
PHP learn-php
'''.strip().splitlines()

d = {}
for st in s:
    x,y = st.split()
    d[x] = y

print(*d.items())


'''
(('Главная', 'home'), ('Python', 'learn-python'), ('Java', 'learn-java'), ('PHP', 'learn-php'))
'''
    











