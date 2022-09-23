# cara tidak pythonic
for i in range(3):
    print(f"hello world")


print(f"\nPYTHONISTA\n")

# PYTHONIC
for _ in range(5):
    print("hello world2")


listku = [1, 2, 3, 4, 5]
a, b, *_ = listku
print(f"listku = {listku}\na = {a}\nb = {b}\n")

print()

listku = [100, 200, 300, 400, 500]
*_, a, b = listku
print(f"listku = {listku}\na = {a}\nb = {b}\n")
