# cara kurang pythonic
nim = ["001", "002", "003"]
nama = ["adi", "ansyah", "putra"]
for i, data_nama in enumerate(nama):
    print(f"{nim[i]} --- {data_nama}")


print(f"\nPYTHONISTA\n")

# PYTHONIC
nim = ["001", "002", "003"]
nama = ["Adi", "Ansyah", "Putra"]
hobi = ["belajar", "ngoding", "makan"]
for dataNim, data_Nama, dataHobi in zip(nim, nama, hobi):
    print(f"{dataNim} --- {data_Nama} --- {dataHobi}")
