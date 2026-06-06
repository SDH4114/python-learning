import json

def load_users():
    with open("users.json", "r", encoding="utf-8") as file:
        return json.load(file)

def save_users(users):
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)



def load_bag():
    with open("bags.json", "r", encoding="utf-8") as file:
        return json.load(file)

def save_bag(bag):
    with open("bags.json", "w", encoding="utf-8") as file:
        json.dump(bag, file, ensure_ascii=False, indent=4)



def load_quests():
    with open("quests.json", "r", encoding="utf-8") as file:
        return json.load(file)

def save_quests(quests):
    with open("quests.json", "w", encoding="utf-8") as file:
        json.dump(quests, file, ensure_ascii=False, indent=4)



products = {
    "Молоко": 12, "Хлеб": 2, "Сыр": 15, "Грибы": 8, "Вода": 2,
    "Яблоко": 5, "Апельсин": 5, "Мясо": 20, "Рыба": 18, "Яйца": 10,
    "Магические грибы": 33, "Сыр с плесенью гнома": 27, "Черный хлеб": 6, "Синее молоко": 19, "Огненный перец": 14,
    "Лунная соль": 11, "Кристальный сахар": 13, "Теневой чай": 16, "Кофе бездны": 22, "Мед призрака": 25,
    "Обсидиановая морковь": 17, "Проклятая картошка": 9, "Золотой лук": 12, "Ягоды свободы": 21, "Суп странника": 30
}

users = load_users()
bags = load_bag()
iCount= len(users)
quests = load_quests()

def logIn_func(users):
    print("User name")
    logName=input("> ")
    print("User password")
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

def singUp_func(users,iCount):
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

def account_func(users, current_use):
    getOut=False
    print(users[current_use])
    print("")

    while True:
        print("Do you want to delete Account? (yes/no)")
        delete= input("> ")
        print("")

        if delete.capitalize() in ("Yes","Y"):
            users.pop(current_use)
            bags.pop(current_use)
            quests.pop(current_use)

            getOut=True
            save_users(users)
            save_bag(bags)
            break

        elif delete.capitalize() in ("Not","N","No"):
            print("ok")
            print("")
            break

        else:
            print("sorry answer is unknown")
            print("")
    return getOut

def shop_func(products, user_bag):
    while True:
        print("write product or exit")
        print("if you want see all products write \"Products\"")
        prod = input("> ")
        print("")

        if prod.capitalize() in products:
            print(prod," - ", products[prod])
            print("Do you what to buy?")
            print("yes or not")
            buy= input("> ")
            print("")

            if buy.capitalize() in ("Yes","Y"):
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

            elif buy.capitalize() in ("No","Not","N"):
                print("")

            else:
                print("sorry answer is unknown")
                print("")

        elif prod.capitalize() == "Products":
            for keys, values in products.items():
                print(keys ," - ", values)
            print("")

        elif prod.capitalize() == "Exit":
            print(user_bag)
            print("")
            break

        else:
            print("sorry we dont have this product(")
            print("")


def quests_func(current_use,quests):
    print("Quests Board")
    print("Accepted Quests")
    print("Apply Quest")
    print("")

    questDo=input("> ")

    if questDo.capitalize() in ("Quests board","Board"):
        for key, value in quests.items():
            print(key, " - ", value)
    elif questDo.capitalize() in ("Accepted quests","Accepted"):
        print("soon")
    elif questDo.capitalize() in ("Apply quest","Apply"):
        create_quest_func(quests)
        print("")
    else:
        print("bad blabla")

def create_quest_func(quests):
#   for key, dificult in user_quest.items():
#       print(key, " - ", dificult)

    print("Do you want to apply quest?")
    print("Yes or Not")
    questDo = input("> ")

    if questDo.capitalize() in ("Yes","Y"):
        print("Write goal")
        questGoal = input("> ").capitalize()

        print("Write dificult")
        questDif = input("> ").capitalize()

        need_dic = {}
        
        print("Write need thinghs (stop)")
        while True:
            print("What you need?")
            needAdd=input("> ").capitalize()
            print("")
            if needAdd == "Stop":
                break

            print("How many?")
            needAddCount = int(input("> "))
            need_dic.update({needAdd:needAddCount})

        print("Write reward")
        quesreward = input("> ").capitalize()

        quests.update({questGoal:{"dificult":questDif,"need":need_dic,"reward":quesreward}})
        save_quests(quests)


def bag_func(products, user_bag):
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
        if user_bag and bagDo.capitalize() in ("Buy","Buy everything"):
            for iBuy in  user_bag:
                Allcount+= user_bag[iBuy]*products[iBuy]
            print("Products- ",Allcount)
            print("Count- ",user_bag)
            Allcount=0
            user_bag.clear()
            save_bag(bags)
            break
        elif bagDo.capitalize() == "Delete":
            user_bag.clear()
            save_bag(bags)
            break
        elif bagDo.capitalize() == "Exit":
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

    if logUp.capitalize() == "Log in":
        current_use = logIn_func(users)
        if current_use == "":
            print("sorry wrong user name or password")
            print("")
        else:
            while getOut == False:
                print("")
                print("Shop")
                print("Quests")
                print("Bag")
                print("Account")
                print("Exit")
                chooseDo= input("> ")
                print("")

                if chooseDo.capitalize() == "Shop":
                    shop_func(products, bags[current_use])

                elif chooseDo.capitalize() == "Quests":
                    quests_func(current_use,quests)

                elif chooseDo.capitalize() == "Bag" and bags[current_use]:
                    bag_func(products, bags[current_use])

                elif not bags[current_use] and chooseDo.capitalize() == "Bag":
                    print("Sorry but you dont have anything in bag")

                elif chooseDo.capitalize() == "Account":
                    getOut = account_func(users,current_use)

                elif chooseDo.capitalize() == "Exit":
                    break

                else:
                    print("sorry answer is unknown")
                    print("")

    elif logUp.capitalize() == "Sing up":
        iCount= len(users)+1
        singUp_func(users,iCount)
    else:
        print("sorry answer is unknown")
        print("")
