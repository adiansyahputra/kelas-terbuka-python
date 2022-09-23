# self itu mengikat kepada instance
# class

class mahasiswa():

    jumlah_mahasiswa = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim
        mahasiswa.jumlah_mahasiswa += 1

# main programmnya / instance


adi = mahasiswa("adiansyah putra", 12021001)
radit = mahasiswa("raditya hapusan", 12012919)

print(mahasiswa.jumlah_mahasiswa)
