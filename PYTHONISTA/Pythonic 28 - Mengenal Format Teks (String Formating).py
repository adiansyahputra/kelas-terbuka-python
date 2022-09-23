# cara tidak pythonic
nama = "gerix"
nim = 112
print("nama saya " + nama + " nim saya " + str(nim))  # --> cara Java
print("nama saya %s dan nim saya adalah %d" % (nama, nim))  # --> cara C

print(f"\nPYTHONISTA\n")

# Pythonic
print("nama saya {} dan nim saya adalah {}".format(nama, nim))
mahasiswa = {
    "nama": "budi",
    "kelas": "si",
    "nim": 120
}
print("nama gua {nama} kelas gua {kelas} nim gua {nim}".format(**mahasiswa))
print(f"ini baru nama gua {nama}, dan nim gua {nim}")
print(
    f"nama gua {mahasiswa['nama']} kelas gua {mahasiswa['kelas']} nim gua {mahasiswa['nim']}")
