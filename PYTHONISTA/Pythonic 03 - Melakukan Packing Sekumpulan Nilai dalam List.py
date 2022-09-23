# cara tidak pythonic
a = 1
b = 2
c = 3
d = [None]*3
d[0] = a
d[1] = b
d[2] = c
print(f"a = {a}, b = {b}, c = {c}")
print(f"d = {d}")


print(f"\nPYTHONISTA\n")

# PYTHONIC
a, b, c = 10, 20, 30
# d = a, b, c
d = [a, b, c]
print(f"a = {a}, b = {b}, c = {c}")
print(f"d = {d}")
"""
python secara default melakukan packing sekumpulan nilai ke dalam tuple untuk mengubah menjadi list cukup tambahkan []
"""
