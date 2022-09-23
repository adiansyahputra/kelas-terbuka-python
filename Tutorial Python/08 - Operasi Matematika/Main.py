# operasi aritmatika

a = 20
b = 12

# operasi pertambahan +
hasil = a + b
print(a, "+", b, "=", hasil)

# operasi pengurangan -
hasil = a - b
print(a, "-", b, "=", hasil)

# operasi perkalian *
hasil = a * b
print(a, "*", b, "=", hasil)

# operasi pembagian /
hasil = a / b
print(a, "/", b, "=", hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a, "**", b, "=", hasil)

# operasi modulus (sisa bagi) %
hasil = a % b
print(a, "%", b, "=", hasil)

# operasi floor division (pembagian yg hasilnya dibulatkan ke bawah) //
hasil = a // b
print(a, "//", b, "=", hasil)

# prioritas operasi / operation precedence
# urutannya adalah (), eksponen, perkalian, pertambahan
'''
    1. ()
    2. eksponen **
    3. perkalian * % // / 
    4. pertambahan dan pengurangan + -
'''
a = 2
b = 3
c = 4
hasil = a ** b * c + a - b % c // a
print(a, "**", b, "*", c, "+", a, '-', b, "%", c, "//", a, "=", hasil)

hasil = a + b * c
print(a, "+", b, "*", c, "=", hasil)

hasil = (a + b) * c
print("(", a, "+", b, ")", "*", c, "=", hasil)
