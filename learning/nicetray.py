try:
    a = int(input("> "))
    b = int(input("> "))
    b=0
    print(a/b)
except ZeroDivisionError:
    print("Нельзя делить на 0")
except ValueError:
    print("Не то значение")
else:
    print("если не сработало прошлое")
finally:
    print("работает всегда")

file = open("data/test.md", "w")

while True:
    try:
        print("Ведите число")
        wr = int(input("> "))
        file.write(str(wr))
        break
    except (ValueError, FileNotFoundError):
        print("Ведите число")
    finally:
        file.close()
        print("все отключил файл")
