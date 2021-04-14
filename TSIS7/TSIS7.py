import pygame
from math import pi, sin, cos 
pygame.init()

WIDTH = 1040
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sin cos figure")


isOn = True


FPS = 1
clock = pygame.time.Clock()

while isOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isOn = False
    
    screen.fill((255,255,255))
    for i in range(0, 961, 20):
        if i == 480:
            pygame.draw.line(screen,(0,0,0),(i + 40,0),(i + 40,720), 2)
        elif i % 160 == 0:
            pygame.draw.line(screen,(0,0,0),(i + 40,0),(i + 40,720))
        elif i % 80 == 0:
            pygame.draw.line(screen,(0,0,0),(i + 40,0),(i + 40,25))
        elif i % 40 == 0:
            pygame.draw.line(screen,(0,0,0),(i + 40,0),(i + 40,15))
        elif i % 20 == 0:
            pygame.draw.line(screen,(0,0,0),(i + 40,0),(i + 40,5))
    for i in range(0, 641, 20):
        if i == 320:
            pygame.draw.line(screen,(0,0,0),(0,i + 40),(1300, i + 40), 2)
        elif i % 80 == 0:
            pygame.draw.line(screen,(0,0,0),(0,i + 40),(1300, i + 40))
        elif i % 40 == 0:
            pygame.draw.line(screen,(0,0,0),(0,i + 40),(15, i + 40))
        elif i % 20 == 0:
            pygame.draw.line(screen,(0,0,0),(0,i + 40),(5, i + 40))
    for x in range(40, 1001):
        sin_y1 = 320 * sin((x - 40) / 160 * pi)
        sin_y2 = 320 * sin((x - 39) / 160 * pi)
        pygame.draw.aalines(screen, (255, 0, 0), False, [(x, 360 + sin_y1), ((x + 1), 360 + sin_y2)])
    
    for x in range(40, 1001, 4):
        cos_y1 = 320 * cos((x - 40) / 160 * pi)
        cos_y2 = 320 * cos((x - 38) / 160 * pi)
        pygame.draw.aalines(screen, (0, 0, 255), False, [(x, 360 + cos_y1), ((x + 2), 360 + cos_y2)])
    pygame.display.flip()