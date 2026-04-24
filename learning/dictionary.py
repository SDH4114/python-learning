user = {"name":"Haos", "age":26, "city":"Baku", "job":"Hero", "code":4114, 777:"lucky"}
#тут вместо символов мы используем ключи первый элемент ключь а после : уже его значени
# как ключь можно использовать что хочешь


# instnt= dict(name="Haos", code=4114) так тоже можно НО записывать как ключиь можно только текст

print(user["name"],"is a",user["job"])#просто выводит значения от этих ключей
# Haos is a Hero
# print(user["unknown"]) если ключа нет просто ошибка

print(user.items())#выводит и ключи и значения как кортежи
# dict_items([('name', 'Haos'), ('age', 26), ('city', 'Baku'), ('job', 'Hero'), ('code', 4114), (777, 'lucky')])

for key in user: # for key in user.keys() тоже самое
    print(key)
# вот так мы можем вывести только ключи

for value in user.values():
    print(value)
#вот так мы можем вывести только сами элементы

# а так уже получаем оба
#из за items() мы получаем доступ к значениям
for key, value in user.items():# и можем создать вторую переменую value
    #и она уже равна нашему значению при ключе
    print(key,"-",value)

print(user["age"]) #выйдет 26
print(user.get("age")) #выйдет 26 это одно и тоже


clear_man = {"name": "Amin","age": 20,"job": "programmer"}
print(clear_man)
clear_man.clear()
#чистит весь список
print(clear_man)

user.pop("city") # удоляет конкретный элемент по ключу
#user.popitem()#удаляет последний элемент
print(user)#{'name': 'Haos', 'age': 26, 'job': 'Hero', 'code': 4114, 777: 'lucky'}

print(user.keys())#пишет все ключи
#dict_keys(['name', 'age', 'job', 'code', 777])

print(user.values())#пишет все значения
#dict_values(['Haos', 26, 'Hero', 4114, 'lucky'])
print(user.items())#пишет все ключи- значения
#dict_items([('name', 'Haos'), ('age', 26), ('job', 'Hero'), ('code', 4114), (777, 'lucky')])


user.update({"age":16, "family":{"brother":"Rent","sister":"Raya"}})
#так можно менять и добовлять новые ключь-значение

#user["age"]=16 так тоже можно
print(user)

print("Haos's brother is", user["family"]["brother"])
print("Haos's sister is",user["family"]["sister"])

person={
    "user_1":{
        "name":"Haos",
        "age":26,
        "grades":{"math":100,"physics":100,"chemistery":90}
    },
    "user_2":{
        "name":"Rent",
        "age":27,
        "grades":{"math":100,"physics":90,"chemistery":100}
    },
    "user_3":{
        "name":"Raya",
        "age":26,
        "grades":{"math":90,"physics":90,"chemistery":100}
    }
}
print("Haos's chemistery grades are",person["user_1"]["grades"]["chemistery"])
print("Rent's physics grades are",person["user_2"]["grades"]["physics"])
print("Raya's chemistery grades are",person["user_3"]["grades"]["chemistery"])

if input(">") in user:
    print("KEY FOUND!")
else:
    print("KEY DIDNT FIND")