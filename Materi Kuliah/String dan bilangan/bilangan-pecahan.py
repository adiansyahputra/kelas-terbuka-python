"""
Bilangan Pecahan
Python menyediakan modul fractions untuk mengoperasikan bilangan
pecahan. Pecahan adalah bilangan yang memiliki pembilang dan penyebut, misalnya 3/2. Perhatikan contoh berikut:
"""

from fractions import Fraction as F
import fractions

# output: 3/2
print(fractions.Fraction(1.5))

# output: 1/3
print(fractions.Fraction(1, 3))

"""
Operasi dasar seperti penjumlahan atau pembagian pecahan juga bisa dilakukan dengan

"""


# output: 2/3
print(F(1, 3) + F(1, 3))

# output: 6/5
print(1 / F(5, 6))

# output: True
print(F(-3, 10) < 0)
