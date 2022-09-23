class Hero:

    jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("hero bernama " + self.name)


hero1 = Hero("Adi", 1000, 1000, 1000)
print(Hero.jumlah)
hero1 = Hero("radit", 1000, 1000, 1000)
print(Hero.jumlah)
hero1 = Hero("reginald", 1000, 1000, 1000)
print(Hero.jumlah)
