print("ini adalah program pembagian")

while True:
    try:
        penyebut = int(input("masukkan angka penyebut"))
        pembilang = int(input("masukkan angka pembilang"))
        hasil = penyebut / pembilang
        break
    except ValueError:
        print("yang anda masukkan bukan angka")
    except ZeroDivisionError:
        print("yang anda masukkan adalah angka 0 tolong diganti ya bro sis wkwk")
    except Exception as err:
        print(err)

print("hasil pembagian adalah : ", hasil)
