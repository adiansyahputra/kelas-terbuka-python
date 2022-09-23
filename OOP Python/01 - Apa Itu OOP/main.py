class Hero:  # ----> template
    pass


hero1 = Hero()  # ----> object / instance / instansiate
hero2 = Hero()
hero3 = Hero()

hero1.name = "Adi"
hero1.health = 100

hero2.name = "Leonard"
hero2.health = 190

hero3.name = "Reginald"
hero3.health = 290

print(hero1.__dict__)
print(hero1.name)
