#PARENT CLASS
class Animal:
    def __init__(self):
        pass

    def speak(self):
        pass
                                       #POLYMORPHISM IS BASICALLY FUNCTION OVERIDING
#CHILD CLASS
class Dog(Animal):
    def __init__(self):
        pass
    def speak(self):
        print("I am a dog and i bark")

#SECOND CHILD CLASS
class Cat(Animal):
    def __init__(self):
        pass
    def speak(self):
        print("i am a cat and i meow")



#CREATING INSTANCES
Dog1=Dog()
Dog1.speak()

Cat1=Cat()
Cat1.speak()