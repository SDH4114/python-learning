def str_to_float(st):
    try:
        sf = float(st)
        return st
    except ValueError:
        print("sorry but this is impsoble")

print(str_to_float(input("> ")))
