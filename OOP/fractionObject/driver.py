"""Examples."""

from fraction import Fraction

try:
    f4 = Fraction(8,0)
except ZeroDivisionError:
    print("Zero cannot be used as a divisor")

f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = Fraction(1,1)
print(f1+f2)
print(f1+f3)
print(f1*f2)
print(f1-f2)
print(f1/f2)



