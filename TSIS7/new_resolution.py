import pygame
from math import pi, sin, cos 
pygame.init()

WIDTH = 1100
HEIGHT = 780

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("sin cos figure")

#FONTS
font1 = pygame.font.SysFont("Arial", 30, True)
font2 = pygame.font.SysFont("Arial", 20)

isOn = True


FPS = 1
clock = pygame.time.Clock()

while isOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isOn = False
    
    screen.fill((255,255,255))

    pygame.draw.line(screen,(0,0,0),(50, 10),(1090, 10), 2)
    pygame.draw.line(screen,(0,0,0),(50, 370),(1090, 370), 2)
    pygame.draw.line(screen,(0,0,0),(50, 730),(1090, 730), 2)
    pygame.draw.line(screen,(0,0,0),(50, 10),(50, 730), 2)
    pygame.draw.line(screen,(0,0,0),(570, 10),(570, 730), 2)
    pygame.draw.line(screen,(0,0,0),(1090, 10),(1090, 730), 2)

    for i in range(0, 961, 20):
        if i % 160 == 0:
            pygame.draw.line(screen,(0,0,0),(i + 90, 10),(i + 90, 730))
        elif i % 80 == 0:
            pygame.draw.line(screen,(0,0,0),(i + 90,10),(i + 90, 35))
            pygame.draw.line(screen,(0,0,0),(i + 90,705),(i + 90, 730))
        elif i % 40 == 0:
            pygame.draw.line(screen,(0,0,0),(i + 90,10),(i + 90, 25))
            pygame.draw.line(screen,(0,0,0),(i + 90,715),(i + 90, 730))
        elif i % 20 == 0:
            pygame.draw.line(screen,(0,0,0),(i + 90,10),(i + 90, 15))
            pygame.draw.line(screen,(0,0,0),(i + 90,725),(i + 90, 730))
    for i in range(0, 641, 20):
        if i % 80 == 0:
            pygame.draw.line(screen,(0,0,0),(50, i + 50),(1090, i + 50))
        elif i % 40 == 0:
            pygame.draw.line(screen,(0,0,0),(50, i + 50),(65, i + 50))
            pygame.draw.line(screen,(0,0,0),(1075, i + 50),(1090, i + 50))
        elif i % 20 == 0:
            pygame.draw.line(screen,(0,0,0),(50, i + 50),(55, i + 50))
            pygame.draw.line(screen,(0,0,0),(1085, i + 50),(1090, i + 50))
    for x in range(90, 1049):
        sin_y1 = 320 * sin((x - 90) / 160 * pi)
        sin_y2 = 320 * sin((x - 88) / 160 * pi)
        pygame.draw.aalines(screen, (255, 0, 0), False, [(x, 370 + sin_y1), ((x + 1), 370 + sin_y2)])
    
    for x in range(90, 1049, 4):
        cos_y1 = 320 * cos((x - 90) / 160 * pi)
        cos_y2 = 320 * cos((x - 88) / 160 * pi)
        pygame.draw.aalines(screen, (0, 0, 255), False, [(x, 370 + cos_y1), ((x + 2), 370 + cos_y2)])
    
    #vertical
    screen.blit(font2.render("1.00", True, (0,0,0)), (8, 38))
    screen.blit(font2.render("0.75", True, (0,0,0)), (8, 118))
    screen.blit(font2.render("0.50", True, (0,0,0)), (8, 198))
    screen.blit(font2.render("0.25", True, (0,0,0)), (8, 278))
    screen.blit(font2.render("0.00", True, (0,0,0)), (8, 358))
    screen.blit(font2.render("-0.25", True, (0,0,0)), (2, 438))
    screen.blit(font2.render("-0.50", True, (0,0,0)), (2, 518))
    screen.blit(font2.render("-0.75", True, (0,0,0)), (2, 598))
    screen.blit(font2.render("-1.00", True, (0,0,0)), (2, 678))

    #horizontal
    screen.blit(font2.render("-0.25", True, (0,0,0)), (2, 438))
    pygame.display.flip()