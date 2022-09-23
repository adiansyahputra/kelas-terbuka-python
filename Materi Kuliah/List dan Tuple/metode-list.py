"""
Metode List

List memiliki banyak metode untuk operasi seperti menambahkan anggota, menghapus, menyisipkan, menyortir, dan lain sebagainya. Mereka bisa diakses menggunakan format list.metode().
----------------------------------------------------------------------------------

Menambahkan Anggota List

Fungsi append() berguna untuk menambahkan anggota ke dalam list. Selain itu, ada metode extend() untuk menambahkan anggota list ke dalam list.
>>> ganjil = [1,3,5,7]
>>> ganjil.append(9)
>>> print(ganjil)  [1,3,5,7,9]
>>> ganjil.extend([11,13,15])
>>> print(ganjil) [1,3,5,7,9,11,13,15]
Kita juga bisa menggunakan operator + untuk menggabungkan dua list, dan operator * untuk melipatgandakan list.
>>> genap = [2, 4, 6]
>>> print(genap + [8, 10, 12])
[2, 4, 6, 8, 10, 12]
>>> print(['p','y'] * 2)
['p','y','p','y]
-----------------------------------------------------------------------------------

Menyisipkan Anggota List

Fungsi insert() berfungsi untuk menyisipkan anggota list pada indeks tertentu. >>> ganjil = [5,7,11,13,15]
>>> # kita akan menyisipkan 9 setelah angka 7
>>> ganjil.insert(2,9)
>>> print(ganjil)  [5,7,9,11,13,15]
-----------------------------------------------------------------------------------

Menghapus Anggota List

Kita bisa menggunakan metode remove(), pop(), atau kata kunci del untuk menghapus anggota list. Selain itu kita bisa menggunakan clear() untuk mengosongkan list. Fungsi pop() selain menghapus anggota list, juga mengembalikan nilai indeks anggota tersebut. Hal ini berguna bila kita ingin memanfaatkan indeks dari anggota yang terhapus untuk digunakan kemudian.
-----------------------------------------------------------------------------------

Mengurutkan anggota List

Pada saat kita perlu mengurutkan atau menyortir anggota list, kita bisa menggunakan metode sort(). Untuk membalik dengan urutan sebaliknya bisa dengan menggunakan argumen reverse=True.
>>> alfabet = ['a','b','d','f','e','c','h','g','j','i'] 
>>> alfabet.sort()
>>> print(alfabet)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 
>>> alfabet.sort(reverse=True)
>>> print(alfabet)
['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
-----------------------------------------------------------------------------------

Membalik Urutan List

Selain mengurutkan, kita juga bisa membalikkan urutan list dengan menggunakan metode reverse().
>>> alfabet = ['a','c','d','e','b']
>>> alfabet.reverse()
>>> print(alfabet)  ['b', 'e', 'd', 'c', 'a']

"""
