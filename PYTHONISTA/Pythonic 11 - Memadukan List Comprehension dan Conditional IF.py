# cara tidak pythonic
listku = [10, 20, 30, 40, 50, 60, 70]
listmu = []
for item in listku:
    if item > 40:
        listmu.append(item)

print(f"listku = {listku}\nlistmu = {listmu}")


print(f"\nPYTHONISTA\n")

# PYTHONIC
listku = [100, 200, 300, 400, 500, 600]
listmu = [item for item in listku if item > 400]
print(f"listku = {listku} \nlistmu = {listmu}")
