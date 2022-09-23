# teknik looping

namaBand = ["Payung Teduh",
            "Fourtwnty",
            "Dialog Dini Hari",
            "Mr. Sonjaya",
            "Parahyena"]

namaLagu = ["Akad",
            "Zona Nyaman",
            "Rumahku",
            "Sang Filsuf",
            "Sindoro"]

playList = {"kuda", "kucing", "semut", "kudanil", "kera", "bebek", "angsa"}

playList2 = {"Payung Teduh": "Akad",
             "Fourtwnty": "Zona Nyaman",
             "Dialog Dini Hari": "Rumahku",
             "Mr. Sonjaya": "Sang Filsuf",
             "Parahyena": "Sindoro"}

# enumerate

for index, band in enumerate(namaBand):
    print(index, ":", band)

# zip

for band, lagu in zip(namaBand, namaLagu):
    print(band, "menanyikan lagu :", lagu)

# set

for hewan in sorted(playList):
    print(hewan)

print("="*100)

# dictionary

for i, v in playList2.items():
    print(i, "lagunya :", v)

# tambahan aja sih

for i in reversed(range(1, 10, 1)):
    print(i)
