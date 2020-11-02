import math

x = float(input("Введіть x: "))

if x**2 + math.log(x) > 0:
    y = math.cos(x**2 + math.log(x))
elif x**2 + math.log(x) == 0:
    y = 1/(x**2 + math.log(x))
elif x**2 + math.log(x) < 0:
    y = math.cos(x)

print(f"y = {y}")