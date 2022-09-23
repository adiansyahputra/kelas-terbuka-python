"""
Tuple
Tuple mirip dengan list. Bedanya, tuple bersifat immutable, sehingga anggotanya tidak bisa diubah. Kalau mirip, mengapa harus menggunakan tuple?
Kita menggunakan tuple tergantung kebutuhan. Untuk beberapa hal, tuple memiliki kelebihan sebagai berikut:
>>> Karena tuple adalah immutable, maka iterasi pada tuple lebih cepat dibandingkan list.
>>> Tuple bisa berisi anggota yang immutable yang dapat digunakan sebagai key untuk dictionary. List tidak bisa dipakai untuk itu.
>>> Kalau kita memerlukan data yang memang tidak untuk diubah, maka
menggunakan tuple bisa menjamin bahwa data tersebut akan write-protected. 
-----------------------------------------------------------------------------------

Membuat Tuple
Tuple dibuat dengan meletakkan semua anggota di dalam tanda kurung ( ), masing- masing dipisahkan oleh tanda koma. Menggunakan tanda kurung sebenarnya hanya opsional, tapi kita sebaiknya tetap menggunakannya untuk kemudahan pembacaan kode. Tuple dapat berisi tipe data yang sama maupun campuran.
"""

# membuat tuple kosong
my_tuple = ()
print(my_tuple)

# tuple dengan 1 elemen
# output: (1,)
my_tuple = (1,)
print(my_tuple)

# tuple berisi integer
# output = (1, 2, 3)
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple bersarang
# output: ("hello", [1, 2, 3], (4, 5, 6))
my_tuple = ("hello", [1, 2, 3], (4, 5, 6))
print(my_tuple)

# tuple bisa tidak menggunakan tanda ()
# output (1,2,3)
my_tuple = 1, 2, 3

# memasukkan anggota tuple ke variable yang bersesuaian
# a akan berisi 1, b berisi 2, dan c berisi 3
# output 1 2 3
a, b, c = my_tuple
print(a, b, c)
