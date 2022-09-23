# cara tidak pythonic
def fungsiku():
    nim = "011"
    nama = "roger"
    kelas = 211
    hasil = (nim, nama, kelas)
    return hasil


ygmauguaprint = fungsiku()
print(f"hasil 1 = {ygmauguaprint[0]}")
print(f"hasil 2 = {ygmauguaprint[1]}")
print(f"hasil 2 = {ygmauguaprint[2]}")


print(f"\nPYTHONISTA\n")

# PYTHONISTA


def fungsiku():
    nim = "001"
    nama = "steve"
    kelas = 999
    gabung = nim, nama, kelas
    return gabung


a, b, c = fungsiku()
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
