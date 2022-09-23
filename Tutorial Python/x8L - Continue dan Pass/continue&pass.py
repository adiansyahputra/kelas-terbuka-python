# bedanya break dengan continue
# break = fungsinya untuk mengakhiri for (terminasi) / langsung ke bawah
# continue = fungsinya untuk melanjutkan ke step berikutnya / langsung naik ke atas
# pass fungsinya = untuk dummy di for if else / dilewatkan saja dan mengerjakan perintah dibawahnya
for i in range(1, 10):
    if i == 6:
        print("ini adalah nilai 6")
        break
        # continue
        # pass
        print("cek bro 1")
    print("nilai saat ini adalah", i)
else:
    print("akhir dari loop")

print("print di luar loop")
