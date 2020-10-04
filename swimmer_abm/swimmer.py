import random

class Swimmer:
    
    def __init__(self, pool, speed=1, d0=0, sigma=0, d_resp=1, dir=1):
        self.speed = speed
        self.sigma = sigma
        self.d_resp = d_resp
        self.pool = pool        
        self.pos = d0
        if dir in [-1, 1]:
            self.dir = dir
        else:
            self.dir = 1
        self._correct_pos()

    def _correct_pos(self):
        # TODO: fix for > 2*pool.length
        if self.pos > self.pool.length:
            self.pos = float(self.pool.length - int(self.pos)%self.pool.length)
            self.dir = -1
        elif self.pos < 0:
            self.pos = -self.pos
            self.dir = 1        

    def swim(self, dt):
        self.pos += self.dir*random.gauss(self.speed, self.sigma)*dt
        self._correct_pos()
        