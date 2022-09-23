"""
Argumen Fungsi
Kita bisa memanggil fungsi dengan menggunakan salah satu dari empat jenis argumen berikut:

1.  Argumen wajib (required argument)
Argumen wajib adalah argumen yang dilewatkan ke dalam fungsi dengan urutan posisi yang benar. Di sini, jumlah argumen pada saat pemanggilan fungsi harus sama persis dengan jumlah argumen pada pendefinisian fungsi. Pada contoh fungsi sapa() di atas, kita perlu melewatkan satu argumen ke dalam fungsi sapa(). Bila tidak, maka akan muncul error.
>>> sapa('Umar') 
Hi Umar. Apa kabar?
>>> # akan muncul error
>>> sapa()
Traceback (most recent call last):
File "<pyshell#5>", line 1, in <module>
sapa()
TypeError: sapa() missing 1 required positional argument: 'nama'

2.  Argumen kata kunci (keyword argument)
Argumen dengan kata kunci berkaitan dengan cara pemanggilan fungsi. Ketika menggunakan argumen dengan kata kunci, fungsi pemanggil menentukan argumen dari nama parameternya. Hal ini membuat kita bisa mengabaikan argumen atau menempatkannya dengan sembarang urutan. Python dapat menggunakan kata kunci yang disediakan untuk mencocokkan nilai sesuai dengan parameternya. Jelasnya ada pada contoh berikut:
"""

# definisi fungsi print_string


def print_string(str):
    """
    Menampilkan argumen string str ke Layar
    """
    print(str)


# Kita memanggil fungsi dengan kata kunci
print_string(str="Hello Python")

"""
Urutan parameter tidak menjadi masalah. Perhatikan contoh berikut:
"""

# Definisi fungsi


def print_info(nama, usia):
    """
    Fungsi ini menampilkan info yang dimasukkan
    """
    print("Nama: ", nama)
    print("Usia: ", usia)


# Memanggil fungsi
# output
# Nama: Budi
# Usia: 25
print_info(usia=25, nama="Budi")

"""
3.  Argumen default
Fungsi dengan argumen default menggunakan nilai default untuk argumen yang tidak diberikan nilainya pada saat pemanggilan fungsi. Pada contoh berikut, fungsi akan menampilkan usia default bila argumen usia tidak diberikan:
"""

# Definisi fungsi


def print_info(nama, usia=17):
    """
    Fungsi ini menampilkan info yang dimasukkan
    """
    print("Nama: ", nama)
    print("Usia ", usia)


# Memanggil fungsi print_info
print_info(usia=29, nama="Galih")

# Memanggil fungsi tidak menyediakan argumen usia
print_info(nama="Galih")

"""
Pada contoh di atas, pemanggilan fungsi kedua tidak menyediakan nilai untuk parameter usia, sehingga yang digunakan adalah nilai default yaitu 17.
"""
"""
4.  Argumen dengan panjang sembarang
Terkadang kita butuh untuk memproses fungsi yang memiliki banyak argumen. Nama – nama argumennya tidak disebutkan saat pendefinisian fungsi, beda halnya dengan fungsi dengan argumen wajib dan argumen default. Sintaksnya fungsi dengan argumen panjang sembarang adalah seperti berikut:
def function_name([formal_args,] *var_args_tuple):
    <---function_docstring--->
    statement(s)
    return [expression]
Tanda asterisk (*) ditempatkan sebelum nama variabel yang menyimpan nilai dari semua argumen yang tidak didefinisikan. Tuple ini akan kosong bila tidak ada argumen tambahan pada saat pemanggilan fungsi. Berikut adalah contohnya:
"""

# Definisi fungsi


def print_info(arg1, *vartuple):
    """
    Fungsi untuk menampilkan nilai argumen sembarang yang dilewatkan
    """
    print("Outputnya adalah: ")
    print(arg1)
    for var in vartuple:
        print(var)


# Pemanggilan fungsi
# Satu argumen
print_info(10)

# Empat argumen
print_info(10, 30, 50, 70)
