def summ(*args): # * дает писать сколько угодно аргументов
    print(args) # все переменые сохраняются как картеж
    return sum(args)

print(summ(1,4,5,7))
# (1, 4, 5, 7)
# 17


def data(**args): # ** дает писать сколько угодно аргементов С ИМЕНЕМ
    return args # сохраняется как словарь

print(data(name="Amin",age="16",bd="17 Ferbrary"))
# {'name': 'Amin', 'age': '16', 'bd': '17 Ferbrary'}


def obyem_4d(a,b,*,c,d): # ,*, заставляет писать все следуюшие аргументы С ИМЕНЕМ
    return a*b*c*d

print(obyem_4d(3,5,c=2,d=3))
# 90