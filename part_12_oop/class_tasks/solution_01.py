class Human:

    def __init__(self, health: int):
        self.health = health

    def attack(self):
        print("Human is attacking!")

    def upgrade(self):
        print(f"Upgrading to {self.health + 100}")


class Warrior(Human):
    def __init__(self, health: int, defense: float):
        #    Human(250)
        super().__init__(health)
        self.defense = defense

    def attack(self):
        print("Warrior is attacking!")


class Barbarian(Human):

    def __init__(self, health: int, damage: int):
        super().__init__(health)
        self.damage = damage


class MyPersonalException(Exception):
    pass


human = Human(250)
warrior = Warrior(150, 25.9)
barbarian = Barbarian(110, 300)
person = Person(250)

human.attack()
warrior.attack()
barbarian.attack()
warrior.upgrade()
barbarian.upgrade()
