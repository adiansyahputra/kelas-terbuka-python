# cara tidak pythonic
listku = [10, 20, 30, 40, 50]
cari = 52
ketemu = False
for item in listku:
    if cari == item:
        ketemu = True
        break
if ketemu:
    print(f"congrats ditemukan! angka = {cari}"),
else:
    print(f"maaf, tidak ditemukan")


print(f"\nPYTHONISTA\n")

# PYTHONIC
listku = [1, 2, 3, 4, 5]
cari = 9
if cari in listku:
    print(f"selamat angka {cari} ditemukan !")
else:
    print(f"maaf angka {cari} yang anda cari tidak ditemukan")
