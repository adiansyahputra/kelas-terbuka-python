"""
Pada saat menulis dan menjalankan program, kita sering dihadapkan pada munculnya kesalahan atau error. Seringkali error menyebabkan program berhenti sendiri.
Error dapat terjadi akibat kesalahan struktur (sintaks) program. Hal ini disebut syntax error. Contohnya adalah seperti berikut:
>>> if x < 5
File "<stdin>", line 1
    if x < 5
SyntaxError: invalid syntax
Kita bisa melihat bahwa penyebabnya adalah lupa titik dua pada pernyataan if.

Error juga dapat terjadi pada saat runtime (saat program berjalan). Error seperti ini disebut eksepsi. Misalnya, bila kita membuka file yang tidak ada, maka akan muncul pesan kesalahan FileNotFoundError. Bila kita membagi bilangan dengan nol akan muncul ZeroDivisionError, dan lain sebagainya.
Pada saat terjadi eksepsi, Python akan menampilkan traceback dan detail dimana kesalahan terjadi.
>>> 1/0
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

"""
"""
Daftar Eksepsi Built-in Python

Eksepsi                               Penyebab Error
AssertionError     -------->       Muncul pada saat pernyataan assert gagal 

AttributeError     -------->       Muncul pada saat penugasan terhadap attribute atau referensi gagal

EOFError           -------->       Muncul saat fungsiinput()mendapatkan kondisi akhir file (end- of-file)

FloatingPointError     -------->       Muncul saat operasi terhadap bilangan float gagal

GeneratorExit     -------->       Muncul saat metode close() generator dipanggil

ImportError     -------->       Muncul saat modul yang hendak diimpor tidak ditemukan

IndexError     -------->       Muncul saat indeks dari sequence berada di luar range

KeyError     -------->       Muncul saat suatu key tidak ditemukan di dalam dictionary

KeyboardInterrupt     -------->       Muncul saat user menekan tombol interupsi (Ctrl + C)

MemoryError     -------->       Muncul saat operasi kehabisan memori

NameError     -------->       Muncul saat variabel tidak ditemukan

NotImplementedError     -------->       Muncul oleh metode abstrak

OSError     -------->       Muncul saat sistem operasi bersangkutan mengalami error

OverflowError     -------->       Muncul saat hasil operasi perhitungan terlalu besar untuk direpresentasikan

ReferenceError     -------->       Muncul saat weak reference digunakan untuk mengakses referensi sampah program

RuntimeError     -------->       Muncul saat error yang terjadi di luar semua kategori eksepsi lain

StopIteration     -------->       Muncul oleh fungsinext()untuk menunjukkan bahwa tidak ada lagi item yang tersisa pada iterator

SyntaxError     -------->       Muncul oleh parser saat terjadi kesalahan sintaks

IndentationError     -------->       Muncul saat ada indentasi yang salah

TabError     -------->       Muncul saat indentasi memiliki jumlah spasi atau tab yang tidak konsisten

SystemError     -------->       Muncul saat interpreter mendeteksi kesalahan internal

SystemExit     -------->       Muncul oleh fungsi sys.exit()

TypeError     -------->       Muncul saat melakukan operasi pada tipe data yang tidak sesuai

UnboundLocalError     -------->       Muncul saat referensi dibuat untuk variabel lokal dari fungsi, tapi tidak ada nilainya.

UnicodeError     -------->       Muncul saat terjadi kesalahan berkenaan dengan encoding dan decoding unicode

UnicodeEncodeError     -------->       Muncul saat terjadi kesalahan pada proses encoding

UnicodeDecodeError     -------->       Muncul saat terjadi kesalahan pada proses decoding

UnicodeTranslateError     -------->       Muncul saat terjadi kesalahan berkenaan dengan penerjemahan unicode

ValueError     -------->       Muncul saat fungsi menerima argumen yang tipe datanya salah

ZeroDivisionError     -------->       Muncul saat terjadi operasi pembagian bilangan dengan nol
"""
