from planets import Planet
from math import cos, sin, pi
import pygame

# ~ simple color list ~
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
navy = (0, 0, 150)
green = (0, 128, 0)
grey = (128, 128, 128)
yellow = (255, 215, 0)
orange = (255, 140, 0)
khaki = (240, 230, 140)
colors = (
    blue, black, white, red, navy, green, grey, yellow, orange, khaki
)
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
SCALE = 1/1e8  # 1:1000000 ration in real life
timestep = 60
planets = []

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

def createPlanet(mass, position, color, speed, direction, radius):
    dx = cos(direction.value) * speed
    dy = sin(direction.value) * speed
    x = (position[0] - W/2) / SCALE
    y = (position[1] - H/2) / SCALE
    planets.append(
        Planet(mass, color, (x, y), dx, dy, radius)
    )

def main():
    is_running = True
    mass = 5.9736e24
    speed, direction = 0, Angle(0)
    radius = 10
    currentColorIndex = 0
    clock = pygame.time.Clock()

    while is_running:
        window.fill(black)
        currentColor = colors[currentColorIndex]
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    mass /= 1.25
                if event.key == pygame.K_e:
                    mass *= 1.25
                if event.key == pygame.K_w:
                    speed += 1e3
                if event.key == pygame.K_s:
                    speed -= 1e3
                if event.key == pygame.K_a:
                    direction.increaseValue(pi/4)
                if event.key == pygame.K_d:
                    direction.increaseValue(-pi/4)
                if event.key == pygame.K_r:
                    if currentColorIndex == 0:
                        currentColorIndex = len(colors) - 1
                    else:
                        currentColorIndex -= 1
                if event.key == pygame.K_t:
                    if currentColorIndex + 1 == len(colors):
                        currentColorIndex = 0
                    else:
                        currentColorIndex += 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    createPlanet(mass, pos, currentColor, speed, direction, radius)

        for planet in planets:
            drawPlanet(planet)
            planet.updatePosition(planets)
        pygame.draw.circle(window, currentColor, pos, radius)
        end = (pos[0] + speed/50 * cos(direction.value), 
                pos[1] + speed/50 * sin(direction.value))
        pygame.draw.line(window, currentColor, pos, end, 2)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
