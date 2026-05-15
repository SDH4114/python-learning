# setik = set("hi",4,5,7,9,1,7,5,"hi","oke")
setik = {"hi",4,5,7,9,1,7,5,"hi","oke"}
#множество те же списки только в них не бывает одинаковые списки


hell_set= set("hello")# в таком случае разделает все буквы и удалет одинаковые
print(hell_set)
# {'o', 'h', 'e', 'l'}

print(setik)

#setik[1]=44 невозможно

setik.add(0)
print(setik)
#добавляет значение

setik.update(["32",True,4,"hi",4])
print(setik)
#добавляет {0, 1, 4, 5, <class 'bool'>, 7, 9, '32', 'oke', 'hi'}

setik.remove(True)
#удаляет элемент

setik.pop()
print(setik)
# удаляет первый элемент

setik.clear()
#очисшяет весь список


numi = [3,6,8,2,4,4,9,0,9]

numi = set(numi) #превратили в множество и убрали повторения
print(numi)

new_setik = frozenset([3,6,4,4,9,0,9,"32",True,4,"hi",4,"hi",4,5,7,9,1,7,5,"hi","oke"])
#это картеж + множества нет повторений и нельзя менять