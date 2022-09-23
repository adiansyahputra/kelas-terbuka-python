# cara tidak pythonic
listku = []
for i in range(1, 51):
    listku.append(i)
print(f"listku = {listku}")


print(f"\nPYTHONISTA\n")

# PYTHONIC
listku = [i for i in range(2, 52)]
print(f'listku = {listku}')
