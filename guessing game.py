coins = (1,2,5)
special_number = 8
start = 0
lmt = 5
while start<=lmt:
    start += 1
    special_number = int(input("guess: "))
    if special_number == 8:
        print(" you wins")
        break
    else:
        print("you lose!")
else: 
    x = int(input(f"you have reached your limit please enter a coin to continue:{coins} "))
    print(f" you have {x} number of lives in the game")
   