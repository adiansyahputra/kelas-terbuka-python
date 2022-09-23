# latihan konversi satuan temperatur

# program konversi celcius ke satuan lain
print("\nPROGRAM KONVERSI SATUAN\n")

celcius = float(input("masukkan suhu dalam celcius : "))
print("suhu yang diinput adalah", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah", reamur, "Reamur")

# farenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah", kelvin, "Kelvin")


print("\n<=====Tugas=====>\n")

# merubah fahrenheit ke kelvin
# fahrenheit -> celcius -> kelvin
fahrenheit = float(input("masukkan suhu dalam fahrenheit: "))
kelvin = ((5/9) * (fahrenheit - 32)) + 273.15
print("suhu dalam kelvin adalah", kelvin, "Kelvin")

# merubah kelvin ke fahrenheit
# kelvin -> celcius -> fahrenheit
kelvin = float(input("masukkan suhu dalam kelvin: "))
fahrenheit1 = (kelvin - 273.15)
fahrenheit2 = ((9/5) * fahrenheit1) + 32
print("suhu dalam fahrenheit adalah", fahrenheit2, "Fahrenheit")
