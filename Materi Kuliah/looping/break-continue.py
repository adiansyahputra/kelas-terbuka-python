"""
Looping umumnya akan berhenti bila kondisi sudah bernilai salah. Akan tetapi, seringkali kita perlu keluar dari looping di tengah jalan tergantung keperluan. Hal ini bisa kita lakukan dengan menggunakan kata kunci break dan continue.

Statement break memaksa program keluar dari blok looping di tengah jalan. Sedangkan statement continue menyebabkan program langsung melanjut ke step / interval berikutnya dan mengabaikan (skip) baris kode di bawahnya (yang satu blok). Jelasnya perhatikan contoh berikut:
"""

# contoh penggunaan statement break
for letter in "PythonProgramming":
    if letter == "g":
        break
    print("Huruf sekarang:", letter)
print("good bye!")

"""
Bila pada program di atas kita ganti kode break menjadi continue, maka hasilnya akan jadi seperti berikut:
"""

# contoh penggunaan statement continue
for letter in "PythonProgramming":
    if letter == "g":
        continue
    print("Huruf sekarang:", letter)
print("good bye!")

"""
Perhatikan bahwa huruf g tidak pernah ditampilkan karena diabaikan karena kode continue.
"""
