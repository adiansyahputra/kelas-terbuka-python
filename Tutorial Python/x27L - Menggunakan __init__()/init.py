# class

class mahasiswa():

    def __init__(self, iniNama, nim):
        self.nama = iniNama
        self.nim = nim

    def belajar(self, kondisi):  # ----> # method --> fungsi yang menempel pada class
        print(self.nama, "sedang belajar", kondisi)

    def tidur(tidur, kondisi):
        print(tidur.nama, "sedang istirahat", kondisi)


# main programnya
otong = mahasiswa("Adiansyah Putra", 12121212)
print(otong.nama)
otong.nama = "lerry"
print(otong.nama)
print(otong.nim)
