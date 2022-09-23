"""
Ruang Lingkup (Scope) Variabel
Di Python, tidak semua variabel bisa diakses dari semua tempat. Ini tergantung
dari tempat dimana kita mendefinisikan variabel. Ruang lingkup variabel ada dua, yaitu:
• Global
• Local
Variabel yang didefinisikan di dalam fungsi memiliki scope lokal, sedangkan
variabel yang didefinisikan di luar fungsi memiliki scope global. Ini berarti, variabel lokal hanya bisa diakses dari dalam fungsi di mana ia di definisikan, sedangkan variabel global bisa diakses dari seluruh tempat dimanapun di dalam program. Berikut adalah contohnya:
"""

total = 0
# Variable global
# Definisi fungsi


def sum(arg1, arg2):
    """
    Menambahkan variable dan mengembalikan hasilnya
    """
    total = arg1 + arg2
    # total disini adalah variable lokal
    print("Di dalam fungsi nilai total : ", total)
    return total


# Pemanggilan fungsi sum
sum(10, 20)
print("Di luar fungsi, nilai total : ", total)

"""
Perhatikan bagaimana variabel total di dalam dan di luar fungsi adalah dua variabel yang berbeda.
"""
