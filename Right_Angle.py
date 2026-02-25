import math

print("Right Triangle Calculator")
print("1. Use 2 sides")
print("2. Use 1 side + angle (radians)")

choice = input("Choose option (1/2): ")


if choice == "1":
    print("Which sides do you have?")
    print("1. Opposite + Adjacent")
    print("2. Opposite + Hypotenuse")
    print("3. Adjacent + Hypotenuse")

    sides = input("Choose (1/2/3): ")

    if sides == "1":
        opposite = float(input("Enter opposite: "))
        adjacent = float(input("Enter adjacent: "))
        hypotenuse = math.sqrt(opposite**2 + adjacent**2)
        print("Hypotenuse:", hypotenuse)

    elif sides == "2":
        opposite = float(input("Enter opposite: "))
        hypotenuse = float(input("Enter hypotenuse: "))
        adjacent = math.sqrt(hypotenuse**2 - opposite**2)
        print("Adjacent:", adjacent)

    elif sides == "3":
        adjacent = float(input("Enter adjacent: "))
        hypotenuse = float(input("Enter hypotenuse: "))
        opposite = math.sqrt(hypotenuse**2 - adjacent**2)
        print("Opposite:", opposite)

    else:
        print("Invalid choice")

elif choice == "2":
    side = float(input("Enter known side: "))
    angle = float(input("Enter angle in radians: "))

    print("Which side do you want to find?")
    print("1. Opposite")
    print("2. Adjacent")
    print("3. Hypotenuse")

    target = input("Choose (1/2/3): ")

    if target == "1":
        opposite = side * math.sin(angle)
        print("Opposite:", opposite)

    elif target == "2":
        adjacent = side * math.cos(angle)
        print("Adjacent:", adjacent)

    elif target == "3":
        hypotenuse = side / math.sin(angle)
        print("Hypotenuse:", hypotenuse)

    else:
        print("Invalid choice")

else:
    print("Invalid option")