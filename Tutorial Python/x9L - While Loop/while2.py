# else, break, continue, pass
angka = 0

while angka < 10:

    if angka == 5:
        # print("checkpoint 1")
        # break
        angka += 1
        continue
        # print("checkpoint2")

    print("nilai angka adalah", angka)
    angka += 1
else:
    print("nilai angka diakhir while adalah:", angka)

print("diluar while")
