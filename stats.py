import math

a = float(input())
b = float(input())
c = float(input())
d = float(input())

mean = (a+b+c+d)/4
print(mean)
var = ((a-mean)**2+(b-mean)**2+(c-mean)**2+(d-mean)**2)/4
print(var)
std = var**.5
print(std)