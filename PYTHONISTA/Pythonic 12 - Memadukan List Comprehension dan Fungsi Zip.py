# cara tidak pythonic
nama = ["adi", "ansyah", "putra"]
umur = [19, 20, 21]
listku = []
for i in range(len(nama)):
    listku.append([nama[i], umur[i]])

print(f"listku = {listku}")


print(f"\nPYTHONISTA\n")

# PYTHONIC
nama = ["putra", "ansyah", "adi"]
nim = [10, 11, 12]
listku = [[d_nama, d_nim]for d_nama, d_nim in zip(nama, nim)]
print(f"listku = {listku}")
