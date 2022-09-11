import math

class Planet:
    scale = 1/1e6
    timestep = 60 * 60  # 1 hour per frame
    G = 6.6743e-11

    def __init__(self, mass, color, pos=(0, 0), dx=0, dy=0, radius=5):
        self.mass = mass
        self.color = color
        self.pos = pos
        self.dx = dx
        self.dy = dy
        self.ddx = 0
        self.ddy = 0
        self.radius = radius
    
    @property
    def x(self):
        return self.pos[0]
    
    @property
    def y(self):
        return self.pos[1]
