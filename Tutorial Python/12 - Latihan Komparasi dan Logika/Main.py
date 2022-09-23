# episode latihan komparasi dan logika

# membuat gabungan area rentang dari angka
# ++++++++3------------10+++++++++
inputUser = float(input("masukkan angka kurang dari 3 atau lebih dari 10: "))

# ++++++++3-------
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

# --------10++++++
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

# ++++++++3------------10+++++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan =", isCorrect)

print('\n', 10 * "=", '\n')

# membuat irisan area rentang dari angka
# ------3+++++++++10------
inputUser = float(input("masukkan angka antara 3 sampai 10: "))

# ------3++++++++
isLebihDari = (inputUser > 3)
print("Lebih dari 3 =", isLebihDari)

# ++++++10-------
isKurangDari = (inputUser < 10)
print("Kurang dari 10 =", isKurangDari)

# --------3++++++++++++10--------
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan =", isCorrect)

print("\n", 10 * "=", "\n")

# tugas
# ------0++++++5-------8+++++++11------
inputDariLoe = float(input(
    "masukkan angka antara 0 sampai 5 atau antara 8 sampai 11 ="))
lebihDariNol = (inputDariLoe > 0)
print("lebih dari 0 =", lebihDariNol)

kurangDariLima = (inputDariLoe < 5)
print("kurang dari 5 =", kurangDariLima)

apakahBenar1 = lebihDariNol and kurangDariLima
print("angka yang anda masukkan antara 0 sampai 5 =", apakahBenar1)

lebihDariLapan = (inputDariLoe > 8)
print("lebih dari 8 =", lebihDariLapan)

kurangDariSebel = (inputDariLoe < 11)
print("kurang dari 11 =", kurangDariSebel)

apakahBenar2 = lebihDariLapan and kurangDariSebel
print("angka yang anda masukkan antara 8 sampai 11 =", apakahBenar2)

isCorrect = apakahBenar1 or apakahBenar2
print("angka yang anda masukkan =", isCorrect)

# ++++++0------5+++++++8-------11++++++
