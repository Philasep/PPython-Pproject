Ls = ["rock","scissors", "paper"]
x = input()
y = input()
if x == Ls[0] and y == Ls[1]:
    print("Player 1 wins")
elif x == Ls[1] and y == Ls[2]:
    print("Player 1 wins")
elif x == Ls[2] and y == Ls[0]:
    print("Player 1 wins")
elif x ==Ls[0] and y == Ls[2]:
    print("Player 2 wins")
elif x == Ls[1] and y ==Ls[0]:
    print("Player 2 wins")
elif x == Ls[2] and y == Ls[1]:
    print("Player 2 wins")
else:
    print("Tie")