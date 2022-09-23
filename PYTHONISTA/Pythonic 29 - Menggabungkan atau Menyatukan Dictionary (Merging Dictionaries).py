# cara tidak pythonic
data1 = {
    "nama": "kiki",
    "kelas": 9
}
data2 = {
    "umur": 20,
    "ipk": 2.90
}
mahasiswa = {}
for data in data1:
    mahasiswa[data] = data1[data]
for data in data2:
    mahasiswa[data] = data2[data]
print(f"data mahasiswa = {mahasiswa}")


print(f"\nPYTHONISTA\n")

# Pythonic
data1 = {
    "nama": "kiki",
    "kelas": 9
}
data2 = {
    "umur": 20,
    "ipk": 2.90
}
data3 = {
    "hobi": "makan",
    "sepatu": "ventela"
}
gabung = {**data1, **data2, **data3}
print(f"gabungan = {gabung}")
