class Mangga:

    # magic method
    # __init__ --> pertama kali dieksekusi saat buat object dengan class ini
    def __init__(self, name, jumlah):
        self.name = name
        self.jumlah = jumlah

    def __repr__(self):  # --> ini biasa dipakai saat debugging
        return f"debug - ini adalah mangga {self.name}, dengan jumlah {self.jumlah}"

    def __str__(self):  # --> ini biasa dipakai saat project sudah jadi
        return f"ini adalah mangga {self.name}, dengan jumlah {self.jumlah}"

    def __add__(self, object):  # --> biasa digunakan dalam program dengan aritmatika
        return self.jumlah + object.jumlah

    @property  # --> disini property untuk mencegah karena terjadi bound
    def __dict__(self):  # --> untuk mengedit dict
        return f"object ini mempunyai nama dan jumlah"


belanja1 = Mangga("manalagi", 3)
belanja2 = Mangga("harummanis", 1)
print(belanja1)
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)
