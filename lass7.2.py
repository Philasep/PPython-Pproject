import math
x = float(input())
y = float(input())
r = float(input())
d = math.sqrt((x**2 + y**2))
if d <= r:
    print("Inside the circle")
else:
    print("Outside the cirlce")





