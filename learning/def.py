def fonk(a):
    for i in range(a):
        print("toodoon!")

fonk(int(input("toodoon count> ")))

def summe(a,b):
    return a+b
# с помошью return result мы вытаскиваем значение из функцыи в переменую
#без этого в переменой было бы пусто none

res = summe(3,4)
print(res)

print(summe("AY","YA!"))

lama_y= lambda x,k,b: k*x+b
y=lama_y(int(input("x- ")),int(input("k- ")),int(input("b- ")))
print(y)
#lambda это таже функцыя но проше и пишется в одну строчку и в ней не нужен return