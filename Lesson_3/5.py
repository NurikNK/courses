import random
number = random.randint(50, 150)
if number <= 100:
    print(list(range(0, number, 2)))
elif number > 100:
    print(list(range(200, number, -2)))