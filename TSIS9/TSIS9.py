import pygame
import random
import time
import os
pygame.init()


#Initialize files
images = {}
def get_image(path):
    global images
    image = images.get(path)
    if image == None:
        canonPath = path.replace("/", os.sep).replace("\\", os.sep)
        image = pygame.image.load(path)
        images[path] = image
    return image




#main Settings
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake game")
scoreFont = pygame.font.SysFont('Arial', 30)
wallImage = get_image('./materials/wall.png')
wallSize = wallImage.get_width()


#Levels
mainMenuBool = True
firstLevel = False
secondLevel = False
thirdLevel = False
continueGame = True
continueFirst = False
continueSecond = False
continueThird = False

#Text
mainMenuFont = pygame.font.SysFont('Arial', 25)
scoreFont = pygame.font.SysFont('Arial', 30)
gameOverFont = pygame.font.SysFont('Myraid Pro', 60)
gameOver = gameOverFont.render("Game Over", True, (0,0,0))




#Clock
clock = pygame.time.Clock()


class Snake:
    def __init__(self):
        self.size = 3
        self.radius = 10
        self.dx = 10
        self.dy = 0
        self.elements = [[100, 100], [120, 100], [140, 100]]
        self.score = 0
        self.add = False

    def addSnake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0,0])
        self.add = False

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen, (255,0,0), element, self.radius)


    def move(self):
        if self.add:
            self.addSnake()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

class Food:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = random.randint(50, HEIGHT - 50)
        self.image = get_image("./materials/food.png")

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

def collision():
    if ((food.x in range(snake.elements[0][0] - 10, snake.elements[0][0] + 10)) and (food.y in range(snake.elements[0][1] - 10, snake.elements[0][1] + 10))) or (snake.elements[0][0] in range(food.x, food.x + 30) and snake.elements[0][1] in range(food.y, food.y + 30)):
        food.x = random.randint(50, WIDTH - 50)
        food.y = random.randint(50, WIDTH - 50)
        snake.score += 1
        snake.add = True
        snake.score += 1
        snake.add = True
def gameOverScreen():
    screen.fill((255,0,0))
    screen.blit(gameOver,((600 - gameOver.get_width())/2, (600 - gameOver.get_height())/2))
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
def collisWall():
    if (snake.elements[0][0] > 600 - wallSize or snake.elements[0][0] < wallSize) or (snake.elements[0][1] > 600 - wallSize or snake.elements[0][1] < wallSize):
        gameOverScreen()

def showWalls():
    for i in range(0,600,wallSize):
        screen.blit(wallImage, (i,0))
        screen.blit(wallImage, (i,600 - wallSize))
        screen.blit(wallImage, (0, i))
        screen.blit(wallImage, (600 - wallSize, i))

def showScore(x,y,score):
    show = scoreFont.render('Score: ' + str(score), True, (0,0,0))
    screen.blit(show, (x,y))


def mainMenu():
    screen.fill((102, 102, 255))

    if continueGame:
        pygame.draw.rect(screen, (255, 204, 0), pygame.Rect(200,150,200,35))
        continueText = mainMenuFont.render('Continue', True, (0, 51, 0))
        screen.blit(continueText, (240,153))

    pygame.draw.rect(screen, (255, 204, 0), pygame.Rect(200,200,200,35))
    firstLevelText = mainMenuFont.render('First level', True, (0, 51, 0))
    screen.blit(firstLevelText, (240,203))

    pygame.draw.rect(screen, (255, 204, 0), pygame.Rect(200,250,200,35))
    secondLevelText = mainMenuFont.render('Second level', True, (0, 51, 0))
    screen.blit(secondLevelText, (240,253))

    pygame.draw.rect(screen, (255, 204, 0), pygame.Rect(200,300,200,35))
    thirdLevelText = mainMenuFont.render('Third level', True, (0, 51, 0))
    screen.blit(thirdLevelText, (240,303))

    pygame.draw.rect(screen, (255, 204, 0), pygame.Rect(200,350,200,35))
    exitText = mainMenuFont.render('Exit', True, (0, 51, 0))
    screen.blit(exitText, (280,353))
    pygame.display.update()


snake = Snake()
food = Food()
turn = True

