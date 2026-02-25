x = float(input("Weight: "))
y = input(" (L)ls or (K)g: ")
if y.upper() == "K":
   P = x*2.20462
   print(f"You are {P} Pounds")
elif y.upper() =="L":
   K = x/2.20462
   print(f"you are {K} Kilograms ")
else:
   print("only Kilograms and pounds")
   
  