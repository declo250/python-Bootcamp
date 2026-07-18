print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice=input("You're at a cross road. Where do you want to go? Type 'left' or 'right'").lower()
if choice == 'left':
    choice2=input("You've come to a lake. There is an island in the middle of the lake.Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()
    if choice2 =='swim':
        print("Attacked by trout. Game over.")
    elif choice2=='wait':
        choice3=input("Which door? Blue,Red,Yellow").lower()
        if choice3=='red':
            print("Burned by fire. Game over.")
        elif choice3=='blue':
            print("Eaten by Beasts. Game over")
        elif choice3=='yellow':
            print("You win")
        else:
            print("Game over")

else:
    print("Fall into a hole. Game over.")
