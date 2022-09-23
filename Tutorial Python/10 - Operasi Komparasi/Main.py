# operasi komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 5
b = 2

# lebih dari (>)
print("=====Lebih dari (>)=====")
hasil = a > 3
print(a, ">", 3, "=", hasil)
hasil = b > 3
print(b, ">", 3, "=", hasil)
hasil = b > 2
print(b, ">", 2, "=", hasil)

# kurang dari (<)
print("=====kurang dari (<)=====")
hasil = a < 3
print(a, "<", 3, "=", hasil)
hasil = b < 3
print(b, "<", 3, "=", hasil)
hasil = b < 2
print(b, "<", 2, "=", hasil)

# lebih dari sama dengan (>=)
print("=====lebih dari sama dengan (>=)=====")
hasil = a >= 3
print(a, ">=", 3, "=", hasil)
hasil = b >= 3
print(b, ">=", 3, "=", hasil)
hasil = b >= 2
print(b, ">=", 2, "=", hasil)

# kurang dari sama dengan (<=)
print("=====kurang dari sama dengan (<=)=====")
hasil = a <= 3
print(a, "<=", 3, "=", hasil)
hasil = b <= 3
print(b, "<=", 3, "=", hasil)
hasil = b <= 2
print(b, "<=", 2, "=", hasil)

# sama dengan dari (==)
print("=====sama dengan dari (==)=====")
hasil = a == 5
print(a, "==", 5, "=", hasil)
hasil = b == 5
print(b, "==", 5, "=", hasil)

# tidak sama dengan dari (!=)
print("=====tidak sama dengan dari (!=)=====")
hasil = a != 5
print(a, "!=", 5, "=", hasil)
hasil = b != 5
print(b, "!=", 5, "=", hasil)

# "is" sebagai komparasi objek identity
print("=====object identity (is)=====")
a = 7  # ini adalah assignment membuat object
b = 7
print("nilai a =", a, "id =", hex(id(a)))
print("nilai b =", b, "id =", hex(id(b)))
hasil = a is b
print("a is b =", hasil)
a = 7  # ini adalah assignment membuat object
b = 9
print("nilai a =", a, "id =", hex(id(a)))
print("nilai b =", b, "id =", hex(id(b)))
hasil = a is b
print("a is b =", hasil)

# "is not" sebagai komparasi objek identity
print("=====object identity (is not)=====")
a = 7  # ini adalah assignment membuat object
b = 7
print("nilai a =", a, "id =", hex(id(a)))
print("nilai b =", b, "id =", hex(id(b)))
hasil = a is not b
print("a is b =", hasil)
a = 7  # ini adalah assignment membuat object
b = 9
print("nilai a =", a, "id =", hex(id(a)))
print("nilai b =", b, "id =", hex(id(b)))
hasil = a is not b
print("a is b =", hasil)
