class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("I am a cat")

    def sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("I am a dog")

    def sound(self):
        print("Bark")

cat = Cat("Kitty", 5)
dog = Dog("Tommy", 8)

for animal in (cat, dog):
    animal.sound()
    animal.info()
