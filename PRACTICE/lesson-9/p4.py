f = open("fruit.txt", encoding='utf-8')
s = f.read().lower().split()

# dict
d = {}
for word in s:
    d[word] = s.count(word)
    
# отсортировать по значению ?

d = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(*d, sep='\n')

