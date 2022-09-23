# cara tidak pythonic
def tambah(a, b):
    return a + b


def kali(c, d):
    return c * d


x, y = 10, 20
kondisi = False
if kondisi:
    hasil = tambah(x, y)
else:
    hasil = kali(x, y)
print(f"hasil = {hasil}")


print(f"\nPYTHONISTA\n")

# PYTHONIC


def kurang(p, q):
    return p - q


def bagi(b, c):
    return b / c


x, y = 20, 4
kondisi = True
hasil = kurang(x, y) if kondisi else bagi(x, y)
# hasil = (kurang if kondisi else bagi)(x, y)
print(f"hasil = {hasil}")
