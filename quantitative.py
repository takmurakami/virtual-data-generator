import random

temp = 20
w_per_min = 3000
time = 0

print("time, temp[℃]")
print("0.0, 20.0")

while temp < 100:
    temp += 3000 / 420 / 2
    time += 0.5
    if temp > 100:
        temp = 100
    print(str(time) + ", " + str(temp + random.randint(0, 30) / 10))
