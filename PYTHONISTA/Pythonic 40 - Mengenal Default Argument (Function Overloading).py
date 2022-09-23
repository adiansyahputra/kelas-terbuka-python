# cara tidak pythonic
def sapa(nama, sapaan):
    print(f"Hi, {nama}. {sapaan}")


sapa("ulfah", "selamat pagi")
sapa(sapaan="helo", nama="luox")


print(f"\nPYTHONISTA\n")

# Pythonic


def sapa(nama, sapaan="Apa kabar kawan ?"):
    print(f"Hi, {nama}. {sapaan}")


sapa("ulfah", "selamat pagi")
sapa("newPython")
