# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_awal = "adi"
nama_tengah = "ansyah"
nama_akhir = "putra"

nama_lengkap = nama_awal + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + "=" + str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

D = "D"
status = D in nama_lengkap
print("string " + D + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print("string " + d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*11)
print(11*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-7 : " + nama_lengkap[7])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-[0,2] : " + nama_lengkap[0:3])
print("index ke-[4,10] : " + nama_lengkap[4:11])
print("index ke-[0,2,4,6,8,10] : " + nama_lengkap[0:11:2])

# item paling kecil
print("item paling kecil : " + min(nama_lengkap))

# item paling besar
print("item paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))

data = 97
print("char untuk ASCII code 97 adalah " + chr(data))

# 4. operator dalam bentuk method
data = "adi bedidi guridi adiadi"
jumlah = data.count("d")
print("jumlah d pada " + data + " = " + str(jumlah))
