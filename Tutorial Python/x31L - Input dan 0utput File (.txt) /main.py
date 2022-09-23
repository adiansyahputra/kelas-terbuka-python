# input output file

# variable = open("nama file", "modenya")

# membuat file txt

"""
mode nya nehh
w = write mode / mode menulis file atau menghapus file lama / jika file tidak ada maka file akan dibuat baru
r = read mode only / hanya bisa baca
a = appending mode / menambahkan data di akhir baris
r+ = read and write mode
"""

file = open("data.txt", "w")

file.write("ini adalah write mode test1")
file.write("\nini adalah baris keduanyaa")
file.write("\nini adalah baris ketiganyaa")

file.close()

file2 = open("data.txt", "r")

# print(file2.read())
# print(file2.read(10))
# print(file2.readline())
# print(file2.readline())
# print(file2.readline())

file2.close()

file3 = open("data.txt", "a")

file3.write("\nini tambahan dari mode appending hehe")
file3.write("\nini tambahan dari mode appending hehe")

file3.close()

# ----> kayanya belum working bray sorry about that
file4 = open("data.txt", "r+")

print(file4.read())
