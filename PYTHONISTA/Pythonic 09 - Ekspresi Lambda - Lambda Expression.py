def lipat_ganda(x):
    return x * 2


listku = [10, 20, 30]
listmu = list(map(lipat_ganda, listku))
print(f"listku = {listku}")
print(f"listmu = {listmu}")


print(f"\nPYTHONISTA\n")

# PYTHONIC
listku = [1, 2, 3]
listmu = list(map(lambda x: x * 3, listku))
print(f"listku = {listku}")
print(f"listmu = {listmu}")
