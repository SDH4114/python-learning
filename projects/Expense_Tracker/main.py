import json
import datetime as dt
from pathlib import Path

def load_expenses():
    try:
        with open(Path(__file__).parent / "expenses.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File didnt find")
        return []
    except json.decoder.JSONDecodeError:
        print("File is empty or broken")
        return []

def save_expenses(expenses):
    with open(Path(__file__).parent / "expenses.json", "w", encoding="utf-8") as file:
        json.dump(expenses, file, ensure_ascii=False, indent=4)




def add_expense(expenses):
    print("Write title")
    title = input("> ")

    print("Write category")
    category = input("> ").lower()

    while True:
        try:
            print("Write amount")
            amount = float(input("> "))
            if amount>0:
                break
            else:
                print("Amount cant be negative")
        except ValueError:
            print("""
Sorry but write amount not text
                  """)

    expenses.append({"title":title, "category":category,"amount":amount, "date":f"{dt.datetime.now().date()}"})
    save_expenses(expenses)


def show_expenses(expenses):
    for i in expenses:
        print(f"""Title - {i["title"]}
Category - {i["category"]}
Amount - {i["amount"]}
Date - {i["date"]}
""")


def show_total(expenses):
    total_count_in = 0
    for i in expenses:
        print(f""" Title - {i["title"]}
Amount - {i["amount"]}
""")
        total_count_in += i["amount"]

    return total_count_in


def show_by_category(expenses):
    categories = {}

    for expense in expenses:
        category = expense["category"]

        if category not in categories:
            categories[category]=0

        categories[category] += expense["amount"]

    for category, total, in categories.items():
        print(f"{category} - {total}")

def most_expensive(expenses):
    max_expense = expenses[0]

    for expense in expenses:
        if expense["amount"] > max_expense["amount"]:
            max_expense = expense

    print(f"""Title - {max_expense["title"]}
Category - {max_expense["category"]}
Amount - {max_expense["amount"]}
Date - {max_expense["date"]}
""")


def menu(expenses):

    while True:
        print("""
Expense Tracker

1. Add expense
2. Show expenses
3. Show total
4. Show by category
5. Show most expensive
6. Exit
    """)

        chooseDo= input("> ").lower()
        print()
        if chooseDo in ("add expense", "add", "1"):
            add_expense(expenses)
            print()

        elif chooseDo in ("show expenses", "show", "2"):
            if not expenses:
                print("No expenses yet")
            else:
                show_expenses(expenses)
                input("waiting...")
            print()

        elif chooseDo in ("show total","total","3"):
            if expenses:
                print(f"Total amount - {show_total(expenses)}")
                print()
                input("waiting...")
            else:
                print("No expenses yet")
            print()

        elif chooseDo in ("show by category", "category", "4", "show category"):
            if not expenses:
                print("No expenses yet")
            else:
                show_by_category(expenses)
                input("waiting...")
            print()

        elif chooseDo in ("show most expensive","most expensive","expensive","5"):
            if not expenses:
                print("No expenses yet")
            else:
                most_expensive(expenses)
                input("waiting...")
            print()

        elif chooseDo in ("exit","6"):
            break
        else:
            print("Sorry unknown command")
        print()


def main():
    expenses = load_expenses()
    menu(expenses)

if __name__ == "__main__":
    main()