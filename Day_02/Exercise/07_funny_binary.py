numbers_cards = ["1","2","3","4","5","6","7","8","9"]
special_cards = ["+2","skip","reverse"]
super_cards = ["0","+4","color"]
max_cards = 8 * (special_cards + numbers_cards)
min_cards = 4 * super_cards
print(max_cards + min_cards)

#create the binary for letter 'h' as a list of 1s and 0
binary_h = list (bin(ord("h")))
binary_h = binary_h[2:]

#Create the binary for letter 'a as a list of 1s and 0s
binary_a = list (bin(ord("a")))
binary_a = binary_a[2:]

#Create the binary for hahaha
binary = (binary_h + binary_a)*3
print(binary)









