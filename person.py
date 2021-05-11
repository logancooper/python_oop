class Person:
    friendsList = []
    greetingCount = 0
    
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print('Hello %s, I am %s!' % (other_person.name, self.name))
        self.greetingCount += 1
        print(self.greetingCount)

    def printContactInfo(self):
        print("My name is %s, my phone number is %s, and my email is %s" % (self.name, self.phone, self.email))

    def addFriend(self, newFriend):
        self.friendsList.append(newFriend)
    
    def numFriends(self):
        print("I have " + str(len(self.friendsList)) + " friends")

    #def __str__(self):



sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

sonny.printContactInfo()
jordan.printContactInfo()

sonny.addFriend(jordan)
sonny.numFriends()
