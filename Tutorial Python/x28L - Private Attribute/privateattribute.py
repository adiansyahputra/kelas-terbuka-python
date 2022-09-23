# private = __

# class

class mahasiswa():

    jurusan = "teknik tata boga"
    __nilai = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim

    def uts(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def checkStatus(self):
        if self.__nilai <= 50:
            print(self.nama, "maaf anda tidak lulus")
        else:
            print(self.nama, "selamat anda lulus")

# main programmnya


adi = mahasiswa("adiansyah putra", 120210120)
radit = mahasiswa("raditya hapusan", 12012019)

adi.uts(50)
adi.uas(30)

radit.uts(20)
radit.uas(20)

adi.checkStatus()
radit.checkStatus()
