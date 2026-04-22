user = {"name":"Haos", "age":26, "city":"Baku", "job":"Hero", "code":4114, 777:"lucky"}
#тут вместо символов мы используем ключи первый элемент ключь а после : уже его значени
# как ключь можно использовать что хочешь


# instnt= dict(name="Haos", code=4114) так тоже можно НО записывать как ключиь можно только текст

print(user["name"],"is a",user["job"])#просто выводит значения от этих ключей
# Haos is a Hero
# print(user["unknown"]) если ключа нет просто ошибка

print(user.items())#выводит и ключи и значения как кортежи
# dict_items([('name', 'Haos'), ('age', 26), ('city', 'Baku'), ('job', 'Hero'), ('code', 4114), (777, 'lucky')])

for key in user:
    print(key)
# вот так мы можем вывести только ключи

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

