import random

r = random.randrange(1, 10)

a = int(input("Pogodoi broj izmedju 1 i 10\n"))
print(f'uneo si: {a}')

if a == r:
    print("bravo")
if a < r:
    print("broj je veci")
if a > r:
    print("broj je manji")
print(f'zamisljeni broj je bio {r}')