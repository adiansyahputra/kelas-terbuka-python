# cara tidak pythonic
siswa = [("191", "budi", 3.20), ("192", "setyo", 2.35), ("193", "riko", 2.10)]
nim = []
nama = []
ipk = []

for item in siswa:
    nim.append(item[0])
    nama.append(item[1])
    ipk.append(item[2])

print(f"nim = {nim}")
print(f"nama = {nama}")
print(f"ipk = {ipk}")


print(f"\nPYTHONISTA\n")

# PYTHONIC
siswa = [("191", "budi", 3.20), ("192", "setyo", 2.35), ("193", "riko", 2.10)]
nim, nama, ipk = zip(*siswa)

print(f"nim = {nim}")
print(f"nama = {nama}")
print(f"ipk = {ipk}")
