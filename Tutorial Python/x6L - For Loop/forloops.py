# list sebagai iterable
gorengan = ["bakwan", "risol", "tahu isi",
            "pastel", "lontong", "tempeg goreng"]
for g in gorengan:
    print(g)
    print(len(g))

# string sebagai iterable
bakwan = "bakwan"
for i in bakwan:
    print(i)

# for di dalam for
gorengan = ["bakwan", "risol", "tahu isi",
            "pastel", "lontong", "tempeg goreng"]
buah = ["anggur", "semangka", "pepaya", "melon", "mangga"]
sayur = ["kangkung", "bayam", "katuk", "oyong", "sop"]

Daftar_belanja = [gorengan, buah, sayur]
print(Daftar_belanja)

print(39*"=")

for subDaftarBelanja in Daftar_belanja:
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)
