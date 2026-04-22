a = int(input("введите- "))
b = int(input("введите- "))

while a<23 and b <24: # проверка выполняется пока а<23 и b<24
    if a>b:
        print(a,"больше",b)
        b+=2 #увеличиваем b для следуюшей проверки
    elif a<b: #проверка что a<b выполняется только если прошлое не верное и следуюшие не будут выпонятся
        print(b,"больше",a)
        a+=2 #увеличиваем адля следуюшей проверки
    else: #выполняется только если все условия не верны
        print(a,"равно",b)
        break #остонавливаем цыкл

huy=input("введите- ")
huy_string=None

if huy.isdigit(): #проверка что huy может ли быть числом
    huy = int(huy) # делаем один раз что бы в этом if каждый раз не писать int(huy)
    if a+b<huy:
        print("хуй всесилен")
        print(a+b,"<",huy)
    elif a+b==huy:
        print("хуй не всесилен(")
        print(a+b,"=",huy)
    else:
        print("хуй не всесилен(")
        print(a+b,">",huy)
        huy=a+b+1 #меняем значение huy
        del a # удаляем переменую по приколу
        del b #удаляем переменую по приколу
else: #противоположный смысл с его if
    print(huy*3) # дублирует текст/умножает цыфру
    huy_string=True
    print("is", huy ,"string?")
    print("answer- ",huy_string)

jmix= "jmix is happy" if huy_string==True else "jmix is sad" # тот же самый if else только в строку
print(jmix)