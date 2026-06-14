import datetime as dt , time , os , platform as plt
# datatime дает работать и с датой и с временем    time только со временем и задержки (sleep)
from math import sqrt as sq , ceil


def alarm():
    print("Write alarm time.(Example: 14:14)")
    alarmTime = input("> ")
    now = dt.datetime.now().strftime("%H:%M")

    if now < alarmTime:
        while True:
            time.sleep(5)# пауза 5 секунд
            now = dt.datetime.now().strftime("%H:%M")
            if now >= alarmTime:
                print(now)
                break
    else:
        print("Write another time.")

def timer():
    print("Write timer duration.(in seconds)")
    try:
        timerDur = int(input("> "))
        if timerDur >0:
            time.sleep(timerDur)
            print("Time Out")
        else:
            print("Wrong time")
    except ValueError:
        print("Wrong time")

def oss():
    print("Ur os name",os.name,"- based on", plt.system())


def sqrte():
    while True:
        print("Write any number.")
        try:
            if num < 0:
                print("Number must be positive.")
                continue

            print(sq(num))
            print("Do u want ceil it?")
            ceilIt = input("> ").capitalize()

            if ceilIt in ("Y","Yes"):
                print(ceil(sq(num)))
            elif ceilIt in ("N","Not","No"):
                break
            else:
                print("Sorry unknown command")

        except ValueError:
            print("Sorry write number.")


while True:
    print("What do u want? (alarm or timer or os settings or sqrt ,exit)")
    altiChoose= input("> ").capitalize()

    if altiChoose == "Alarm":
        alarm()
        break
    elif altiChoose == "Timer":
        timer()
        break
    elif altiChoose in ("Os","Settings","Os settings"):
        oss() 
        break
    elif altiChoose == "Sqrt":
        sqrte()
        break
    elif altiChoose == "Exit":
        break
    else:
        print("Sorry unknown command")
