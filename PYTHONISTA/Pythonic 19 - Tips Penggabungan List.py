# cara tidak pythonic
a = [1, 2, 3]
b = [4, 5, 6]
c = [None]*(len(a) + len(b))

for i in range(len(a)):
    c[i] = a[i]

for i in range(len(b)):
    c[i + len(a)] = b[i]
"""

yg di bawah ini versi gua ya wkwk
c = []
for i in range(len(a)):
    c.append(a[i])
for i in range(len(b)):
    c.append(b[i])

"""

print(c)


print(f"\nPYTHONISTA\n")

# PYTHONIC
a = [10, 11, 12]
b = [13, 14, 15]
c = a + b
print(c)

print()

a = ["adi", 11, True]
b = [False, "adi", 15]
c = b + a
print(c)
