class Entity:
    def attack(self):
        print(f"Attacking with {self.damage} damage")


class Monster(Entity):
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    # def __repr__(self):
    #     return f"I'm a monster with health: {self.health} and damage: {self.damage}."

    # def __str__(self):
    #     return f"A monster with {self.health} health."


monster = Monster(100, 10)
print(monster.health)
monster.attack()
print(monster)
