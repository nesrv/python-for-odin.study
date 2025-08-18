import os
# print(os.name)
# Создание и удаление папки
# os.mkdir("new_folder")
# os.rmdir("new_folder")
# os.rename("new.txt", "old.txt")
# if os.path.exists("old.txt"):
#     print("File exists")
#     os.remove("old.txt")
# else:
#     print("File does not exist")
#     open("old.txt", "w").close()


# os.makedirs(folders, exist_ok=True)
# os.removedirs(folders)
# os.chdir("c:/")

print("текущее положение на диске", os.getcwd())
# folders = "folder/" * 2
# os.makedirs(folders, exist_ok=True)

# os.replace("old.txt", "C:\\W25\\!REPETITOR\\python-odin\\PRACTICE\\lesson-12\\new.txt")

x = 123

rf'hello {x} world'

fr'hello world'

# print(os.listdir(".."))
# os.chdir("..")

# print(*os.walk("."))

# for x in os.listdir():
#     print(x)

# for _, _, filenames in os.walk("c:\\"):
#     for filename in filenames:        
#         print(filename, end=", ") if filename.endswith(".py") else ...

d = {
    "f": lambda x : x ** 2
}

print(os.stat("p1.py"))