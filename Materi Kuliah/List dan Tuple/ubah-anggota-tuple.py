"""
Mengubah Anggota Tuple
Setelah tuple dibuat, maka anggota tuple tidak bisa lagi diubah atau dihapus. Akan tetapi, bila anggota tuple-nya adalah tuple bersarang dengan anggota seperti list, maka item pada list tersebut dapat diubah. Jelasnya ada pada contoh berikut:

"""

my_tuple = (2, 3, 4, [5, 6])
# kita tidak bisa mengubah anggota tuple
# bila kita hilangkan tanda komentar # pada baris ke 6
# akan muncul error # TypeError: "tuple" object does not support item assignment

# my_tuple[1] = 8

# tapi list di dalam tuple bisa diubah
# output: (2, 3, 4, [7, 6])
my_tuple[3][0] = 7
print(my_tuple)

# tuple bisa diganti secara keseluruhan dengan penugasan kembali
# output: ("p", "y", "t", "h", "o", "n")
my_tuple = ("p", "y", "t", "h", "o", "n")
print(my_tuple)

# anggota tuple juga tidak bisa dihapus menggunakan del
# perintah berikut akan menghasilkan error TypeError
# kalau anda menghilangkan tanda komentar #

# del my_tuple[0]

# kita bisa menghapus tuple keseluruhan

del my_tuple
