import math

a = float(input())
b = float(input())
c = float(input())
d = float(input())

mean = (a+b+c+d)/4
print(mean)
var = (mean-a)**2+(mean-b)**2+(mean-c)**2+(mean-d)**2
print(var)
std = math.sqrt(var)
print(std)
