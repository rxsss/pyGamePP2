import pygame
pygame.init()

HEIGTH = 700
WIDTH = 800
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Paint")


#image
eraseImage = pygame.image.load('./materials/eraser.png')

#Font
font = pygame.font.SysFont("Arial", 30)

#Booleans
rectangle = False
circle = True
eraser = False

#color
color = (255,0,0)

#List of drawings
rectDrawings = list()
circleDrawings = list()
lineDrawings = list()
firstly = True
# print(circleDrawings)
# if firstly:
#     ci = open('circleDrawings.txt', 'r')
#     circleDrawings = ci.read()
#     firstly = False
# print(circleDrawings)
previous, pos = None, None
turn = True
while turn:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = open("rectDrawings.txt", "w")
            c = open("circleDrawings.txt", "w")
            l = open("lineDrawings.txt", "w")
            r.write(str(rectDrawings))
            c.write(str(circleDrawings))
            l.write(str(lineDrawings))
            r.close()
            c.close()
            l.close()
            turn = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            previous = pygame.mouse.get_pos()
            if previous[0] in range(10, 40) and previous[1] in range(10, 40):
                color = (0,0,0)
            if previous[0] in range(50, 80) and previous[1] in range(10, 40):
                color = (255,255,0)
            if previous[0] in range(90, 120) and previous[1] in range(10, 40):
                color = (255,0,255)
            if previous[0] in range(130, 160) and previous[1] in range(10, 40):
                color = (0,255,255)
            if previous[0] in range(500, 530) and previous[1] in range(10, 40):
                rectangle = True
                circle = False
                eraser = False
            if previous[0] in range(540, 570) and previous[1] in range(10, 40):
                rectangle = False
                eraser = False
                circle = True
            if previous[0] in range(580, 615) and previous[1] in range(10, 40):
                eraser = True
                rectangle = False
                circle = False
            if previous[0] in range(670, 760) and previous[1] in range(5, 45):
                pygame.image.save(screen, "screenshot.png")
                
            
        if event.type == pygame.MOUSEMOTION:
            mov = pygame.mouse.get_pos()
            if previous:
                if eraser:
                    lineDrawings.append([previous, mov])
                    previous = mov
        if event.type == pygame.MOUSEBUTTONUP:
            last = pygame.mouse.get_pos()
            if previous:
                if rectangle:
                    rectDrawings.append([color, previous, last])
                if circle:
                    circleDrawings.append([color, previous, last])
            previous = None
    pygame.draw.rect(screen, (128,128,128), pygame.Rect(0,0,800,50))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(10,10,30,30))
    pygame.draw.rect(screen, (255,255,0), pygame.Rect(50,10,30,30))
    pygame.draw.rect(screen, (255,0,255), pygame.Rect(90,10,30,30))
    pygame.draw.rect(screen, (0,255,255), pygame.Rect(130,10,30,30))
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(500,10,30,30))
    pygame.draw.circle(screen, (0,0,0), (555,25), 15)
    screen.blit(eraseImage, (580, 10))
    showText = font.render("Shape: ", True, (0,0,0))
    screen.blit(showText, (390,7))
    pygame.draw.rect(screen, (90,90,90), pygame.Rect(670,5,90,40))
    showSave = font.render("Save", True, (30,30,255))
    screen.blit(showSave, (680,8))
    rectDrawings.reverse()
    circleDrawings.reverse()
    for i in rectDrawings:
        pygame.draw.rect(screen, i[0], pygame.Rect(i[1],(i[2][0] - i[1][0], i[2][1] - i[1][1])))
    for i in circleDrawings:
        pygame.draw.circle(screen, i[0], ((i[2][0] + i[1][0])/2,(i[2][1] + i[1][1])/2 ), i[2][0] - (i[2][0] + i[1][0])/2)
    for i in lineDrawings:
        pygame.draw.line(screen, (255,255,255), i[0], i[1], 20)
    pygame.display.update()


pygame.quit()