class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.year = year
        self.model = model

    def print_info(self):
        print(self.year, self.make, self.model)

car = Vehicle('Nissan', 'Leaf', 2015)
car.print_info()
