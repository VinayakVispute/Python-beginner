class Mammal:
    def walk(self):
        print("Move")


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


cat = Cat()
cat.walk()
dog=Dog()
dog.walk()