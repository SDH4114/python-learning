import json

def load_users():
    with open("projects/shop/users.json", "r", encoding="utf-8") as file:
        return json.load(file)

def save_users(users):
    with open("projects/shop/users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

def load_bag():
    with open("projects/shop/bags.json", "r", encoding="utf-8") as file:
        return json.load(file)

def save_bag(bag):
    with open("projects/shop/bags.json", "w", encoding="utf-8") as file:
        json.dump(bag, file, ensure_ascii=False, indent=4)


products = {
    "Молоко": 12, "Хлеб": 2, "Сыр": 15, "Грибы": 8, "Вода": 2,
    "Яблоко": 5, "Апельсин": 5, "Мясо": 20, "Рыба": 18, "Яйца": 10,
    "Магические Грибы": 33, "Сыр с Плесенью Гнома": 27, "Черный Хлеб": 6, "Синее Молоко": 19, "Огненный Перец": 14,
    "Лунная Соль": 11, "Кристальный Сахар": 13, "Теневой Чай": 16, "Кофе Бездны": 22, "Мед Призрака": 25,
    "Обсидиановая Морковь": 17, "Проклятая Картошка": 9, "Золотой Лук": 12, "Ягоды Свободы": 21, "Суп Странника": 30
}

users = load_users()
bags = load_bag()
iCount= len(users)


def LogIn(users):
    print("User name",end=" ")
    logName=input("> ")
    print("User password",end=" ")
    logPassword=input("> ")
    print("")

    current_user=""
    for iUser in users:
        if users[iUser]["name"]==logName and users[iUser]["password"]==logPassword:
            current_user=iUser
            if current_user not in bags:
                bags[current_user]={}
                save_bag(bags)
            break
    return current_user

def SingUp(users,iCount):
    print("User name",end=" ")
    singName=input("> ")
    print("")

    print("User password",end=" ")
    singPassword=input("> ")
    print("")

    print("User card number",end=" ")
    singCard=input("> ")
    print("")

    users.update({f"user_{iCount}":{"name":singName, "password":singPassword,"card_number":singCard}})
    save_users(users)
    print("")
    return users , iCount

def Account(users, current_use):
    getOut=False
    print(users[current_use])
    print("")

    while True:
        print("Do you want to delete Account? (yes/no)")
        delete= input("> ")
        print("")

        if delete in ("yes","YES","y","Yes","Y"):
            users.pop(current_use)
            bags.pop(current_use)
            getOut=True
            save_users(users)
            save_bag(bags)
            break

        elif delete in ("not","NOT","n","Not","N","no","No","NO"):
            print("ok")
            print("")
            break

        else:
            print("sorry answer is unknown")
            print("")
    return getOut

def Shop(products, user_bag):
    while True:
        print("write product or exit")
        print("if you want see all products write \"Products\"")
        prod = input("> ")
        print("")

        if prod in products:
            print(prod," - ", products[prod])
            print("Do you what to buy?")
            print("yes or not")
            buy= input("> ")
            print("")

            if buy in ("yes","YES","y","Yes","Y"):
                print("How many?")
                count=input("> ")
                while count.isdigit() == False or int(count)<0:
                    print("How many?")
                    count=input("> ")

                count = int(count)
                if count >0:
                    print("")
                    if prod in user_bag:
                        user_bag[prod] += count
                    else:
                        user_bag[prod] = count
                    print(prod, "was add to bag")
                    print(user_bag)
                    save_bag(bags)
                    print("")
                else:
                    print("count must be more than 0")

            elif buy in ("not","NOT","n","Not","N"):
                print("")

            else:
                print("sorry answer is unknown")
                print("")

        elif prod in ("Products","PRODUCTS","products"):
            for keys, values in products.items():
                print(keys ," - ", values)
            print("")

        elif prod in ("EXIT","exit","Exit"):
            print(user_bag)
            print("")
            break

        else:
            print("sorry we dont have this product(")
            print("")


def Bag(products, user_bag):
    for keys, values in user_bag.items():
        print(keys," - ",values)
    print("")
    print("Buy  everything")
    print("Delete  everything")
    print("Exit")
    while True:
        bagDo = input("> ")
        print("")
        Allcount=0
        if user_bag and bagDo in ("buy","BUY","Buy","buy everything","Buy Everything","BUY EVERYTHING"):
            for iBuy in  user_bag:
                Allcount+= user_bag[iBuy]*products[iBuy]
            print("Products- ",Allcount)
            print("Count- ",user_bag)
            Allcount=0
            user_bag.clear()
            save_bag(bags)
            break
        elif bagDo in ("delete","DELETE","Delete"):
            user_bag.clear()
            save_bag(bags)
            break
        elif bagDo in ("EXIT","exit","Exit"):
            break
        else:
            print("sorry we didnt understand your answer(")


while True:
    getOut=False
    print("")
    print("     Accaunt")
    print("Log In Or Sing Up")
    logUp=input("> ")
    print("")

    if logUp in ("Log in","Log In","log in","LOG IN","log In"):
        current_use = LogIn(users)
        if current_use=="":
            print("sorry wrong user name or password")
            print("")
        else:
            while getOut == False:
                print("")
                print("Shop")
                print("Bag")
                print("Account")
                print("Exit")
                chooseDo= input("> ")
                print("")

                if chooseDo in ("Shop","shop","SHOP"):
                    Shop(products, bags[current_use])

                elif chooseDo in ("bag","BAG","Bag") and bags[current_use]:
                    Bag(products, bags[current_use])

                elif not bags[current_use] and chooseDo in ("bag","BAG","Bag"):
                    print("Sorry but you dont have anything in bag")

                elif chooseDo in ("Account","ACCOUNT","account"):
                    getOut = Account(users,current_use)

                elif chooseDo in ("EXIT","exit","Exit"):
                    break

                else:
                    print("sorry answer is unknown")
                    print("")

    elif logUp in ("Sing Up","Sing up","sing up","SING UP","sing Up"):
        iCount= len(users)+1
        SingUp(users,iCount)
    else:
        print("sorry answer is unknown")
        print("")
