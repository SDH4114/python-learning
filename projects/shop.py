users={
    "user_0":{"name":"Zero","password":"0000","age":17,"card_numer":"0000 0000"}
}

name=""
age=0
password=""
card_numer=""
i=0

while True:
    print("     Accaunt")
    print("Log In Or Sing Up")
    logUp=input("> ")
    if logUp in ("Log in","Log In","log in","LOG IN","log In"):
        print("User name",end=" ")
        logName=input("> ")
        print("User password",end=" ")
        logPassword=input("> ")

        for i in users:
            if users[i]["name"]==logName and users[i]["password"]==logPassword:
                print("Succses!")

    elif logUp in ("Sing Up","Sing up","sing up","SING UP","sing Up"):
        i+=1
        print("User name",end=" ")
        singName=input("> ")
        print("User password",end=" ")
        singPassword=input("> ")
        users.update({f"user_{i}":{"name":singName, "password":singPassword}})
        print(users)


