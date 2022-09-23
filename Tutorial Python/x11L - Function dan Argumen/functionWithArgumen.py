# fungsi dengan menggunakan argumen sederhana
def siswa(nama):
    print("siswa bernama :", nama)


siswa("adi")

# fungsi dengan menggunakan keywords arguments


def guru(nama, pelajaran):
    print("guru ini bernama :", nama)
    print("guru ini mengajar :", pelajaran)


guru(nama="Adiansyah Putra", pelajaran="Pemrograman")
guru(pelajaran="Olah Raga", nama="sitin")
guru("senirupa", "laeli")  # ini contoh yang salah

# fungsi dengan menggunakan default arguments


def penjagaSekolah(nama, shift="siang", galak="tidak"):
    print("penjaga sekolah ini bernama :", nama)
    print("shift :", shift)
    print("galak ?: ", galak)
