# cara tidak pythonic
nama = "ivankov"
if nama == "budi" or nama == "santi" or nama == "kimi":
    print("siswa teladan")
else:
    print("siswa reguler")


print(f"\nPYTHONISTA\n")

# Pythonic
nama = "risbu"
if nama in ("budi", "salsa", "kimi"):
    print("siswa teladan")
else:
    print("siswa reguler")
