print("Welcome to Treasure Island.\nYour mission is to find the treasure")

directions = input("left or right?/L or R: ")

# color = input("which door?/B, R, Y: ")

if directions.upper() == "R":
    print("Fall into a hole.\nGame Over.")
elif directions.upper() == "L":
    action = input("swim or wait?/S or W: ")
    if action.upper() == "S":
        print("Attacked by trout.\nGame Over.")
    elif action.upper() == "W":
        color = input("which door?/B, R, Y: ")
        if color.upper() == "B":
            print("Eaten by beasts.\nGame Over.")
        elif color.upper() == "R":
            print("Burned by fire.\nGame Over.")
        elif color.upper() == "Y":
            print("You Win!")
        else:
            print("Game Over.")