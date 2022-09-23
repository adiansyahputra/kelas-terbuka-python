class Ojek():

    def __init__(self, input_nama, input_jenis_motor, input_lokasi):
        self.nama = input_nama
        self.motor = input_jenis_motor
        self.lokasi = input_lokasi

    def cetak_identitas(self):
        print("nama driver :", self.nama, "\njenis motor :",
              self.motor, "\nlokasi :", self.lokasi)


class Gojek(Ojek):
    pass

# instance / main programnya


ojek1 = Ojek("poli", "matic", "jaktim")
ojek2 = Gojek("gengeng", "gigi", "serang")

ojek1.cetak_identitas()
ojek2.cetak_identitas()
