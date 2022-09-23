"""
for var in sequence:
    body of for

var adalah variabel yang digunakan untuk penampung sementara nilai dari sequence pada saat terjadi perulangan. Sequence adalah tipe data berurut seperti string, list, dan tuple.

Perulangan terjadi sampai looping mencapai elemen atau anggota terakhir dari sequence. Bila loop sudah sampai ke elemen terakhir dari sequence, maka program akan keluar dari looping.
"""

# Program untuk menemukan jumlah bilangan dalam satu list

# list number
numbers = [7, 5, 9, 8, 9, 0, 8, 4, 0]

# variable untuk menyimpan jumlah

sum = 0

# iterasi
for each in numbers:
    sum += each

# output: jumlah semuanya: 50
print("Jumlah Semuanya :", sum)
