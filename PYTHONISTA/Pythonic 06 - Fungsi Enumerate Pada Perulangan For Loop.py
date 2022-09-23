# cara tidak pythonic
nim = ["001", "002", "003"]
nama = ["adi", "ansyah", "putra"]
for i in range(len(nim)):
    print(f"nim = {nim[i]} --- nama = {nama[i]}")


print(f"\nPYTHONISTA\n")

# PYTHONIC
nim = ["001", "002", "003"]
nama = ["adi", "ansyah", "putra"]
for i, dataNim in enumerate(nim):
    print(f"{dataNim} -- {nama[i]}")
