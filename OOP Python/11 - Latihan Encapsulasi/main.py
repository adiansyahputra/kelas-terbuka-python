class Hero:
    # private class variable
    __jumlah = 0

    def __init__(self, name, health, attack, armor):
        self.__name = name
        self.__healthBase = health
        self.__attackBase = attack
        self.__armorBase = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthBase * self.__level
        self.__attack = self.__attackBase * self.__level
        self.__armor = self.__armorBase * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    # private class method
    @property
    def info(self):
        return f"{self.__name}: \n\t{self.__health}/{self.__healthMax}\n\t{self.__attack}\n\t{self.__armor}"

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if(self.__exp >= 100):
            print(self.__name, f"level up")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthBase * self.__level
            self.__attack = self.__attackBase * self.__level
            self.__armor = self.__armorBase * self.__level

    def attack(self, musuh):
        self.gainExp = 50


slardar = Hero("slardar", 100, 5, 10)
axe = Hero("axe", 100, 5, 10)
print(slardar.info)

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)
print(slardar.info)
