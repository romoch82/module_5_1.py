class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('"Такого этажа не существует"')
        else:
            for new_floor in range(new_floor+1):
                if new_floor < 1:
                    continue
                print(new_floor)



h1 = House('ЖК "Эльбрус"', 30)
h2 = House('Домик мини', 2)

h1.go_to(5)
h2.go_to(10)