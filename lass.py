x = float(input())
y = float(input())
z = float(input())

if x + y > z and x + z > y and y + z > x:
    print("Valid Triangle")
else:
    print("Invalid Triangle")