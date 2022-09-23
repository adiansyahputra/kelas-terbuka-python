"""
Mengakses anggota Tuple
Seperti halnya list, kita bisa mengakses anggota tuple lewat indeksnya menggunakan format namatuple[indeks]. Indeks dimulai dari 0 untuk anggota pertama. Selain itu, indeks negatif juga bisa dipakai mulai dari -1 untuk anggota terakhir tuple.
"""

my_tuple = ("p", "y", "t", "h", "o", "n")
# output: "p"
print(my_tuple[0])

# output: "y"
print(my_tuple[1])

# output: "n"
print(my_tuple[-1])

# output: "o"
print(my_tuple[-2])

# indexError
# print(my_tuple[6])

"""
Sama seperti list, kita bisa mengakses satu range anggota tuple dengan menggunakan operator titik dua ( : ).
"""

my_tuple = ("p", "r", "o", "g", "r", "a", "m", "i", "n", "g")
# akses dari indeks 0 s/d 2

# output: ("p", "r", "o")
print(my_tuple[:3])

# akses dari indeks 2 s/d 5
print(my_tuple[2:6])

# akses dari indeks 3 sampai akhir
print(my_tuple[3:])
