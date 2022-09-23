class Hero:

    def __init__(self, inputNama, inputHealth, inputPower, inputArmor):
        self.name = inputNama
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


hero1 = Hero("adi", 1000, 100, 10)
hero2 = Hero("radit", 100, 30, 15)
hero3 = Hero("putra", 200, 20, 20)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
