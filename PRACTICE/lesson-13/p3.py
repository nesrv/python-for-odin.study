import shutil
# высокоуровневые операции для работы с файлами

# shutil.copy("txt.txt", "txt10.txt")

# shutil.copy2("txt.txt", "txt11.txt") # копирование с сохранением метаданных

# shutil.copytree("sub_dir", "new_folder-1")
# shutil.copytree("..", "new_folder-2")

# shutil.rmtree("new_folder-2")

# shutil.move("txt.txt", "sub_dir//txt2.txt")

# shutil.make_archive("archive", "zip", "sub_dir")
# shutil.make_archive("archive", "gztar", "sub_dir")

# shutil.unpack_archive("archive.tar.gz", "new_folder-4")

usage = shutil.disk_usage("c:\\")
print(usage)
print(f'{usage.total / (1024 ** 3) :.1f}')