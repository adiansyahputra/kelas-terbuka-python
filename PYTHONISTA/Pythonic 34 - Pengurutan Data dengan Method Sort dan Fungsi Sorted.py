# cara tidak pythonic
mahasiswa = ("elin", "wawang", "gibski", "ajax")
print(mahasiswa)
# mahasiswa.sort()  # --> method sort terbatas hanya untuk imutable (list)
# print(f"method sort = {mahasiswa}")


print(f"\nPYTHONISTA\n")

# Pythonic
fungsiSort = sorted(mahasiswa)
print(f"fungsi sort = {fungsiSort}")
