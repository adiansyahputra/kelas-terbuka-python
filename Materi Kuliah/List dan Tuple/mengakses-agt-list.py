"""

List dibuat dengan menempatkan semua item di dalam tanda kurung [ ], dipisahkan oleh tanda koma. Anggota list bisa berisi satu tipe data, atau campuran.

# list kosong
my_list = []
# list berisi integer my_list = [1,2,3,4,5]
# list berisi tipe campuran my_list = [1, 3.5, "Hello"]

List juga bisa berisi list lain. Ini disebut list bersarang
# list bersarang
my_list = ["hello", [2,4,6], ['a','b']]

"""

"""
Mengakses anggota List
Kita bisa mengakses anggota list dengan menggunakan indeksnya dengan format namalist[indeks]. Indeks list dimulai dari 0. List yang memiliki 5 anggota akan memiliki indeks mulai dari 0 s/d 4. Mencoba mengakses anggota list di luar itu akan menyebabkan error IndexError.
"""

my_list = ["I", "love", "python", "programming", 2017]
# output: I
print((my_list[0]))

# output: python
print((my_list[2]))

# list dalam list
your_list = ["hello", [1, 2, 3], "python"]

# output 1
print(your_list[1][0])

# output3
print(your_list[1][2])

# IndexError
my_list[6]
