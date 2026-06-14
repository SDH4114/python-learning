import books

def validator(func):
    def checker(book):
        for i in books.books_list:
            if book.lower() == i.lower():
                print("This book exists")
                func(i)
                return

        print("Sorry we didnt find a book.")

    return checker

def find_book():
    print("Write book name.")
    book = (input("> "))

    return book


@validator # open_book = validator(open_book)
def open_book(book):
    print("Opening book:", book)


open_book(find_book())