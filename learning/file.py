file = open("data/test.md", "w")
# "w" обнуляет файл и пишет новое
# "a" добавояет к концу файлы
# "r" дает прочитать файл

file.write("Hello\n")
file.write("sweety\n")
# тут по умолчанию нет перехода на новую строчку так что пишем вручную


write = input("> ")
file.write(write+"\n")


file.close()

file = open("data/test.md", "a")
file.write("yeaa\n")

file.close()

file = open("data/test.md","r")

print(file.read()) #вот так выводит весь файл
#если в () написать число то выведится столько то символов
# print(file.read(4)) выйдет Hell

for line in file:
    #print(line) в таком случае выпишется все даже \n которого не видно нам но будет много пропусков
    print(line, end="")

file.close()