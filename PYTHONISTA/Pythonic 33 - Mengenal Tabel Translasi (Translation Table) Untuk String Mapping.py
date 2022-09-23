# cara tidak Pythonic
# yg mau diganti = a, i ,e ,o --> 4,1,3,0

kalimatYangMauDiganti = "Belajar Python"
translasi = {
    "a": "4",
    "i": "1",
    "e": "3",
    "o": "0"
}
kalimatSetelahDiganti = ""
for item in kalimatYangMauDiganti:
    val = translasi.get(item)
    kalimatSetelahDiganti += val if val else item

print(f"kalimat setelah diganti = {kalimatSetelahDiganti}")


print(f"\nPYTHONISTA\n")

# Pythonic
hulu = "a, i, e, o"
# hulu = "aieo" --> ini juga bisa
hilir = "4, 1, 3, 0"
# hilir = "4130" --> ini juga bisa
kalimatSebelum = "Belajar Dart"
tabelTranslasi = str.maketrans(hulu, hilir)
kalimatSesudah = kalimatSebelum.translate(tabelTranslasi)
print(f"kalimat Sesudah = {kalimatSesudah}")
