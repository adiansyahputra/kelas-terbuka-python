"""
String adalah tipe data yang paling sering digunakan di Python. Kita bisa membuat string dengan meletakkan karakter di dalam tanda kutip. Tanda kutipnya bisa kutip tunggal maupun kutip ganda. Contohnya adalah sebagai berikut:

var1 = 'Hello Python'
var2 = 'Programming with Python'

>>> Mengakses Nilai String

Untuk mengakses nilai atau substring dari string, kita menggunakan indeks dalam tanda [ ].
var1 = 'Hello Python!'
print("var1[0]", var1[0]) 
var2 = "I love Python" 
print("var2[2:6]:",var2[2:6])

>>> Mengupdate String

String adalah tipe data immutable, artinya tidak bisa diubah. Untuk mengupdate string, kita perlu memberikan nilai variabel string lama ke string yang baru. Nilai yang baru adalah nilai string lama yang sudah diupdate.
var1 = 'Hello Python!'
var2 = var1[:6]
print("String Update: - ", var1[:6] + 'World')

>>> Menggabung String

Kita bisa menggabungkan dua atau lebih string menjadi satu dengan menggunakan operator +. Selain itu kita juga bisa melipatgandakan string menggunakan operator *.
"""

str1 = "Hello"
str2 = "Python"

# menggunakan +
print("str1 + str2 = ", str1 + str2)

# menggunakan *
print("str1 * 3 =", str1 * 3)

"""
Mengetahui Panjang String
Untuk mengetahui panjang dari string, kita bisa menggunakan fungsi len(). >>> string = 'I love Python'
>>> len(string)
18
"""

string = "i love you"
print(len(string))
