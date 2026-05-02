users={
    "user_0":{"name":"Zero","password":"0000","card_numer":"0000 0000"},
    "user_1":{"name":"Haos","password":"4114","card_numer":"0000 0000"},
    "user_2":{"name":"Rent","password":"3113","card_numer":"0000 0000"},
    "user_3":{"name":"Raya","password":"2112","card_numer":"0000 0000"}

}

products = {
    "Молоко": 12, "Хлеб": 2, "Сыр": 15, "Грибы": 8, "Вода": 2,
    "Яблоко": 5, "Апельсин": 5, "Мясо": 20, "Рыба": 18, "Яйца": 10,
    "Магические Грибы": 33, "Сыр с Плесенью Гнома": 27, "Черный Хлеб": 6, "Синее Молоко": 19, "Огненный Перец": 14,
    "Лунная Соль": 11, "Кристальный Сахар": 13, "Теневой Чай": 16, "Кофе Бездны": 22, "Мед Призрака": 25,
    "Обсидиановая Морковь": 17, "Проклятая Картошка": 9, "Золотой Лук": 12, "Ягоды Свободы": 21, "Суп Странника": 30
}
bag={}
name=""
password=""
card_numer=""
iCount=3
Allcount=0

while True:
    getOut=False
    print("")
    print("     Accaunt")
    print("Log In Or Sing Up")
    logUp=input("> ")
    print("")

    if logUp in ("Log in","Log In","log in","LOG IN","log In"):
        print("User name",end=" ")
        logName=input("> ")
        print("User password",end=" ")
        logPassword=input("> ")
        print("")

        current_user=""
        for iUser in users:
            if users[iUser]["name"]==logName and users[iUser]["password"]==logPassword:
                current_user=iUser
                break

        if current_user=="":
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
                                count=int(input("> "))
                                print("")
                                if prod in bag:
                                    bag[prod]+=count
                                else:
                                    bag[prod]=count
                                print(prod,"was add to bag")
                                print(bag)
                                print("")

                            elif buy in ("not","NOT","n","Not","N"):
                                print("")

                            else:
                                print("sorry answer is unknown")
                                print("")

                        elif prod in ("Products","PRODUCTS","products"):
                            print(products.keys())
                            print("")

                        elif prod in ("EXIT","exit","Exit"):
                            print(bag)
                            print("")
                            break

                        else:
                            print("sorry we dont have this product(")
                            print("")

                elif chooseDo in ("bag","BAG","Bag"):
                    print(bag)
                    print("")
                    print("Buy everythig")
                    print("Delete everythig")
                    print("Exit")
                    bagDo = input("> ")
                    print("")
                    while True:
                        Allcount=0
                        if bagDo in ("buy","BUY","Buy","buy everything","Buy Everything","BUY EVERYTHING"):
                            for iBuy in bag:
                                Allcount+=bag[iBuy]*products[iBuy]
                            print("Products- ",Allcount)
                            print("Count- ",bag)
                            Allcount=0
                            bag.clear()
                            break
                        elif bagDo in ("delete","DELETE","Delete"):
                            bag.clear()
                            break
                        elif bagDo in ("EXIT","exit","Exit"):
                            break
                        else:
                            print("sorry we dont have this product(")


                elif chooseDo in ("Account","ACCOUNT","account"):
                    print(users[current_user])
                    print("")

                    while True:
                        print("Do you want to delete Account? (yes/no)")
                        delete= input("> ")
                        print("")

                        if delete in ("yes","YES","y","Yes","Y"):
                            users.pop(current_user)
                            getOut=True
                            break

                        elif delete in ("not","NOT","n","Not","N","no","No","NO"):
                            print("ok")
                            print("")
                            break

                        else:
                            print("sorry answer is unknown")
                            print("")
                        break

                elif chooseDo in ("EXIT","exit","Exit"):
                    break

                else:
                    print("sorry answer is unknown")
                    print("")

    elif logUp in ("Sing Up","Sing up","sing up","SING UP","sing Up"):
        iCount+=1
        print("User name",end=" ")
        singName=input("> ")
        print("")

        print("User password",end=" ")
        singPassword=input("> ")
        print("")

        users.update({f"user_{iCount}":{"name":singName, "password":singPassword}})
        print("")

    else:
        print("sorry answer is unknown")
        print("")
