class Hero:

    # private class method
    __jumlah = 0

    def __init__(self, nama):
        self.nama = nama
        Hero.__jumlah += 1

    # private instance method with getter
    def getJumlah(self):
        return Hero.__jumlah

    # private instance method special for class with staticmethod
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah

    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah


adi = Hero("adi")
print(adi.getJumlah2())
radit = Hero("radit")
print(radit.getJumlah2())
reginald = Hero("reginald")
print(Hero.getJumlah3())
