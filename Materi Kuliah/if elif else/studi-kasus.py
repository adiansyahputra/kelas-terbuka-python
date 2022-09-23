"""
Latihan

Studi Kasus : Penjualan Tiket
Perusahaan XYZ bergerak dibidang penjualan tiket bus dengan detail tiket sebagai berikut :
1. setiap transaksi perlu menginput data pembeli seperti Nama Pembeli, jumlah tiket yang akan dibeli, no_Hp, dan memilih jurusan sesuai kategori yang diinginkan.
2. Potongan 10% didapat jika jumlah beli >= 3.
3. Totalharga=(jumlahbeli*harga)-potongan. Data harga tiket sebagai berikut :
Kodejurusan Nama Kota
SBY surabaya BL Bali LMP lampung
Harga
300,000 350,000 500,000
"""

# Input
print("=" * 40)
print(14 * "-" + " " + "Harga Tiket" + " " + "-"*13)
print("=" * 40)
print("Kode Jurusan\t Nama Kota\t Harga")
print("SBY         \t Surabaya \t 300.000")
print("Bl          \t Bali     \t 350.000")
print("LMP         \t Lampung  \t 500.000")

print("=" * 40)

namaPembeli = input("Masukkan Nama Pembeli : ")
noHandphone = int(input("Masukkan No. Handphone : "))
jurusan = input("Pilih Jurusan [ SBY/BL/LMP ] : ")
jumlahBeliTiket = int(input("Masukkan Jumlah Beli Tiket : "))

if jurusan == "SBY" or "sby":
    namaKota = "Surabaya"
    harga = 300000
elif jurusan == "BL" or "bl":
    namaKota = "Bali"
    harga = 350000
else:
    jurusan == "LMP" or "lmp"
    namaKota = "Lampung"
    harga = 500000

diskon = 0.1 * harga * jumlahBeliTiket

if jumlahBeliTiket >= 3:
    potonganDidapat = diskon
else:
    jumlahBeliTiket < 3
    potonganDidapat = 0

totalBayar = harga * jumlahBeliTiket - diskon

# Output
print("\n")
print("-" * 40)
print(" " * 10 + "PENJUALAN TIKET BUS" + " " * 11)
print(" " * 18 + "XYZ" + " " * 19)
print("-" * 40)
print("Nama Pembeli  : " + str(namaPembeli))
print("No. Handphone :", noHandphone)
print("Kode Jurusan yang dipilih : " + str(jurusan))
print("Harga         : ", harga)
print("Jumlah Beli   : ", jumlahBeliTiket)
print("-" * 40)
print("Potongan yang didapat : ", potonganDidapat)
print("Total Bayar  : ", totalBayar)
uangBayar = int(input("Masukkan Uang Bayar : "))
uangKembali = uangBayar - totalBayar
print("Uang kembali : ", uangKembali)
