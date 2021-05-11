class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness

    def eat_food(self):
        self.fullness += 10

    def get_love(self):
        self.happiness += 10
    
    def be_alive(self, hunger, mopiness):
        self.happiness -= hunger
        self.fullness -= mopiness

    def print_stats(self):
        print(self.name + "'s Fullness is: " + str(self.fullness))
        print(self.name + "'s Happiness is: " + str(self.happiness))
        print(self.name + "'s Hunger is: " + str(self.hunger))
        print(self.name + "'s Mopiness is: " + str(self.mopiness))

class FloofyPet(Pet):
    def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level

    def eat_food(self):
        self.fullness += 10

    def get_love(self):
        self.happiness += 10
    
    def be_alive(self):
        self.happiness -= self.hunger
        self.fullness -= self.mopiness/2
    
    def cuddle(self, other_pet):
        for i in range(self.cuddle_level):
            other_pet.get_love()

    def print_stats(self):
        print(self.name + "'s Fullness is: " + str(self.fullness))
        print(self.name + "'s Happiness is: " + str(self.happiness))
        print(self.name + "'s Hunger is: " + str(self.hunger))
        print(self.name + "'s Mopiness is: " + str(self.mopiness))
        print(self.name + "'s Cuddle Level is: " + str(self.cuddle_level))

#VARIABLES
petList = []
userInputChoice = 0


#FUNCTIONS
# print divider
# user choice
# print out pet list
# Add pet to pet list
# Add floofy pet to list
# print out pet stats
# take actions on pet by name

def printDivider():
    print("--------------------------------")

def userChoice(userInputChoice):
    printDivider()
    userInputChoice = int(input("1. Print the pet list\n2. Add a pet to the list\n3. Add a Floofy pet to the list\n4. Print out a pet's stats\n5. Pet Actions\n6. Quit\n"))
    if(userInputChoice == 1):
        printPets(petList)
    if(userInputChoice == 2):
        addPet(petList)
    if(userInputChoice == 3):
        addFloofyPet(petList)
    if(userInputChoice == 4):
        printPetStats(petList)
    if(userInputChoice == 5):
        petActions(petList)
    if(userInputChoice == 6):
        quit()

def printPets(petList):
    printDivider()
    print("Your pets: ")
    for pet in petList:
        print(pet.name)
    userChoice(userInputChoice)

def findInPetList(name):
    for pet in petList:
        if(pet.name == name):
            return pet
    print(name + " is not in your pet list.")

def addPet(petList):
    printDivider()
    #Get name, fullness, happiness, hunger, mopiness
    newPetName = input("Please enter the new pet's name: ")
    newPetFullness = input("Please enter the new pet's Fullness: ")
    newPetHappiness = input("Please enter the new pet's Happiness: ")
    newPetHunger = input("Please enter the new pet's Hunger: ")
    newPetMopiness = input("Please enter the new pet's Mopiness: ")
    newPet = Pet(newPetName, newPetFullness, newPetHappiness, newPetHunger, newPetMopiness)
    petList.append(newPet)
    print(newPet.name + " has been added to the pet list!")
    userChoice(userInputChoice)

def addFloofyPet(petList):
    printDivider()
    #Get name, fullness, happiness, hunger, mopiness
    newPetName = input("Please enter the new pet's name: ")
    newPetFullness = input("Please enter the new pet's Fullness: ")
    newPetHunger = input("Please enter the new pet's Hunger: ")
    newPetCuddleLevel = input("Please enter the new pet's cuddle level: ")
    newPet = FloofyPet(newPetName, newPetFullness, newPetHunger, newPetCuddleLevel)
    petList.append(newPet)
    print(newPet.name + " has been added to the pet list!")
    userChoice(userInputChoice)

def printPetStats(petList):
    #print pet stats based on name
    printDivider()
    userInputPetName = input("Please enter the name of the pet you would like to view: ")
    for pet in petList:
        if(pet.name == userInputPetName):
            pet.print_stats()
            userChoice(userInputChoice)
            return
    print(userInputPetName + " is not in your pet list.")
    userChoice(userInputChoice)
    
def petActions(petList):
    printDivider()
    userInputPetName = input("Please enter the name of the pet you would like to interact with: ")
    foundPet = findInPetList(userInputPetName)
    print(foundPet.name)
    userInputActionChoice = input("What action would you like to take with your pet?\n1. Eat Food\n2. Get Love\n3. Be Alive\n4. Cuddle\n5. Cancel")
    if(userInputActionChoice == 1):
        foundPet.eat_food()
        print(foundPet.name + "'s Fullness increased!")
    if(userInputActionChoice == 2):
        foundPet.get_love()
        print(foundPet.name + "'s Happiness increased!")
    if(userInputActionChoice == 3):
        foundPet.be_alive()
        print(foundPet.name + "'s Fullness & Happiness decreased")
    if(userInputActionChoice == 4):
        if(isinstance(foundPet, FloofyPet)):
            userSecondPetInput = input("Please enter another pet for " + foundPet.name + " to cuddle: ")
            secondPet = findInPetList(userSecondPetInput)
            if(secondPet):
                foundPet.cuddle(secondPet)
                print(foundPet.name + "cuddled " + secondPet.name + " and increased their Happiness!")
    if(userInputActionChoice == 5):
        return
    userChoice(userInputChoice)


#LOGIC/UPDATE
print("Welcome to the pet app")
userChoice(userInputChoice)
