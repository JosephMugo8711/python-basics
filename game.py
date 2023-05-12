print("Welcome to Treasure Island. Your mission is to find the treasure")
name = input("What is your name?\n")

cross_roads = (input("You are at a cross road, do you want to go right or left?\n")).lower()

if cross_roads == 'right':
    print(f"Hi {name}, Game over 🔥🔥🔥")
else:
    lake = (input("You have reached a lake, do you want to swim or wait for a boat?\n")).lower()
    if lake == "swim":
        print(f"Hi {name}, Game over 🔥🔥🔥")
    else:
        door = (input("You have passed the lake, you need to choose a door. Red, Yellow or Blue?/n")).lower()
        if door == "red" or door == "blue":
            print(f"Hi {name}, Game over 🔥🔥🔥")
        else:
            print("You win")