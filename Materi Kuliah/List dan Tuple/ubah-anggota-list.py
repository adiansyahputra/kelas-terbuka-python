"""
Mengubah Anggota List
List adalah tipe data yang bersifat mutable, artinya anggotanya bisa diubah. Ini berbeda dengan string dan tuple yang bersifat immutable.
"""

# misal ada nilai yang salah
ganjil = [1, 3, 4, 7, 9]

# ubah item ke 3 (indeks ke 2)
ganjil[2] = 5
print(ganjil)

# mengubah sekali banyak
ganjil[2:5] = [11, 13, 15]
print(ganjil)
