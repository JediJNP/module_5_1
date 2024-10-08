print('"Developer - не только разработчик"')

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor

        if new_floor >  self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor+1):
                print(i)


test1 = House('ЖК Строитель', 22)
test2 = House('ЖК Союз', 11)

test1.go_to(7)
test2.go_to(12)