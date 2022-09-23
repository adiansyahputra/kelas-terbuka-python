barang = ["kunci", "ember", "jaket", "ban", "mobil"]
print(barang)

# beberapa method yang bisa digunakan untuk memanipulasi list
# method untuk menambah data kedalam list
barang.append("sepeda")  # untuk menambah dibelakangnya
print(barang)

barang.extend("dompet")  # menambahkan dibelakangnya secara iterable
print(barang)

barang.insert(2, "lakban")  # menambahkan di posisi manapun
print(barang)

# method untuk menghitung anggota
jumlahSepeda = barang.count("sepeda")
print("jumlah sepeda :", jumlahSepeda)

# method untuk meremove data
barang.remove("sepeda")
print(barang)

# method untuk membalikkan data
barang.reverse()
print(barang)
print("+"*120)

# hati-hati untuk beginner
# stuff = barang ---> ini contoh yang salah
# yang benar begini dibawah
stuff = barang.copy()
stuff.append("gelas")
print(stuff)
print(barang)
