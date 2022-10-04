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


m1 = Monster(400, 200)
m2 = Monster(20, 20)
m3 = m1 + m2

print(len(m1), len(m2))

while m1.attack(): pass
while m2.attack(): pass

m1()
m2()

m3()
