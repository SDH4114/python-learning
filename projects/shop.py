users={
    "user_0":{"name":"Zero","password":"0000","age":17,"card_numer":"0000 0000"},
    "user_1":{"name":"Haos","password":"4114","age":17,"card_numer":"0000 0000"},
    "user_2":{"name":"Rent","password":"3113","age":18,"card_numer":"0000 0000"},
    "user_3":{"name":"Raya","password":"2112","age":17,"card_numer":"0000 0000"}

}

products={"Молоко":12,"Хлеб":2,"Яблоко":5,"Апельсин":5,"Мясо":20,"Вода":2}

bag=[]
name=""
age=0
password=""
card_numer=""
iCount=3

while True:
    accDeleted=False
    print("")
    print("     Accaunt")
    print("Log In Or Sing Up")
    logUp=input("> ")

    if logUp in ("Log in","Log In","log in","LOG IN","log In"):
        print("User name",end=" ")
        logName=input("> ")
        print("User password",end=" ")
        logPassword=input("> ")

        current_user=""
        for iUser in users:
            if users[iUser]["name"]==logName and users[iUser]["password"]==logPassword:
                current_user=iUser
                break

        if current_user=="":
            print("sorry wrong user name or password")
        else:
            while accDeleted == False:
                print("")
                print("Shop")
                print("Bag")
                print("Account")
                print("Exit")
                chooseDo= input("> ")

                if chooseDo in ("Shop","shop","SHOP"):
                    while True:
                        print("write product or exit")
                        prod = input("> ")

                        if prod in products:
                            print(prod," - ", products[prod])
                            print("Do you what to buy?")
                            print("yes or not")
                            buy= input("> ")

                            if buy in ("yes","YES","y","Yes","Y"):
                                bag.append(prod)
                                print(prod,"was add to bag")
                                print(bag)
                            elif buy in ("not","NOT","n","Not","N"):
                                print("")
                            else:
                                print("sorry answer is unknown")
                        elif prod in ("EXIT","exit","Exit"):
                            print(bag)
                            break
                        else:
                            print("sorry we dont have this product(")

                elif chooseDo in ("bag","BAG","Bag"):
                    print(bag)

                elif chooseDo in ("Account","ACCOUNT","account"):
                    print(users[current_user])

                    while True:
                        print("Do you want to delete Account? (yes/no)")
                        delete= input("> ")

                        if delete in ("yes","YES","y","Yes","Y"):
                            users.pop(current_user)
                            accDeleted=True
                            break

                        elif delete in ("not","NOT","n","Not","N","no","No","NO"):
                            print("ok")
                            break

                        else:
                            print("sorry answer is unknown")
                        break

                elif chooseDo in ("EXIT","exit","Exit"):
                    break

                else:
                    print("sorry answer is unknown")

    elif logUp in ("Sing Up","Sing up","sing up","SING UP","sing Up"):
        iCount+=1
        print("User name",end=" ")
        singName=input("> ")

        print("User password",end=" ")
        singPassword=input("> ")

        users.update({f"user_{iCount}":{"name":singName, "password":singPassword}})
        print(users)

    else:
        print("sorry answer is unknown")
# если прочел скажи мышки