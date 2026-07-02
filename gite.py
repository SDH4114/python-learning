# import os
import datetime as dt
from pyfiglet import Figlet
import subprocess as sp

# написать мини программу которая делает всю отправку репо в гитхаб

# Path(sys.argv[0]).name нормально выводит имя файлы без расширения
# sys.argv[0] выводит имя файла с расшерением

def create_commit(commit_default = None):
    if commit_default is None:
        commit_default = str(dt.date.today())

    # os.system("git add .")
    # os.system(f'git commit -m "{commit_defult}"')

    result_add = sp.run(["git", "add", "."])
    if result_add.returncode != 0:
        print("git add failed")
        return False

    result_commit = sp.run(['git', "commit", "-m", commit_default])
    if result_commit.returncode != 0:
        print("git commit failed")
        return False

    return True

def push():
    print("Do you want to push commit?")

    while True:
        answer = input("> ").lower().strip()
        if answer in ("y","yes"):
            # os.system("git push")
            sp.run(['git','push'])
            break

        elif answer in ("n","not","no"):
            break

        else:
            print("Sorry unknown command")

def main():
    print("Write commit name")
    commit = input("> ").strip()

    if not commit:
        success = create_commit()
    else:
        success = create_commit(commit)

    if success:
        push()
    else:
        print("Nothing to commit/Commit failed")
        return


if __name__ == "__main__":
    main()
    print(Figlet(font='slant').renderText("THANK U"))
