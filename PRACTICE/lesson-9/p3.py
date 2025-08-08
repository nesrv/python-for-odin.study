f = open("books.txt", encoding='utf-8')

for _ in range(3):
    print(f.readline().strip())

f.seek(0)
s = (f.read()
     .replace(',', '')
     .replace('.', '')
     .replace('"', '')
     .split())

print(max(s, key=len))

# s = f.read()
# s = s.strip('.,"').split()


