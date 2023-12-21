class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Generic animal sound")


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Lion(Mammal):
    def make_sound(self):
        print(f"{self.name} the Lion, aged {self.age}, makes a roar!")


class Elephant(Mammal):
    def make_sound(self):
        print(f"{self.name} the Elephant, aged {self.age}, makes a trumpet sound!")


class Parrot(Bird):
    def make_sound(self):
        print(f"{self.name} the Parrot, aged {self.age}, makes a squawk!")


class Eagle(Bird):
    def make_sound(self):
        print(f"{self.name} the Eagle, aged {self.age}, makes a screech!")


def zoo_announcement(animals):
    for animal in animals:
        animal.make_sound()


# Create instances of animals
lion = Lion("Simba", 5)
elephant = Elephant("Dumbo", 3)
parrot = Parrot("Polly", 2)
eagle = Eagle("Eddie", 4)

# Test the zoo_announcement function
animals_in_zoo = [lion, elephant, parrot, eagle]
zoo_announcement(animals_in_zoo)
