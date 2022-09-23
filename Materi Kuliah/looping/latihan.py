"""
Latihan
Lakukan pengulangan input data sebanyak 2 kali dengan data dibawah ini :
Data Ke- <berulang>
Masukkan NIM anda : <Input Data Ke 1>
Masukkan Nilai UTS : <Input Data Ke 1>
Masukkan Nilai UAS : <Input Data Ke 1>
Nim anda adalah <outputnim1> nilai UTS anda <outpututs1> nilai UTS anda <outputuas1>
"""

data = 1

while data <= 2:
    if data == 3:
        break
    print("Data ke -", data)
    nim = int(input("Masukkan NIM anda : "))
    uts = int(input("Masukkan nilai UTS : "))
    uas = int(input("Masukkan nilai UAS : "))
    print(f"Nim anda adalah {nim} nilai UTS anda {uts} nilai UAS anda {uas}")
    data += 1
