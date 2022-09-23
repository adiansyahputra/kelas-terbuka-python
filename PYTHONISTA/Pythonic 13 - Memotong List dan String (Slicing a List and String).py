# cara tidak pythonic
listku = [10, 20, 30, 40, 50, 60]
listmu = []
for i in range(2, 5):
    listmu.append(listku[i])
print(f"listmu = {listmu}")


print(f"\nPYTHONISTA\n")

# PYTHONIC
listku = [100, 200, 300, 400, 500, 600]
listmu = listku[2:5]
print(f"listmu = {listmu}")
