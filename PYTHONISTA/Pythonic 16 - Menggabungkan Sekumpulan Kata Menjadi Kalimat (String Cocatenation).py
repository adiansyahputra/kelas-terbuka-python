# cara tidak pythonic
from typing import List


listku = ["belajar", "pemrograman", "python"]
kalimat = ""
for kata in listku:
    kalimat += kata + " "

print(f"listku = {listku}")
print(f"kalimat = {kalimat}")


print(f"\nPYTHONISTA\n")

# PYTHONIC
listku = ["belajar", "pemrograman", "python"]
kalimat = " ".join(listku)
print(f"listku = {listku}")
print(f"kalimat = {kalimat}")

listku = ["belajar", "pemrograman", "python"]
kalimat = " === ".join(listku)
print(f"listku = {listku}")
print(f"kalimat = {kalimat}")
