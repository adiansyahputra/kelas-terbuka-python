class Hero:

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

    def serang(self, lawan):
        print(self.name + " serang " + lawan.name)
        lawan.diserang(self, self.power)

    def diserang(self, lawan, powerLawan):
        print(self.name + " di serang " + lawan.name)
        seranganLawan = powerLawan / self.armor
        print("serangan tersisa = " + str(seranganLawan))
        self.health -= seranganLawan
        print("sisa darah dari serangan lawan = " + str(self.health))


adi = Hero("adi", 100, 20, 5)
radit = Hero("radit", 100, 10, 5)

while True:

    adi.serang(radit)
    radit.serang(adi)

    if adi.health <= 0:
        break
    elif radit.health <= 0:
        break
