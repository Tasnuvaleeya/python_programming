class Enemy:

    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(8)
master = Enemy(18)
jason.get_energy()
master.get_energy()