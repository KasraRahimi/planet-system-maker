
class Planet:
    G = 6.6743e-11

    def __init__(self, mass, color, pos=(0, 0), dx=0, dy=0, radius=5):
        self.mass = mass
        self.color = color
        self.pos = pos
        self.dx = dx
        self.dy = dy
        self.radius = radius
    
    @property
    def x(self):
        return self.pos[0]
    
    @property
    def y(self):
        return self.pos[1]
    
    def calculateDistance(self, other, is_vector=False):
        x1, x2, y1, y2 = self.x, other.x, self.y, other.y
        deltaX = x2 - x1
        deltaY = y2 - y1

        if is_vector:
            return deltaX, deltaY
        else:
            return (deltaX**2 + deltaY**2)**(1/2)

    def calculateForce(self, other, is_vector=False):
        m1 = self.mass
        m2 = other.mass
        r = self.calculateDistance(other)
        F = self.G * m1 * m2 / r**2

        if is_vector:
            deltaX = self.calculateDistance(other, True)[0]
            deltaY = self.calculateDistance(other, True)[1]

            Fx = F * deltaX / r
            Fy = F * deltaY /r
            return Fx, Fy
        else:
            return F
    
    def updatePosition(self, planets : list, timestep=3600):
        sumFx, sumFy = 0, 0
        for planet in planets:
            if planet == self:
                continue
            sumFx += self.calculateForce(planet, True)[0]
            sumFy += self.calculateForce(planet, True)[1]
        
        x, y = self.x, self.y
        ddx = sumFx / self.mass
        ddy = sumFy / self.mass
        self.dx += ddx * timestep
        self.dy += ddy * timestep
        x += self.dx * timestep
        y += self.dy * timestep
        self.pos = (x, y)
