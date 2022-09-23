# scope variabel local

# namaKucing = "meong"


# def ubahNamaKucing(namaKucingBaru):
#     namaKucing = namaKucingBaru
#     print("saya rubah nama kucing menjadi", namaKucing)


# ubahNamaKucing("empus")
# print("nama kucing baru saya menjadi", namaKucing)

print("+"*128)

# scope variabel Global

namaKucing = "meong"
makananKucing = "royalCanin"


def ubahNamaKucing(namaKucingBaru):
    global namaKucing
    namaKucing = namaKucingBaru
    print("saya rubah nama kucing menjadi", namaKucing)


def kasihMakanKucing(makanan, nama):
    global namaKucing, makananKucing
    makananKucing = makanan
    namaKucing = nama


ubahNamaKucing("empus")
kasihMakanKucing(nama="geri", makanan="ikan asin")
print("nama kucing baru saya menjadi", namaKucing,
      "dan saya kasih makan", makananKucing)
