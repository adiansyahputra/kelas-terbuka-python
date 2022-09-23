"""
Memotong (Slicing) List
Kita bisa mengakses anggota list dari range tertentu dengan menggunakan operator slicing titik dua ( : ). Slicing akan lebih mudah bila kita memahami indeks dengan baik. Perhatikan gambar berikut:

0   1   2   3   4   5   6   7   8   9
P   Y   T   H   O   N   I   N   D   O
-10 -9  -8  -7  -6  -5  -4  -3  -2  -1

"""

my_list = ["p", "y", "t", "h", "o", "n", "i", "n", "d", "o"]

# anggota list dari 3 s/d 5 (dari h s/d n)
print(my_list[3:6])

# anggota list dari 4 s/d yang terakhir
print(my_list[4:])

# anggota list dari 0 s/d 4
print(my_list[:5])

# indeks dari belakang dari -1 s/d -4
print(my_list[-1:-5])
