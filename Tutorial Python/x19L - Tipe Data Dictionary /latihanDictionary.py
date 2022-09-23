# review
list = [1, 2, 3]
tuple = (1, 2, 3)
set = {1, 2, 3}

# print(type(list))
# print(type(tuple))
# print(type(set))

# dictionary --> structure data associative / mapping

# dictionary = {key:value, key:value}

member1 = {"ID": 101,
           "Nama": "Adiansyah Putra",
           "Pekerjaan": "Mahasiswa",
           "Status Member": "Gold"
           }

member2 = {
    "ID": 102,
    "Nama": "Raditya Hapusan",
    "Pekerjaan": "Programmer",
    "Status Member": "Legendary"
}

memberList = {101: member1, 102: member2}
# print(member1["ID"])
# print(member1.keys())
# print(member1.values())
# print(member1.items())

print(memberList[101])
