import pygame
import random
import math

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

#game background
background = pygame.image.load('game background 2.jpg')

# title and icon
pygame.display.set_caption("Manta ghost killer!")
icon = pygame.image.load('logoipsumicon.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('manta-ray2.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# ghostEnemy
GhostImg = []
ghostX = []
ghostY = []
ghostX_change = []
ghostY_change = []
number_Of_Ghosts = 6

for i in range (number_Of_Ghosts):
    GhostImg.append(pygame.image.load('hauntingicon.png'))
    ghostX.append(random.randint(0,736))
    ghostY.append(random.randint(50,100))
    ghostX_change.append(3)
    ghostY_change.append(40)

#bullet
#ready means you can't see it on the screen, fire means you can
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = .5
bullet_State = "ready"

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


def ghost(x, y, i):
    screen.blit(GhostImg[i], (x, y))

def fire_bullet(x,y):
    global bullet_State
    bullet_State = "fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(ghostX,ghostY,bulletX,bulletY):
    distance = math.sqrt((math.pow(ghostX - bulletX, 2)) + (math.pow(ghostY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# game loop
running = True
while running:

    # RGB -Red,Green, Blue
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            # if keystroke is pressed check whether it's left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_UP:
                playerY_change = -0.3
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_State is "ready":
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(playerX,playerY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerX_change = 0
                playerY_change = 0



    #player movement boundaries
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    playerY += playerY_change

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    #ghost movement boundaries
    for i in range (number_Of_Ghosts):
        ghostX[i] += ghostX_change[i]

        if ghostX[i] <= 0:
            ghostX_change[i] = 0.3
            ghostY[i] += ghostY_change[i]
        elif ghostX[i] >= 736:
            ghostX_change[i] = -0.3

        # collision
        collision = isCollision(ghostX[i], ghostY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_State = "ready"
            score += 1
            print(score)
            ghostX[i] = random.randint(0, 735)
            ghostY[i] = random.randint(50, 150)

        ghost(ghostX[i], ghostY[i],i)

    #bullet movement
    if bulletY <=0 :
        bulletY =480
        bullet_State = "ready"

    if bullet_State is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)


    pygame.display.update()
