class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor

    @property
    def info(self):
        return f"name = {self.name}\n\thealth = {self.__health}"


sniper = Hero("bigi", 100, 10)
print(sniper.info)

sniper.name = "geri"
print(sniper.info)
