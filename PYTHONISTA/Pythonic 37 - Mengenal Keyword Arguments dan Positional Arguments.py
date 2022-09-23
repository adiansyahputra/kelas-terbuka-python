# cara tidak pythonic
def nama(f_nama, l_nama):
    print(f"nama depan = {f_nama}, nama belakang = {l_nama}")


nama("robi", "misoldi")


print(f"\nPYTHONISTA\n")

# Pythonic


def nama(f_nama, l_nama):
    print(f"nama depan = {f_nama}, nama belakang = {l_nama}")


nama(l_nama="misoldi", f_nama="robi")
