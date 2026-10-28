
import math

def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))

result = simple_interest(p, r, t)

print("Simple Interest =", result)
