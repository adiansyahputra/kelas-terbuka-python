# cara tidak pythonic
teks = "belajar pemrograman python"
listku = []
kata = ""
for huruf in teks:
    if huruf != " ":
        kata += huruf
    else:
        listku.append(kata)
        kata = ""
listku.append(kata)
print(listku)


print(f"\nPYTHONISTA\n")

# PYTHONIC
teks = "semangat belajar python"
listku = teks.split()
print(f"listku = {listku}")


print()
teks = "semangat$belajar$python"
listku = teks.split("$")
print(f"listku = {listku}")
