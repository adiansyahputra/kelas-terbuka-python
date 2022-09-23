# cara tidak pythonic
a = -10
if a < 0:
    b = "negatif"
else:
    b = "positif"
print(f"{a} adalah bilangan {b}")

print()


print(f"\nPYTHONISTA\n")

# PYTHONIC
a = -20
b = "positif" if a > 0 else "negatif"
print(f"{a} adalah bilangan {b}")
