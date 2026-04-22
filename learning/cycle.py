for i in range(6): #цыкл повторяется 6 раз от 0 до 5
    print(i) #пишет все значения i

print(" ")

for a in range(1,6,2): # первое число от чего начинаем, второе где заканчиваем, третие сколько добавляем
    #количество итерацый 3
    print(a) #выведится числа 1 3 5 каждый раз добавляем 2

print(" ")

for f in range(1,10):
    #количество итерацый 9
    print(f)

print(" ")


sweety="Hello sweety"
countWords=1
for i in sweety: # используем количество символов в количество итерацый
    print(i*2)
    if i == " ":
        countWords+=1
print(countWords,' words were found')


isRun=True
while isRun:
    if input("Plese stop me- ")=="stop":
        isRun=False
        #break


for i in range(10):
    if i ==9:
        break # остонавлявает цыкл

    if i%2==0:
        continue #пропускает итерацыю
    print(i)


hello="hello"
found=None

for i in hello:
    if i=="l":
        Lfounder=True
        break
    else:
        Lfounder=False
print(Lfounder)