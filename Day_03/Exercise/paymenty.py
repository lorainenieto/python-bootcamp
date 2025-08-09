class Payment:
    def __init__(self, amount):
        self.amount = amount

    def valid(self):
        return self.amount > 0

#Informal Polymorphism Option
class Coupon:
    def __init__(self, amount):
        self.amount = amount

    def valid(self):
        return not self.expired and self.amount > 0

#Inheritance Option
class Coupon(Payment):
    def __init__(self,amount, expired):
        super().__init__(amount)
        self.expired = expired

    def valid(self):
        return not self.expired and super().valid()


class OnlinePayment(Payment):
    def __init__(self, amount, email):
        super(). __init__(amount)
        self.email = email
    def valid(self):
        return self.email.endswith("@gmail.com") and super().valid()

class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super(). __init__(card_number)
        self.card_number = card_number

    def valid(self):
        return self.card_number.isnumeric() and len(self.card_number.valid) == 16
        return is_16_digits and super().valid()







