# cara tidak pythonic
nama = ["putri", "funny", "elspo"]
nim = [100, 101, 102]
ipk = [2.35, 2.55, 2.30]
gabung = []

for i in range(len(nama)):
    gabung.append((nama[i], nim[i], ipk[i]))

print(f"gabung = {gabung}")


print(f"\nPYTHONISTA\n")

# Pythonic
nama = ["putri", "funny", "elspo"]
nim = [100, 101, 102]
ipk = [2.35, 2.55, 2.30]
join = list(zip(nama, nim, ipk))

print(f"join = {join}")
