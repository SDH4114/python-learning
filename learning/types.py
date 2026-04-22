num= 5 # int целое число
point= 3.14 # float число с точкой
word= "Hello" # str строка
bool= True # bool true/false
print(num," = ", type(num)) # <class 'int'>
print(point," = ", type(point)) # <class 'float'>
print(word," = ", type(word)) # <class 'str'>
print(bool," = ", type(bool)) # <class 'bool'>
#type() показывает какая это переменя тип


test=4
del test # удаляет переменую
# print(test) выдаст ошибку так как переменая удалена

print(word+str(point)) # str() меняет переменую на строку так же есть int() и float()
print(" ")

print(word[1:4])# пишет только эти сиволы (1 2 3) ell отсчет идет с 0
print(word[0]) # пишет только этот символ H
print(word[-1]) # пишет только этот символ o отсчет идет с конца
print(word[:3]) # пишет только эти сиволы (0 1 2) Hel
print(word[3:]) # пишет только эти сиволы (3 4)

print(word*3)