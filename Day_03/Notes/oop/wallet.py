
class Wallet:
    def __init__(self, initial_amount=0):
        self.amount = initial_amount

food_wallet = Wallet(250)
food_wallet.amount += 1000
print("Wallet amount:", food_wallet.amount)


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sleep(self):
        print("I will sleep for eight hours")

    def introduce(self):
        print(f"Hello, my names is {self.first_name} {self.last_name}.")

person = Person("John", "Cena")
person.sleep()
person.introduce()
























