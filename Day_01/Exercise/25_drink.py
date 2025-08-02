"""
Create a function brew that takes a parameter 'drink' and ;extra and prints the following format;

I made you a {drink] with {extra}
"""
#
# def brew(drink, extra):
#     print(f"I made you {drink} with {extra}")
#
# brew("coffee", "sugar")
# brew("tea", "milk")


"""
Create a function brew that take a parameter 'drink' and "extra"
 and prints the following formate
 I made you {drink} with {extra}
 But make the extra optional
"""
def brew(drink, extra = None):
    if extra == None:
        print(f"I made you {drink}")
    else:
        print(f"I made you {drink} with {extra}")

brew("coffee", "sugar")
brew("tea", "milk")
brew("matcha")