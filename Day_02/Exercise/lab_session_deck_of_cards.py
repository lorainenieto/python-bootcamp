
from random import choice
def create_deck() -> list[str]:
    """Return a list of 52 strings containing a standard deck"""
    deck =[]
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'k']
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    for rank in ranks:
        for suit in suits:
            deck.append(f"{rank} of {suit}")
    return deck
def draw_top(deck: list[str], count: int=1)-> list[str]:
    """Remove count return count cards from the start from deck"""
    bottom = deck.pop(0)
    return bottom
def draw_bottom(deck: list[str], count: int=1) -> list[str]:
    """Remove and return count cards from the end of the deck"""
    top = deck.pop(-1)
    return top
def draw_random(deck: list[str], count: int=1) -> list[str]:
    """Remove and return count random cards from the deck"""
    random_card = choice(deck)
    deck.remove(random_card)
    return random_card
def show(deck):
    """Print all cards in deck"""
    for card in deck:
        print(card)


create_deck()