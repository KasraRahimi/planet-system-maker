from planets import Planet
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

W, H = 16*60, 9*60
SCALE = 1/1e6  # 1:1000000 ration in real life
planets = []

pygame.init()
window = pygame.display.set_mode((W, H))
pygame.display.set_caption("planet system simulator")

def drawPlanet(planet : Planet):
    x = planet.x * scale + W/2
    y = planet.y * scale + H/2
    pos = (x, y)
    radius = planet.radius



