number = 12
for i in range(0, 40, 5):  # looping dengan range
    print(i)
    if i == number:
        print("angka ditemukan", i)
        break
else:
    print("angka tidak ditemukan")

print("space di luar for")
