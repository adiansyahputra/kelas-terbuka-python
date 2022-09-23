# class

class mahasiswa():
    nama = "nama"  # ---> disebut atribut / yang menempel di class tersebut

    def belajar(self, kondisi):  # ----> # method --> fungsi yang menempel pada class
        print(self.nama, "sedang belajar", kondisi)

    def tidur(tidur, kondisi):
        print(tidur.nama, "sedang istirahat", kondisi)


# main programnya

otong = mahasiswa()
ucup = mahasiswa()

otong.nama = "otong surotong"
ucup.nama = "ucup surucup"

otong.belajar("dengan giat")
ucup.tidur("di depan laptopnya")
