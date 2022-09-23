class Hero:

    def __init__(self, name, health):
        self.name = name
        self.health = health

# class inheritance


class Hero_intelligent(Hero):
    pass


class Hero_strength(Hero):
    pass


ferrow = Hero("ferrow", 100)
bax = Hero_intelligent("bax", 200)
piwpo = Hero_strength("pipow", 20)
print(ferrow.name)
print(bax.name)
print(piwpo.name)
