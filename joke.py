import time
import os

while True:
    print("Ты в цыкле? (Да или Нет)")
    answer = input("> ")
    time.sleep(0.3)
    os.system("cls" if os.name == "nt" else "clear")
