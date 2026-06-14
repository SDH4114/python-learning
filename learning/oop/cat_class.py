class Cat:
    name = None
    age = None
    isHappy = None
    colors = []

    def __init__(self, name, age, isHappy, colors): # __something__ это конструктор
        # важная функцыя из за нее в самом начале установления класса к обьекту надо давать параметры

        self.set_data(name, age, isHappy, colors)
        # self. позволяет использовать внутриний метод класса

        self.get_data()
        # self. позволяет использовать внутриний метод класса

        # этот метод будет запускатся сразу при использовании
        # поэтому мы с начало получаем инфу и сразу отдаем

    def set_data(self, name = None, age = None, isHappy = None, colors = None):
        self.name = name # self.name это имено переменая из класса а name это то что вставляем в функцыю
        self.age = age
        self.isHappy = isHappy
        self.colors = colors

    def get_data(self):
        print(self.name,", age -",self.age,", isHappy -",self.isHappy,", Colors -",self.colors)



cat1 = Cat("Meowy", 4, True, ["White","Orange spots","Black spots"])

# cat1.set_data("Meowy",4,True,["White","Orange spots","Black spots"])

# cat1.name = "Meowy"
# cat1.age = 4
# cat1.isHappy = True
# cat1.colors = ["White","Orange spots","Black spots"]

cat2 = Cat("Luck", 1, True, ["Black"])
# cat2.set_data("Luck",1,True,["Black"])

cat3 = Cat("Rin", 2, True, ["Goldy"])

cat4 = Cat("InAss", 4, False, ["Brown"])

# cat1.get_data()
# cat2.get_data()
# cat3.get_data()
# cat4.get_data()