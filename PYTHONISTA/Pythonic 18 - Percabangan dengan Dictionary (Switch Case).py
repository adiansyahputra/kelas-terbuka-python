# cara tidak pythonic
def one():
    print("one - satu")


def two():
    print("two - dua")


def three():
    print("three - tiga")


case = "satu"
if case == "satu":
    one()
elif case == "dua":
    two()
elif case == "tiga":
    three()


print(f"\nPYTHONISTA\n")

# PYTHONIC


def cie():
    print("cie - satu")


def duo():
    print("duo - dua")


def tigo():
    print("tigo - tiga")


case = "duo"
switch = {
    "cie": cie,
    "duo": duo,
    "tigo": tigo
}
switch[case]()
