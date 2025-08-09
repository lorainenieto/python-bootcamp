class Character:
    def __init__(self, health = 10, strength=10, defense=10):
        self.health = health
        self.strenght = strength
        self.defense = defense

    def attack (self, other):
        damage = self.strenght - other.defense
        other.health -= damage


class Knight:
    def __init__(self, health = 10, defense = 10):
        self.health = health
        self.defense = defense
    def attack(self, other):
        damage = self.defense - other.health
        other.health -= damage

player = Knight(defense = 100)
enemy = Character()
player.attack(enemy)
















