class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, name):
        self.name = name
        print(self.name, "constructed")

    def party(self):
        self.x += 1
        print(self.name, "party album_count", self.x)


class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points += 7
        self.party()
        print(self.name, "points", self.points)

s = PartyAnimal("Sally")
s.party()
print(s.name)

j = FootballFan("Jim")
j.party()
j.touchdown()

