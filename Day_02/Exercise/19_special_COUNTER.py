string = input ('Enter String: ')
special_count = 0
special_char = "!@#$%^&*()"
#Add on to special_count for each special char in string
for item in string:
    if item in special_char:
        special_count += 1
print(special_count)























