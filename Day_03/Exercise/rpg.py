from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, health = 10, defense=10):
        self.health = health
        self.defense = defense

    @abstractmethod
    def attack(self, other):
        raise NotImplementedError()


class Knight:
    def __init__(self, health = 10, defense = 10):
        super().__init__(health, defense)
    def attack(self, other):
        damage = self.defense - other.health
        other.health -= damage

class Mage(Character):
    def __init__(self, health = 10, defense = 10, magic=20):
        super().__init__(health, defense)
        self.magic = magic

    def attack(self, other):
        damage = self.magic - other.health
        other.health -= damage


class Warrior(Character):
    def __init__(self, health = 10, defense = 10, strength = 20):
        super().__init__(health, defense)
        self.strength = strength

    def attack(self, other):
        damage = self.strength - other.health
        other.health -= damage

k1 = Knight(defense=40)
k2 = Knight()












