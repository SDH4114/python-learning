import webbrowser as webb


def validator(func):
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Сайта не сушествует")
    return wrapper

@validator
def open_url(url):
    webb.open(url)

open_url(input("> "))