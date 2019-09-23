class Animal:
    def __init__(self, name):
        self.name = name

    # ABSTRACT METHOD
    def speak(self):
        raise NotImplementedError("Subclass must will implement this abstract method")


class Dog(Animal):
    # ABSTRACT METHOD IS OVERRIDDEN HERE
    def speak(self):
        return self.name + " says woof"


class Cat(Animal):
    # ABSTRACT METHOD IS OVERRIDDEN HERE
    def speak(self):
        return self.name + " says meow"


myDog = Dog("Jimmy")
print(myDog.speak())

myCat = Cat("Tom")
print(myCat.speak())
