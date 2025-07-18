import pygame

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("DMX_It's not....A...GAME!")
icon=pygame.image.load('logoipsumicon.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('manta-ray2.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change =0

def player(x,y):
    screen.blit(playerImg, (x, y))

#game loop
running = True
while running :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False

            # if keystroke is pressed check whether it's left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                playerY_change = 5

        if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key== pygame.K_DOWN or event.key== pygame.K_UP:
                    playerX_change = 0


         # RGB -Red,Green, Blue
        screen.fill((0, 0, 128))

        playerX += playerX_change
        playerY += playerY_change
        player(playerX, playerY)
        pygame.display.update()







