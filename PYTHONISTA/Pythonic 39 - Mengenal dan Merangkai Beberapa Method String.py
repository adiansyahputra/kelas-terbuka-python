# Cara tidak Pythonic
a = "  Belajar Bahasa Pemrograman Python : from Guido Van Rossum  "
print(f"a = {a}")
b = a.strip()
print(f"b = {b}")
b = b.upper()
print(f"b = {b}")
b = b.lower()
print(f"b = {b}")
b = b.replace(":", "%")
print(f"b = {b}")


print(f"\nPYTHONISTA\n")

# Pythonic
a = "  Belajar Bahasa Pemrograman Python : from Guido Van Rossum  "
print(f"a = {a}")
b = a.strip().lower().replace(":", "@")
print(f"b = {b}")
