"""
Mengatur Format String
Ada dua cara melakukan format pada string. Pertama dengan menggunakan fungsi format(), dan kedua dengan menggunakan cara lama (menggunakan %).

Metode format()
Memformat string dengan fungsi format() dibuat dengan menggunakan tanda {} sebagai placeholder atau posisi substring yang akan digantikan. Kita biasa menggunakan argumen posisi atau kata kunci untuk menunjukkan urutan dari substring.
"""

# menggunakan posisi default
defaul_order = "{}, {} dan {}".format("Budi", "Galih", "Ratna")
print("\n--- Urutan Default ---")
print(defaul_order)

# menggunakan argument posisi
positional_order = "{1}, {0}, dan {2}".format("Budi", "Galih", "Ratna")
print("\n--- Urutan berdasarkan posisi ---")
print(positional_order)

"""
Metode format() dapat memiliki spesifikasi format opsional. Misalnya, kita bisa menggunakan tanda < untuk rata kiri, > untuk rata kanan, ^ untuk rata tengah, dan sebagainya.

>>> # format integer
>>> "{0} bila diubah jadi biner menjadi {0:b}".format(12) 
'12 bila diubah jadi biner menjadi 1100'

>>> # format float
>>> "Format eksponensial: {0:e}".format(1566.345) 
'Format eksponensial: 1566345e+03'

>>> # pembulatan
>>> "Sepertiga sama dengan: {0:3f}".format(1/3) 
'Sepertiga sama dengan: 0.333'

>>> # Meratakan string
>>> "|{:<10}|{:^10}|{:>10}|".format('beras', 'gula', 'garam') 
'|beras | gula | garam|'
Format cara lama dengan %

Kita bisa menggunakan operator % untuk melakukan format string.
>>> nama = 'Budi'
>>> print('Nama saya %s' %nama)
Nama saya Budi

>>> x = 12.3456789
>>> print('Nilai x = %3.2f' %x) Nilai x = 12.35
>>> print('Nilai x = %3.4f' %x) Nilai x = 12.3456
"""
print("{0} bila diubah jadi biner menjadi {0:b}".format(12))
print("Format eksponensial: {0:e}".format(1566.345))
print("Sepertiga sama dengan: {0:3f}".format(1/3))
print("|{:<10}|{:^10}|{:>10}|".format("beras", "gula", "garam"))

nama = "budi"
print("Nama saya %s" % nama)

x = 12.3456789
print("Nilai x = %3.2f" % x)
print("Nilai x = %3.4f" % x)
