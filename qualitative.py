import random

sizes = ["S", "M", "L", "XL", "3L"]
colors = ["赤", "青", "緑", "黄", "桃", "黒", "白"]
num_employees = 1000  # 従業員数

print("サイズ, 色")
for i in range(num_employees):
    size = random.randint(0, len(sizes) - 1)
    color = random.randint(0, len(colors) - 1)
    print(sizes[size] + ", " + colors[color])
