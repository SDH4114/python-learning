import os

print(os.getcwd())
# выводит текушую директорию

if not os.path.isdir('osi'): # првоеряет есть ли тут папка
    os.mkdir('osi')
# создает папку один раз потом дает ошибку
os.chdir('osi')
print(os.getcwd())

try:
    os.makedirs('one/two/tree/four') # создает много папок
except FileExistsError:
    print("This folder are exist")

os.chdir('one')

file = open("test.md", "w+")
file.write("Something very cool")
file.close

os.chdir('..')
print(os.getcwd())

print(f"How do u want to call file {file.name}")
rename = input("> ")

os.rename('one/test.md', f"one/{rename}.md")

input()

os.replace(f"one/{rename}.md", f"one/two/tree/{rename}.md")

os.chdir('..')
print(os.listdir())

with open("osi/one/two/tree/deletme.md", "w+") as file:
    file.write("YEEE")


for dirpath, dirnames, filenames in os.walk('.'):
    for dirname in dirnames:
        print(f"Каталог {os.path.join(dirpath, dirname)}")
    for filename in filenames:
        print(f"Файл {os.path.join(dirpath, filename)}")

if os.path.isfile('osi/one/two/tree/deletme.md'):
    os.remove("osi/one/two/tree/deletme.md")
else:
    print("file doesnt exist")


os.rmdir("osi/one/two/tree/four") # папки должны быть пустыми
# os.removedirs удаляет много папок ПУСТЫХ
