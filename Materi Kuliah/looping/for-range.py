"""
Fungsi range() dapat digunakan untuk menghasilkan deret bilangan. range(10) akan menghasilkan bilangan dari 0 sampai dengan 9 (10 bilangan). Kita juga bisa menentukan batas bawah, batas atas, dan interval dengan format range(batas bawah, batas atas, interval). Bila interval dikosongkan, maka nilai default 1 yang akan digunakan.

Fungsi range tidak menyimpan semua nilai dalam memori secara langsung. Ia hanya akan mengingat batas bawah, batas atas, dan interval dan membangkitkan hasilnya satu persatu hanya bila dipanggil. Untuk membuat fungsi ini langsung menampilkan semua item, kita bisa menggunakan fungsi list(). Untuk jelasnya perhatikan contoh berikut:

# Output: range(0,10)
print(range(10))
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10))
# Output: [2, 3, 4, 5, 6, 7]
print(list(range(2,8))
# Output: [2, 5, 8, 11, 14, 17]
print(list(range(2, 20, 3))
"""
# print(range(10))
# print(list(range(10)))
# print(list(range(2, 8)))
# print(list(range(2, 20, 3)))

"""
Kita bisa menggunakan fungsi range() dalam perulangan menggunakan for untuk iterasi bilangan berurut. Hal ini dengan cara mengkombinasikan fungsi range() dengan fungsi len(). Fungsi len() berfungsi untuk mendapatkan panjang atau jumlah elemen suatu data sekuensial atau berurut.
"""

# Program untuk iterasi list menggunakan pengindeksian

mapel = ["matematika", "fisika", "kimia"]

# iterasi list menggunakan indeks

for i in range(len(mapel)):
    print("saya suka ", mapel[i])
