# cara tidak pythonic
listku = [10, 20, 30, 20, 30, 10, 40, 20, 40, 30, 30]
hitung = 30
jumlah = 0
for item in listku:
    if item == hitung:
        jumlah += 1
print(f"banyak {hitung} di dalam {listku} adalah {jumlah}")


print(f"\nPYTHONISTA\n")

# Pythonic
listku = [10, 20, 30, 20, 30, 10, 40, 20, 40, 30, 30]
hitung = 20
jumlah = listku.count(hitung)
print(f"banyak {hitung} di dalam {listku} adalah {jumlah}")
