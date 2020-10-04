from .pool import Pool
from .swimmer import Swimmer

class Model:
    def __init__(self, nswimmers, nlanes=3, sigma_speed=0):
        self.pool = Pool()
        self.swimmers = [Swimmer(self.pool) for n in range(nswimmers)]
        
    def step(self, dt):
        for swimmer in self.swimmers:
            swimmer.swim(dt)
    
    def __repr__(self):
        return ','.join(str(swimmer.pos) for swimmer in self.swimmers)
