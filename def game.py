def game():
    coin=(1,2,5)
    special_number = 8
    start = 0
    lim = 3
    while start<=lim:
        start +=1
        special_number = int(input("guess: "))
        if special_number == 8:
            print(" you won!")
            break
    else:
        x = int(input(f"you have reached the number of limits of the game enter a coin to continue: {coin}"))
        if x != coin[0] or x != coin[1] or x != coin[2]:
            print(" We can only play with R1 or R2 or R5")
        else:
            print(f" you have {x} number of lives in the game, Lets go!!!")
            if x == 1: 
                game()
            elif x == 2:
                game()
                game()
            else:
                game()
                game()
                game()
                game()
                game()
print(" Welcome to the Paradise champ :):)!!")
name = input("What is you name mate? ")
print(f"Nice to meet you {name}:)")
Options = ["Y", "N"]
inqiure = input(f"Do you want to play a number guessing game {name} :)? {Options}:  ")
if inqiure.upper() == "Y":
    print("Great lets start!!!")
    game()
else:
    print("Ouch :( Okay thank you for your time")



