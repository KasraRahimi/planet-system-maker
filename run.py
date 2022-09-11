from planets import Planet
from math import cos, sin, pi
import pygame

# ~ simple color list ~
blue = (0,0,255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
navy = (0, 0, 150)
green = (0, 128, 0)
grey = (128, 128, 128)
yellow = (255,215,0)
orange = (255,140,0)
khaki = (240,230,140)
# =====================

class Angle:
    def __init__(self, value):
        self.value = value

    def increaseValue(self, step):
        self.value += step
        if self.value > 2 * pi:
            self.value -= 2 * pi
        if self.value < 0:
            self.value += 2 * pi


W, H = 16*60, 9*60
SCALE = 1/1e6  # 1:1000000 ration in real life
EARTH_MASS = 5.9736e24
planets = []
speed, direction = 0, Angle(0)
radius = 5
clock = pygame.time.Clock()

pygame.init()
window = pygame.display.set_mode((W, H))
pygame.display.set_caption("planet system simulator")

def drawPlanet(planet : Planet):
    x = planet.x * SCALE + W/2
    y = planet.y * SCALE + H/2
    pos = (x, y)
    radius = planet.radius
    color = planet.color
    pygame.draw.circle(window, color, pos, radius)

def createPlanet(mass, position, color, speed, direction):
    dx = cos(direction) * speed
    dy = sin(direction) * speed
    planets.appent(
        Planet(mass, color, position, dx, dy, radius)
    )

def main():
    is_running = True

    while is_running:
        window.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(window, blue, pos, 30)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

