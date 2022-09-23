# operator dalam bentuk methods

# merubah case dari string

# merubah semua ke upper case
salam = "brooooo"
print("normal : " + salam)
salam = salam.upper()
print("upper : " + salam)

# merubah semua ke lower case
alay = "aKu KeCCee AAbbieeszzzZ"
print("normal : " + alay)
alay = alay.lower()
print("lower : " + alay)

# pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower()  # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()  # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <---- untuk mengecek apakah semuanya huruf
# isalnum <---- untuk mengecek apakah huruf dan angka
# isdecimal() <---- untuk mengecek apakah angka
# istittle() <---- untuk mengecek apakah tiap kata diawali huruf besar
# isspace() <---- untuk mengecek apakah ada spasi, tab, newline \n

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()  # hasilnya bool
print(judul + " is tittle = " + str(cek_judul))

huruf = " ini semua adalah huruf loh wkwkwk"
cek_huruf = huruf.isalpha()  # hasilnya bool
print(huruf + " is alpha = " + str(cek_huruf))

angka = " ini semua adalah angka loh wkwkwk"
cek_angka = angka.isdecimal()  # hasilnya bool
print(angka + " is alpha = " + str(cek_angka))

huruf_angka = " ini semua adalah huruf_angka loh wkwkwk"
cek_huruf_angka = huruf_angka.isalnum()  # hasilnya bool
print(huruf_angka + " is alpha = " + str(cek_huruf_angka))

space = " \n ini semua \t adalah space loh wkwkwk"
cek_space = space.isspace()  # hasilnya bool
print(space + " is alpha = " + str(cek_space))

# ngecek komponen startswith() endswith() <-- keren
cek_start = "adiansyah putra".startswith("adiansyah")
print("cek start = " + str(cek_start))

cek_end = "adiansyah putra".endswith("poetra")
print("cek end = " + str(cek_end))

# penggabungan komponen join() split()
pisah = ["adi", "ansyah", "putra"]
gabungan = ','. join(pisah)
print(pisah)
print(gabungan)

gabungan = " ".join(pisah)
print(gabungan)

gabungan = "sunnyehmgo"
print(gabungan.split("ehm"))

# alokasi karakter rjust() ljust() center()

kanan = "kanan"
print("'" + kanan.rjust(10) + "'")

kiri = "kiri".ljust(15)
print("'" + kiri + "'")

tengah = "tengah".center(20, "=")
print("'" + tengah + "'")

# kebalikannya strip()

tengah = "tengah".strip("=")  # menghilangkan tanda =
print("'" + tengah + "'")

# capitalize() = Mengubah Kata yang huruf depannya lowercase jadi uppercase

text = 'kelas terbuka'.capitalize()
print(text)
