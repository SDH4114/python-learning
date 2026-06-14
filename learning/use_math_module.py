import my_math_module as mmm

while True:
    print("What do u want?(Ploshad, Obyem, Ploshad treeangel)")
    choose = input("> ").capitalize()

    if choose == "Ploshad":
        try:
            a = int(input("a > "))
            b = int(input("b > "))
            if a>0 and b>0:
                print(mmm.sploshad(a,b))
            else:
                print("Wrong numbers")
        except ValueError:
            print("Wrong numbers")

    elif choose == "Obyem":
        try:
            a = int(input("a > "))
            b = int(input("b > "))
            c = int(input("c > "))
            if a>0 and b>0 and c>0:
                print(mmm.obyem(a,b,c))
            else:
                print("Wrong numbers")
        except ValueError:
            print("Wrong numbers")


    elif choose in ("Ploshad treeangel","Treeangel"):
        try:
            a = int(input("a > "))
            b = int(input("b > "))
            if a>0 and b>0:
                print(mmm.ploshad_treeangel(a,b))
            else:
                print("Wrong numbers")
        except ValueError:
            print("Wrong numbers")

    elif choose == "Exit":
        break
    
    else:
        print("Sorry unknown command")
