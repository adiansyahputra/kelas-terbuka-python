"""
Python mendukung penggunaan else sebagai pasangan dari while. Blok pernyataan else hanya akan dieksekusi bila kondisi while bernilai salah.
"""

count = 0

while count < 8:
    print(count, "kurang dari 8")
    count += 1
else:
    print(count, "tidak kurang dari 8")
