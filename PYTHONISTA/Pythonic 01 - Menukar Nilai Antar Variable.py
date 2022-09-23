# cara tidak pythonista
a = 10
b = 20
print("sebelum pertukaran")
print(f"a = {a}, b = {b}")
c = a
a = b
b = c
print("setelah pertukaran")
print(f"a = {a}, b = {b}")


print(f"\nPYTHONISTA\n")

# PYTHONIC
a, b, c, d, e = 1, 2, 3, 4, 5
print("sebelum pertukaran")
print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")
a, b, c, d, e = e, d, c, b, a
print("setelah pertukaran")
print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")
