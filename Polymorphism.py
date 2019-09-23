class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow"


myDog = Dog("Jimmy")

myCat = Cat("Tom")

# CAN CALL COMMON METHOD(S) OF DIFFERENT CLASS
for pet in [myDog, myCat]:
    print(pet.speak())
