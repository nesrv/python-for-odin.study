f = open("file.txt", encoding='utf-8')  # ASCII

s = f.read()
s = s.split('; ')
s = list(map(int, s))
# print(sum(s) / len(s))


lst = []
for i in range(len(s)-1):
    print(s[i], + s[i+1])  
    
    if s[i] % 3 == 0 or s[i+1] % 3 == 0:      
        lst.append(s[i] + s[i+1])

print(len(lst) , max(lst))
open('txt.txt', 'a')