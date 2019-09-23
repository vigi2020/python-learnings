class Animal:
    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an Animal")

    def eat(self):
        print("I am eating")


# INHERITING ANIMAL (BASE CLASS) CLASS IN DOG (DERIVED) CLASS
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    # OVERRIDES ITS BASE CLASS METHOD
    def who_am_i(self):
        print("I am a Dog")


myDog = Dog()
myDog.who_am_i()
myDog.eat()
