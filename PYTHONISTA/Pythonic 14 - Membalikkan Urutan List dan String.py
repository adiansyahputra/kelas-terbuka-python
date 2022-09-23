# cara tidak pythonic
listku = [10, 20, 30, 40, 50, 60]
listmu = []
for i in range(len(listku)):
    reverseD = len(listku) - 1 - i
    listmu.append(listku[reverseD])

print(f"listku = {listku}")
print(f"listmu = {listmu}")


print(f"\nPYTHONISTA\n")

# PYTHONIC
listku = [100, 200, 300, 400, 500, 600]
listmu = listku[::-1]
print(f"listku = {listku}")
print(f"listmu = {listmu}")

kata = "BELAJAR"
print(kata[::-1])
