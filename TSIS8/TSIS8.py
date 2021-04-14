#Game
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
        image = pygame.image.load("./materials/coin.png")
        images[path] = image
    return image
playerImage = pygame.image.load('./materials/Player.png')
playerWidth = playerImage.get_width()
playerHeight = playerImage.get_height()
enemyImage = pygame.image.load("./materials/Enemy.png")
enemyWidth = enemyImage.get_width()
enemyHeight = enemyImage.get_height()
coinImage = get_image("./materials/coin.png")
coinImage = pygame.transform.scale(coinImage, (50,50))
coinWidth = coinImage.get_width()
coinHeight = coinImage.get_height()
streetImage = pygame.image.load("./materials/AnimatedStreet.png")
streetWidth = streetImage.get_width()
streetHeight = streetImage.get_height()


#main Settings
screen = pygame.display.set_mode((streetWidth, streetHeight))
pygame.display.set_caption("My first game")


#Booleans
repeatMusic = True
turn = True
coin = False


#Variables
step = 5
score = 0

playerX = 0
playerY = streetHeight - playerHeight - 15

enemyX = random.randint(40, streetWidth - enemyWidth - 40)
enemyY = 0 - enemyHeight

coinX = random.randint(40, streetWidth - 40)
coinY = 0 - coinHeight


#Texts
font = pygame.font.SysFont("Helvetica", 60)
smallFont = pygame.font.SysFont("Myraid Pro", 30)
gameOver = font.render("Game Over", True, (0,0,0))



#Clock and FPS
FPS = 60
clock = pygame.time.Clock()


#Functions
def enemyMove(x,y):
    global enemyY
    global enemyX
    global score
    global step
    if enemyY > streetHeight + enemyHeight:
        enemyY = 0 - enemyHeight
        enemyX = random.randint(40, streetWidth - enemyWidth - 40)
        score += 1
        step = random.randint(4,9)
    enemyY += step
def showScore(x,y):
    scoreText = smallFont.render("SCORE: " + str(score), True, (0,0,255))
    screen.blit(scoreText, (x,y))
def isCrash(x,y,xx,yy):
    if (x in range(xx + 5, xx + enemyWidth - 5)) or (xx in range(x + 5, x + playerWidth - 5)) :
        if (y in range(yy + 5, yy + enemyHeight - 5)) or (yy in range(y + 5, y + playerHeight - 5)):
            return True
def coinSpawn():
    global coin
    global coinX
    global coinY
    global step

    if not coin:
        spawn = random.randint(0,1000)
        if spawn == 5:
            coin = True
            coinX = random.randint(40, streetWidth - 40)
    if coin:
        screen.blit(coinImage, (coinX, coinY))
        coinY += step
    if coinY > coinHeight + streetHeight:
        coin = False
        coinY = 0 - coinHeight



#Programm start
while turn:
    if playerX in range(coinX, coinX + coinWidth) or coinX in range(playerX, playerX + playerWidth):
        if playerY in range(coinY, coinY + coinHeight) or coinY in range(playerY, playerY + playerHeight):
            coin = False
            coinY = 0 - coinHeight
            score += 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            turn = False

    #Turning music
    if repeatMusic:
        pygame.mixer.Sound('./materials/background.wav').play()
        repeatMusic = False


    #Pressed keys
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: playerX -= step
    if pressed[pygame.K_RIGHT]: playerX += step
    if playerX + playerWidth < 0 or playerX > streetWidth:
        playerX = playerX % streetWidth
    if isCrash(playerX, playerY, enemyX, enemyY):
        pygame.mixer.Sound('./materials/crash.wav').play()
        time.sleep(1)
        screen.fill((255,0,0))
        screen.blit(gameOver,((streetWidth - gameOver.get_width())/2, (screen.get_height() - gameOver.get_height())/2))
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
    
    #MARK: - Final 
    pygame.display.flip()
    screen.blit(streetImage, (0,0))
    enemyMove(enemyX,enemyY)
    pygame.draw.rect(screen, (128,128,128), pygame.Rect(270 , 2, 130, 20))
    showScore(275, 3)
    coinSpawn()
    screen.blit(playerImage, (playerX, playerY))
    screen.blit(enemyImage, (enemyX, enemyY))
    clock.tick(FPS)