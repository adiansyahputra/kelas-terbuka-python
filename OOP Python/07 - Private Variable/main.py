class Hero:

    # class variable
    jumlah = 0

    def __init__(self, inputNama, inputHealth):
        self.nama = inputNama
        self.health = inputHealth
        # instance private variable
        self.__private = "private"
        # instance protected variable --> useless kang wkwk
        self._protected = "protected"


rockstar = Hero("rockstar", 100)
rockstar.__private = "private new"
rockstar._protected = "protected new"
print(rockstar.__dict__)
print(rockstar.__private)
