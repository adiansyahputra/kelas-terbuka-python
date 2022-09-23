"""
Python Decimal
Ada kalanya perhitungan menggunakan float di Python membuat kita terkejut. Kita tahu bahwa 1.1 ditambah 2.2 hasilnya adalah 3.3. Tapi pada saat kita lakukan dengan Python, maka hasilnya berbeda.
>>> (1.1 + 2.2 ) == 3.3
False
>>> 1.1 + 2.2 3.3000000000000003
Mengapa terjadi demikian?
Hal ini terjadi karena bilangan dalam komputer disimpan dalam bentuk digit 0 atau 1. Bila padanan digitnya tidak sesuai, maka bilangan float seperti 0.1 dalam bilangan biner akan menjadi pecahan yang sangat panjang yaitu 0.000110011001100110011... dan komputer kita hanya akan menyimpan panjang yang terbatas. Hal inilah yang menyebabkan terjadinya masalah seperti pada contoh di atas.
Untuk menangani hal seperti itu, kita bisa menggunakan modul bawaan Python yaitu modul decimal. Float hanya memiliki presisi sampai 15 digit di belakang koma, sementara dengan modul decimal kita bisa mengatur presisi jumlah digit di belakang koma.
"""

from decimal import Decimal as D
import decimal

# output: 0.1
print(0.1)

# output: 0.1000000000000000055511151231257827021181583404541015625"
print(decimal.Decimal(0.1))

"""
Modul ini juga membuat kita bisa melakukan perhitungan seperti di sekolah.
"""

print(D(1.1) + D(2.2))  # -------> ini salah ya, yang benar ada dibawah
# output: Decimal("3.3")
print(D("1.1") + D("2.2"))

print(D(1.2) * D(2.50))  # -------> ini salah ya, yang benar ada dibawah
# output: Decimal("3.000")
print(D("1.2") * D("2.50"))

"""
Kapan Saatnya Menggunakan Decimal Dibanding Float? Kita lebih baik menggunakan Decimal dalam kasus:
• Saat kita ingin membuat aplikasi keuangan yang membutuhkan presisi desimal yang pasti
• Saat kita ingin mengontrol tingkat presisi yang diperlukan
• Saat kita ingin menerapkan perkiraan berapa digit decimal yang signifikan
• Saat kita ingin melakukan operasi perhitungan sama persis dengan yang kita lakukan di sekolah

"""
