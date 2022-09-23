class Team:

    def set_team(self, team):
        self.team = team

    def show_team(self):
        print(self.team)


class Tipe_Hero:

    def set_tipe(self, tipe):
        self.tipe = tipe

    def show_tipe(self):
        print(self.tipe)


class Hero(Team, Tipe_Hero):

    def __init__(self, name, health):
        self.name = name
        self.health = health


foxterlin = Hero("foxterlin", 100)
foxterlin.set_team("biru")
foxterlin.set_tipe("penyerang")

foxterlin.show_team()
foxterlin.show_tipe()
