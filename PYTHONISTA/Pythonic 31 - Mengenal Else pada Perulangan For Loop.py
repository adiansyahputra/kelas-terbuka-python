# cara tidak Pythonic
nilai = [80, 70, 60, 50]
kkm = 40
lolosTidaknya = True
for dnilai in nilai:
    if dnilai < kkm:
        print(f"maaf anda tidak lulus")
        lolosTidaknya = False
        break
if lolosTidaknya:
    print(f"selamat anda lulus")


print("\nPYTHONISTA\n")

# Pythonic
nilai = [80, 70, 60, 50]
kkm = 70
for data in nilai:
    if data < kkm:
        print(f"maaf anda tidak lulus")
        break
else:
    print("selamat anda lulus")