while turn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if continueGame:
                
            turn = False
        if event.type == pygame.KEYDOWN:
            if snake.dx != -10:
                if event.key == pygame.K_RIGHT:
                    snake.dx = 10
                    snake.dy = 0
            if snake.dx != 10:
                if event.key == pygame.K_LEFT:
                    snake.dx = -10
                    snake.dy = 0
            if snake.dy != -10:
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 10
            if snake.dy != 10:
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -10
            if event.key == pygame.K_ESCAPE:
                if firstLevel:
                    firstLevel = False
                    mainMenuBool = True
                    continueGame = True
                    continueFirst = True
                if secondLevel:
                    secondLevel = False
                    mainMenuBool = True
                    continueGame = True
                    continueSecond = True
                if thirdLevel:
                    thirdLevel = False
                    mainMenuBool = True
                    continueGame = True
                    continueThird = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if continueGame:
                if (pos[0] in range(200,400)) and (pos[1] in range(150,185)):
                    time.sleep(0.5)
                    mainMenuBool = False
                    if continueFirst:
                        mainMenuBool = False
                        continueFirst = False
                        firstLevel = True
                    if continueSecond:
                        mainMenuBool = False
                        continueSecond = False
                        secondLevel = True
                    if continueThird:
                        mainMenuBool = False
                        continueThird = False
                        thirdLevel = True
            if (pos[0] in range(200,400)) and (pos[1] in range(200,235)):
                time.sleep(0.5)
                mainMenuBool = False
                firstLevel = True
                print(pos)
            if (pos[0] in range(200,400)) and (pos[1] in range(250,285)):
                time.sleep(0.5)
                mainMenuBool = False
                secondLevel = True
                print(pos)
            if (pos[0] in range(200,400)) and (pos[1] in range(300,335)):
                time.sleep(0.5)
                mainMenuBool = False
                thirdLevel = True
                print(pos)
            if (pos[0] in range(200,400)) and (pos[1] in range(350,385)):
                pygame.quit()
                print(pos)

    if mainMenuBool:
        mainMenu()

    if firstLevel:
        screen.fill((102, 102, 153))
        snake.move()
        snake.draw()
        food.draw()
        collision()
        showScore(15,15,snake.score)
        if snake.elements[0][0] < 0 or snake.elements[0][0] > 600:
            snake.elements[0][0] = snake.elements[0][0] % 600
        if snake.elements[0][1] < 0 or snake.elements[0][1] > 600:
            snake.elements[0][1] = snake.elements[0][1] % 600
        for i in range(1,snake.size):
            if snake.elements[0] == snake.elements[i]:
                time.sleep(1.5)
                screen.fill((255,0,0))
                screen.blit(gameOver,((600 - gameOver.get_width())/2, (600 - gameOver.get_height())/2))
                pygame.display.flip()
                time.sleep(5)
                snake.score = 0
                firstLevel = False
                mainMenuBool = True
                continueGame = False

        pygame.display.update()
        clock.tick(15)

    if secondLevel:
        screen.fill((102, 102, 153))
        snake.move()
        snake.draw()
        food.draw()
        collision()
        showScore(15,15,snake.score)
        showWalls()
        collisWall()
        for i in range(1,snake.size):
            if snake.elements[0] == snake.elements[i]:
                time.sleep(1.5)
                screen.fill((255,0,0))
                screen.blit(gameOver,((600 - gameOver.get_width())/2, (600 - gameOver.get_height())/2))
                pygame.display.flip()
                time.sleep(5)
                snake.score = 0
                secondLevel = False
                mainMenuBool = True
                continueGame = False
        pygame.display.update()
        clock.tick(25)
    if thirdLevel:
        screen.fill((102, 102, 153))
        snake.move()
        snake.draw()
        food.draw()
        collision()
        showScore(15,15,snake.score)
        showWalls()
        collisWall()
        for i in range(1,snake.size):
            if snake.elements[0] == snake.elements[i]:
                time.sleep(1.5)
                screen.fill((255,0,0))
                screen.blit(gameOver,((600 - gameOver.get_width())/2, (600 - gameOver.get_height())/2))
                pygame.display.flip()
                time.sleep(5)
                snake.score = 0
                thirdLevel = False
                mainMenuBool = True
                continueGame = False
        pygame.display.update()
        clock.tick(50)