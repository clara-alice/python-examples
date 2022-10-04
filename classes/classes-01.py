class Monster:
    health = 90
    energy = 40

    def attack(self):
        if not self.hasEnergy(20):
            print('can\'t attack')
            return

        self.energy -= 20
        print('the monster has attacked!')

    def move(self):
        if not self.hasEnergy(10):
            print('can\'t move')
            return

        self.energy -= 10
        print('the monster moved!')

    def hasEnergy(self, amountRequired):
        return self.energy >= amountRequired


m1 = Monster()
    
m1.attack()
m1.attack()
m1.attack()
m1.attack()
m1.attack()
m1.attack()
