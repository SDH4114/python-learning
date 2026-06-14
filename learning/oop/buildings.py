class Building:
    def __init__(self, year = None, city = None, cost = None):
        self.__year = year
        self.__city = city
        self.__cost = cost

        # __year и другие это инкапсуляцыя но в pythone она плохая и просто не дает менять ее

    def get_info(self):
        print("Year -",self.__year,", city -",self.__city,", cost- ", self.__cost)


class House(Building): # класс House наследует ВСЕ из класса Building

    def __init__(self, people = None, year = None, city = None, cost = None):
        super().__init__(year, city, cost)
        self.__people=people

    def get_info(self):
        super().get_info()
        print("People -",self.__people)


class School(House): # класс School наследует ВСЕ из класса House
    def __init__(self, people, year, city, cost):
        super().__init__(people, year, city, cost)


class Shop(Building): # класс Shop наследует ВСЕ из класса Building
    pass


school = School(1000, 2000, "Baku", "2M")
house = House(1300,2016, "Shuvalan", "1M")
shop = Shop(2000, "Baku", "50K")

school.get_info()
house.get_info()
shop.get_info()

