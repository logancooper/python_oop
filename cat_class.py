class Cat:
    # Attributes
    species = 'mammal'

    # Constructor
    def __init__(self, name, age):
        self.catName = name
        self.catAge = age

    # Methods
    def describe(self):
        print("%s is %d years old." % (self.catName, self.catAge))

orville = Cat("Orville", 3)
finnegan = Cat("Finnegan", 6)

