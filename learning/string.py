word="chaos cubed"
big_word="CHAOS CUBED"

print("number of letters c is",word.count("c"))# находит количесто букв c
print("")

print(word,"after \'upper\'",word.upper()) #пишет всю строку капсом
print("is word \"",word,"\" big? answer is", word.isupper())# вся ли строка написана капсом
print("is word \"",word,"\" small? answer is",word.islower())# вся ли строка написана маленькими буквами?

print("")

print(big_word,"after \'lower\'",big_word.lower())#пишет всю строку маленькими буквами
print("is big_word \"",big_word,"\" small? answer is",big_word.islower())# вся ли строка написана маленькими буквами?
print("is big_word \"",big_word,"\" big? answer is", big_word.isupper())# вся ли строка написана капсом

print("")

caplitalizm="fREeDoM SdH"
print(caplitalizm.capitalize()) # метод capitalize() делает первый символ всего стринга большой а все остольные маленькими
#fREeDoM SdH будет Freedom sdh


print("posotion of ao is",word.find("ao")) # find() находит позицыию первого нужного нам символа или сочетания

c_positions=[]
for i in range(len(word)):
    if word[i]=="c":
        c_positions.append(i+1)
print("Positions of letters c are",c_positions)

like="sport,movie,music,cooking,reading"
print(like.split(",")) #split() разделает строку по символу и создает из этого список
# по умолчанию разделяет по пробелу можно так же разбивать по несколько символов
# вот так split(", ") или так split(",") так же есть такое split()
# рузультат ['sport', 'movie', 'music', 'cooking', 'reading']



likes=like.split(",")

for i in range(len(likes)):
    likes[i]=likes[i].capitalize()

result=",".join(likes) # из списка делает все в строку а между элементами ставит знак как тут
# ",".join(likes) то что внутри "" будет разделителем элементов а в () это уже сам список где это делаем
print(result)

word="freedom"
#индк 0123456

print(word[0:4]) # выйдет free выводим мы 0 1 2 3 символы (free)
print(word[-3:]) # выведет все от -3 элемента (d) до конца (dom)
print(word[:6]) # выведет все от 6 элемента (m) до начала (freedo)
print(word[1:-1:2]) # начинает от 1 элм (r) и заканчиваем до -1 (m) оно не включительно
# берем каждый воторой смивол между ними то есть через один 1 3 5 (reo)

listik=[3,8,4,"liberty",3.14,'prism']
print(listik[3:])# выйдет ['liberty', 3.14, 'prism'] от третьего символа и до конца

print("")

mega=["ghost",'unluck',"obsidian",word,big_word,caplitalizm,likes,"pepe","ya deme kudasai"]
print(mega)
print(mega[2:8]) #взяли мы 2 3 4 5 6 7 элементы
print(mega[2:8:2]) #взяли мы 2 4 6 элементы
