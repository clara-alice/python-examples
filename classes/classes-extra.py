class Monster:
    '''
    A Monster has some attributes
    '''

    def __init__(self, energy, health):
        self.energy = energy
        self.health = health

        # privates attributes
        self._id = 5 # not modified by convention

    # methods
    def attack(self):
        print('attack')
        self.energy -= 20

    def move(self, speed):
        print('move')
        self.energy -= 2 * speed

monster = Monster(100, 100)

# hasattr
print(hasattr(monster, 'health'))

# setattr
setattr(monster, 'weapeon', 'Sword')
print(monster.weapeon)

# doc
print(monster.__doc__)
