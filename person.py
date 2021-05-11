class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friendsList = []
        self.greetingsList = []
        self.greetingCount = 0

    def greet(self, other_person):
        print('Hello %s, I am %s!' % (other_person.name, self.name))
        self.greetingCount += 1  
        print(self.greetingCount)
        
        foundName = False
        for p in self.greetingsList:
            if(p.name == other_person.name):
                foundName = True
            
        if(foundName == False):
            self.greetingsList.append(other_person)

    def uniqueGreetingsCount(self):
        print(self.name + " has " + str(len(self.greetingsList)) + " unique greetings")
        for g in self.greetingsList:
            print(g)

    def printContactInfo(self):
        print("My name is %s, my phone number is %s, and my email is %s" % (self.name, self.phone, self.email))

    def addFriend(self, newFriend):
        self.friendsList.append(newFriend)
    
    def numFriends(self):
        print("I have " + str(len(self.friendsList)) + " friends")

    def __str__(self):
        return "Person: {} {} {}".format(self.name, self.email, self.phone)


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
molly = Person("Molly", "molly@aol.com", "234-423-5454")

print(*sonny.greetingsList)

sonny.greet(jordan)
sonny.greet(molly)
jordan.greet(sonny)

sonny.printContactInfo()
jordan.printContactInfo()

sonny.addFriend(jordan)
sonny.numFriends()
sonny.uniqueGreetingsCount()
