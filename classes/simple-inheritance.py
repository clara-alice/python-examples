class Monster:
    health = 90
    energy = 40

    def __init__(self, health, energy):
        print('the monster has created')
        
        self.health = health
        self.energy = energy

    def __len__(self):
        return self.energy

    def __abs__(self):
        return abs(self.health - self.energy)

    def __call__(self):
        print(self.__dict__)

    def __add__(self, other):
        total_energy = self.energy + other.energy
        total_health = self.health + other.health

        return Monster(total_health, total_energy)

    def attack(self):
        if not self.hasEnergy(20):
            print('can\'t attack')
            return False

        self.energy -= 20
        print('the monster has attacked!')
        return True

    def move(self):
        if not self.hasEnergy(10):
            print('can\'t move')
            return False

        self.energy -= 10
        print('the monster moved!')
        return True

    def hasEnergy(self, amountRequired):
        return self.energy >= amountRequired


class Shark(Monster):
    def __init__(self, health, energy):
        parent.__init__(self, health, energy)
        self.energy += 30

    def bite(self):
        self.energy -= 30
        print('bite :v')

a = Shark(100, 100)



