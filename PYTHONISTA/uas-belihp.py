def garis():
    print(90*'-')


print("\tTOKO HP BERKAH JAYA ")
print("****************")
print("Kode  Merk                    Harga   ")
print("01    OPPO F11 4/128GB        Rp. 2.649.000")
print("02    OPPO RENO 3             Rp. 2.799.000")
print("03    OPPO RENO 4             Rp. 4.999.000")
print("04    OPPO RENO 4F            Rp. 3.599.000")
print("05    OPPO F9                 Rp. 1.700.000")
print("06    XIAOMI NOTE 7           Rp. 2.300.000")
print("07    XIAOMI NOTE 8 6/128     Rp. 2.700.000")
print("08    XIAOMI NOTE 7 PRO       Rp. 3.000.000")
print("09    XIAOMI NOTE 8 PRO       Rp. 3.500.000")
print("10    XIAOMI REDMI NOTE 9     Rp. 3.700.000")
print("11    IPHONE 11               Rp. 12.000.000")
print("12    IPHONE 11 PRO 256GB     Rp. 16.800.000")
print("13    IPHONE 11 PRO MAX       Rp. 18.000.000")
print("14    IPHONE 12  128 GB       Rp. 17.999.000")
print("15    IPHONE 12 PRO MAX 256   Rp. 20.000.000")
print("****************")
print("\n")

# batas perulangan
banyak = int(input("Banyak Data : "))

# perulangan input
listkode = []
listjumlah = []
for i in range(banyak):
    print("\nData ke-", i+1)
    kode = input("Kode HP [01/02/03/04/05/06/07/08/09/10/11/12/13/14/15]  : ")
    listkode.append(kode)
    jumlah = int(input("Jumlah Beli : "))
    listjumlah.append(jumlah)
# outputjudul
print("\n\n")
print("\t\tTOKO HP BERKAH JAYA")
garis()
print("No    Merk      Harga      Jumlah   Subtotal")
garis()
# proses operasi
total_beli = 0
for i in range(banyak):
    # fungsi if
    if listkode[i] == '01' or listkode[i] == '01':
        merk = "OPPO F11 4/128GB "
        harga = 2649000
    elif listkode[i] == '02' or listkode[i] == '02':
        merk = "OPPO RENO 3"
        harga = 2799000
    elif listkode[i] == '03' or listkode[i] == '03':
        merk = "OPPO RENO 4"
        harga = 4999000
    elif listkode[i] == '04' or listkode[i] == '04':
        merk = "OPPO RENO 4F"
        harga = 3599000
    elif listkode[i] == '05' or listkode[i] == '05':
        merk = "OPPO F9"
        harga = 1700000
    elif listkode[i] == '06' or listkode[i] == '06':
        merk = "XIAOMI NOTE 7"
        harga = 2300000
    elif listkode[i] == '07' or listkode[i] == '07':
        merk = "XIAOMI NOTE 8 6/128"
        harga = 2700000
    elif listkode[i] == '08' or listkode[i] == '08':
        merk = "XIAOMI NOTE 7 PRO"
        harga = 3000000
    elif listkode[i] == '09' or listkode[i] == '09':
        merk = "XIAOMI NOTE 8 PRO"
        harga = 3500000
    elif listkode[i] == '10' or listkode[i] == '10':
        merk = " XIAOMI REDMI NOTE 9"
        harga = 3700000
    elif listkode[i] == '11' or listkode[i] == '11':
        merk = "IPHONE 11    "
        harga = 1200000
    elif listkode[i] == '12' or listkode[i] == '12':
        merk = "IPHONE 11 PRO 256GB"
        harga = 16800000
    elif listkode[i] == '13' or listkode[i] == '13':
        merk = " IPHONE 11 PRO MAX"
        harga = 18000000
    elif listkode[i] == '14' or listkode[i] == '14':
        merk = "IPHONE 12  128 GB "
        harga = 17999000
    elif listkode[i] == '15' or listkode[i] == '15':
        merk = "IPHONE 12 PRO MAX 256"
        harga = 200000001
    else:
        merk = "-"
        harga = 0

    # subtotal
    subtotal = harga*listjumlah[i]
    # SUM subtotal (menjumlahkan subtotal sesuai dengan perulangan)
    total_beli = total_beli+subtotal
    # PPN 5% daru total beli
    ppn = total_beli*0.05
    # total bayar dari total beli + ppn
    total_bayar = total_beli+ppn

    print(i + 1, "    ", merk, "    ", harga, "    ",
          listjumlah[i], "   ", format(subtotal, ',d').replace(',', '.'))
garis()
print("                  Total Pembelian    Rp.",
      format(total_beli, ',d').replace(',', '.'))
print("                  Ppn                Rp.",
      format(round(ppn), ',d').replace(',', '.'))
print("                  Total Bayar        Rp.",
      format(round(total_bayar), ',d').replace(',', '.'))
