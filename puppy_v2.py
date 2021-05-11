class Pet:
    #Constructor
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
    #Eat Food
    def eat_food(self):
        self.fullness = 10
    #Get Love
    def get_love(self):
        self.happiness += 10
    #Be Alive
    def be_alive(self, hunger, mopiness):
        self.happiness -= hunger
        self.fullness -= mopiness
    #Print Self Stats
    def print_stats(self):
        print(self.name + "'s Fullness is: " + str(self.fullness))
        print(self.name + "'s Happiness is: " + str(self.happiness))
        print(self.name + "'s Hunger is: " + str(self.hunger))
        print(self.name + "'s Mopiness is: " + str(self.mopiness))

class FloofyPet(Pet):
    #Constructor
    def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level
    #Be Alive Override
    def be_alive(self):
        self.happiness -= self.hunger
        self.fullness -= self.mopiness/2
    #Cuddle
    def cuddle(self, other_pet):
        for i in range(self.cuddle_level):
            other_pet.get_love()
    #Print Stats Self Override
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
def printDivider():
    print("--------------------------------")

# user choice
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

# print out pet list
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

# Add pet to pet list
def addPet(petList):
    printDivider()
    #Get name, fullness, happiness, hunger, mopiness
    newPetName = input("Please enter the new pet's name: ")
    newPetFullness = int(input("Please enter the new pet's Fullness: "))
    newPetHappiness = int(input("Please enter the new pet's Happiness: "))
    newPetHunger = int(input("Please enter the new pet's Hunger: "))
    newPetMopiness = int(input("Please enter the new pet's Mopiness: "))
    newPet = Pet(newPetName, newPetFullness, newPetHappiness, newPetHunger, newPetMopiness)
    petList.append(newPet)
    print(newPet.name + " has been added to the pet list!")
    userChoice(userInputChoice)

# Add floofy pet to list
def addFloofyPet(petList):
    printDivider()
    #Get name, fullness, happiness, hunger, mopiness
    newPetName = input("Please enter the new pet's name: ")
    newPetFullness = int(input("Please enter the new pet's Fullness: "))
    newPetHunger = int(input("Please enter the new pet's Hunger: "))
    newPetCuddleLevel = int(input("Please enter the new pet's cuddle level: "))
    newPet = FloofyPet(newPetName, newPetFullness, newPetHunger, newPetCuddleLevel)
    petList.append(newPet)
    print(newPet.name + " has been added to the pet list!")
    userChoice(userInputChoice)

# print out all pet stats
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

# take actions on pet by name
def petActions(petList):
    printDivider()
    #Enter pet name to search
    userInputPetName = input("Please enter the name of the pet you would like to interact with: ")
    #foreach of the pets in the list...
    for pet in petList:
        #if the input matches the pet name...
        if(pet.name == userInputPetName):
            #prompt for another input to choose action
            userInputActionChoice = int(input("What action would you like to take with your pet?\n1. Eat Food\n2. Get Love\n3. Be Alive\n4. Cuddle\n5. Cancel\n"))
            #if the input is 1, tell the pet to eat food, print status, and print success message
            if(userInputActionChoice == 1):
                pet.eat_food()
                pet.print_stats()
                print(pet.name + "'s Fullness increased!")
            #if the input is 2, tell the pet to get love, print status, and print success message
            if(userInputActionChoice == 2):
                pet.get_love()
                pet.print_stats()
                print(pet.name + "'s Happiness increased!")
            #if the input is 3, tell the pet to be alive, print status, and print success message
            if(userInputActionChoice == 3):
                pet.be_alive()
                pet.print_stats()
                print(pet.name + "'s Fullness & Happiness decreased")
            #if the input is 4, tell the pet to cuddle...
            if(userInputActionChoice == 4):
                #if it's a floofy pet...
                if(isinstance(pet, FloofyPet)):
                    #enter another pet's name and search for it in the pet list
                    userSecondPetInput = input("Please enter another pet for " + pet.name + " to cuddle: ")
                    secondPet = findInPetList(userSecondPetInput)
                    #if the search returned a value...
                    if(secondPet):
                        #cuddle the second pet and print confirmation message
                        pet.cuddle(secondPet)
                        print(pet.name + "cuddled " + secondPet.name + " and increased their Happiness!")
            if(userInputActionChoice == 5):
                #quit
                userChoice(userInputChoice)
        else:
            print(userInputPetName + " is not in your pet list")
    userChoice(userInputChoice)


#LOGIC/UPDATE
print("Welcome to the pet app")
userChoice(userInputChoice)
