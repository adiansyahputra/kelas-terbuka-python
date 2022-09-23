# cara tidak pythonic
mahasiswa = ["regref osinsin", "kuripqlo poreisj", "meoolps loqqpa"]
print(f"sebelum = {mahasiswa}")
for i in range(len(mahasiswa) - 1):
    for j in range(i + 1, len(mahasiswa)):
        if mahasiswa[i].split()[-1] > mahasiswa[j].split()[-1]:
            mahasiswa[i], mahasiswa[j] = mahasiswa[j], mahasiswa[i]
print(f"sesudah = {mahasiswa}")


print(f"\nPYTHONISTA\n")

# Pythonic


def customKey(nama):
    return nama.split()[-1]


mahasiswa = ["regref osinsin", "kuripqlo poreisj", "meoolps loqqpa"]
print(f"pythonista sebelum = {mahasiswa}")
sesudah = sorted(mahasiswa, key=customKey)
print(f"pythonista sesudah = {sesudah}")
