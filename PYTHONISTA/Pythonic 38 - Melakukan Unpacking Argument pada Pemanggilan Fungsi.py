# cara tidak Pythonic
def perkalian(a, b):
    return a * b


listku = [10, 20]
dictksi = {
    "satu": 20,
    "dua": 20
}
hasilList = perkalian(a=listku[1], b=listku[0])
print(f"hasil dari list: {hasilList}")
hasilDict = perkalian(a=dictksi["satu"], b=dictksi["dua"])
print(f"hasil dari dictku: {hasilDict}")


print(f"\nPYTHONISTA\n")

# Pythonic


def pembagian(a, b):
    return a / b


list1 = [10, 20]
dic1 = {
    "a": 400,  # -->kenapa a, karna harus sama dengan argumen input fungsi
    "b": 20  # -->kenapa b, karna harus sama dengan argumen input fungsi
}
hasilList = pembagian(*list1)
print(f"hasil dari list: {hasilList}")
hasilDict = pembagian(**dic1)
print(f"hasil dari dictku: {hasilDict}")
