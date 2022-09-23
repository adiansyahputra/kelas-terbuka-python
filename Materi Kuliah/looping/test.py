def menu():
    print("Menu Pilihan")
    print()
    print("1. Segitiga")
    print("2. Lingkaran")
    print("3. Trapesium")
    print("4. Jajargenjang")
    print("5. Bola")
    print("6. Kerucut")


def segitiga():
    t = int(input("Masukkan tinggi segitiga : "))
    a = int(input("Masukkan alas segitiga : "))
    l = (a * t * 1/2)
    print("Jadi luas segitiga adalah : %d" % (l))
    print("Terima Kasih")


def lingkaran():
    r = int(input("Masukkan jari - jari lingkaran : "))
    l = 3.14 * r * r
    print("Jadi luas lingkaran adalah : %d" % (l))
    print("Terima Kasih")


def trapesium():
    t = int(input("Masukkan tinggi : "))
    j = int(input("Masukkan jumlah sisi sejajar : "))
    l = t * j / 2
    print("Jadi luas trapesium adalah : %d" % (l))
    print("Terima Kasih")


def jajargenjang():
    t = int(input("Masukkan tinggi jajargenjang : "))
    a = int(input("Masukkan alas jajargenjang : "))
    l = a * t
    print("Jadi luas jajargenjang adalah : %d" % (l))
    print("Terima Kasih")


def bola():
    r = int(input("Masukkan jari - jari : "))
    l = 4 * 3.14 * r * r
    print("Jadi luas bola adalah : %d" % (l))
    print("Terima Kasih")


def kerucut():
    t = int(input("Masukkan tinggi segitiganya : "))
    r = int(input("Masukkan jari-jari lingkaran bawahnya : "))
    l = (3.14 * r) * (t * r)
    print("Jadi luas kerucut adalah : %d" % (l))
    print("Terima Kasih")


# Program Utama
print("Selamat Datang di Program Untuk Menghitung Luas")
print("-----------------------------------------------")
menu()
pilih = input("Masukkan pilihan : ")

if pilih == "1":
    segitiga()
elif pilih == "2":
    lingkaran()
elif pilih == "3":
    trapesium()
elif pilih == "4":
    jajargenjang()
elif pilih == "5":
    bola()
elif pilih == "6":
    kerucut()
else:
    print("Masukkan angka sesuai pilihan yang tersedia")
