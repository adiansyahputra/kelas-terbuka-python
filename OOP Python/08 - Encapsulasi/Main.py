class Hero:

    def __init__(self, name, attack, health):
        self.__name = name
        self.__attack = attack
        self.__health = health

    # getter
    def getName(self):
        return self.__name

    def getAttack(self):
        return self.__attack

    def getHealth(self):
        return self.__health

    # setter
    def diserang(self, serangan):
        self.__health -= serangan

    def upAttack(self, upAttack):
        self.__attack += upAttack


adi = Hero("adi", 5, 50)
print(adi.getName())
print(adi.getAttack())
print(adi.getHealth())
adi.upAttack(4)
print(adi.getAttack())
adi.diserang(10)
print(adi.getHealth())
