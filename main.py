import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid Rain")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"),(WIDTH, HEIGHT)).convert()

PlayerWidth = 40
PlayerHeight = 60
PlayerVelocity = 5
Font = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsedTime):
    WIN.blit(BG, (0,0))

    pygame.draw.rect(WIN, "purple", player)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PlayerHeight,
                         PlayerWidth, PlayerHeight)
    
    clock = pygame.time.Clock()
    startTime = time.time()
    elapsedTime = 0

    while run:
        clock.tick(60)
        elapsedTime = time.time() - startTime

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x + PlayerWidth*0.2 >0:
            player.x -= PlayerVelocity
        if keys[pygame.K_RIGHT] and player.x + PlayerWidth*0.8 < WIDTH:
            player.x += PlayerVelocity
        # if keys[pygame.K_UP]:
        #     player.y -= PlayerVelocity
        # if keys[pygame.K_DOWN]:
        #     player.y -= PlayerVelocity

        draw(player, elapsedTime)
    
    pygame.quit()

if __name__ == "__main__":
    main()