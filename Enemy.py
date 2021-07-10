class Enemy():
    def __init__(self,health,damage):
        self.health = health
        self.damage = damage


    def attack(self):
        pass


class Goblin(Enemy):
    def __init__(self):
        self.name = "Goblin"
        super(Goblin, self).__init__(100, 5)
        print("Glglg!!! I am a Goblin and I will slash you!!!")


class Orc(Enemy):
    def __init__(self):
        self.name = "Orc"
        super(Orc, self).__init__(100, 15)
        print("Wraar I am a Orc and I will cut you down!!!")


class Rat(Enemy):
    def __init__(self):
        self.name = "Rat"
        super(Rat, self).__init__(100, 10)
        print("Squil!! I am a Rat and I will eat you alive!!!")
