class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print(f"show info di kelas hero")
        print(f"{self.name} :\n\thealth : {self.health}")

# subclass


class Hero_intelligent(Hero):
    def __init__(self, name):
        # mengambil dari parent class
        super().__init__(name, 100)

    def show_info(self):
        print(f"show info di kelas hero_intelligent")
        print(f"{self.name} :\n\thealth : {self.health}")


class Hero_strength(Hero):
    def __init__(self, name):
        # mengambil dari parent class
        super().__init__(name, 200)

    def show_info(self):
        print(f"show info di kelas hero_strength")
        print(f"{self.name} :\n\thealth : {self.health}")


heru = Hero_intelligent("Heru")
hure = Hero_strength("hure")

heru.show_info()
hure.show_info()
