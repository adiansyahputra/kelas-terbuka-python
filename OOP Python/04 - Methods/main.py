class Hero:
    # class atribute
    jumlah_hero = 0

    # instance atribute
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    # method
    # 1. method tanpa argumen dan tanpa return
    def siapa(self):
        print("halo saya adi")

    # 2. method dengan argumen
    def healthup(self, up):
        self.health += up

    # 3. method dengan return
    def getHealth(self):
        return self.health


# object
hero1 = Hero("adi", 1000, 1000, 1000)

hero1.siapa()
hero1.healthup(10)
print(hero1.health)
print(hero1.getHealth())
