count = 0
running = True
while running:
    choice =input("Provide command:")
    match choice:
        case "add":
            count +=1
            print(count)
        case "sub":
            count-=1
            print(count)
        case "double":
            count*=2
            print(count)
        case _:
            running = False