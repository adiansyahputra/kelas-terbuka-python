# membuat fungsi sederhana
def suaraayam():
    print("kukuruyuk")


def hargaayam():
    suaraayam()
    print("harga 1 kg ayam adalah Rp 20.000")


# membuat fungsi dengan input argumen
def hargaTotalAyam(kg):
    suaraayam()
    harga = 20000
    hargaTotal = kg * harga
    print("harga", kg, "kg ayam adalah", hargaTotal)


hargaTotalAyam(2)
hargaTotalAyam(3)
hargaTotalAyam(4)
hargaTotalAyam(5)
