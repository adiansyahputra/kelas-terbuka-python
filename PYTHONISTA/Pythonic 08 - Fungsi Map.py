# cara tidak pythonic
def lipat_ganda(x):
    return x * 2


listku = [10, 20, 30]
listmu = []

for item in listku:
    listmu.append(lipat_ganda(item))

print(f"listku = {listku}")
print(f"listmu = {listmu}")


print(f"\nPYTHONISTA\n")

# PYTHONIC


def lipat_ganda(x):
    return x * 2


listku = [1, 2, 3]
listmu = list(map(lipat_ganda, listku))
print(f"listku = {listku}\nlistmu = {listmu}")
