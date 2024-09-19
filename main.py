import pygame
import time
import random
pygame.font.init()

ScreenWidth = 1000
ScreenHeight = 800
Screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("Avoid The Rain")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"),(ScreenWidth, ScreenHeight)).convert()

PlayerWidth = 40
PlayerHeight = 60
PlayerVelocity = 5
RainVelocity = 7
Font = pygame.font.SysFont("comicsans", 30)
RainWidth = 9
RainHeight = 11

def draw(player, elapsedTime, rainDrops):
    Screen.blit(BG, (0,0))

    time_text = Font.render(f"Time: {round(elapsedTime)}s", 1, "white")
    Screen.blit(time_text, (10,10))

    pygame.draw.rect(Screen, "purple", player)

    for rainDrop in rainDrops:
        pygame.draw.rect(Screen, "yellow", rainDrop)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, ScreenHeight - PlayerHeight,
                         PlayerWidth, PlayerHeight)
    
    clock = pygame.time.Clock()
    startTime = time.time()
    elapsedTime = 0
    rainAddTime = 2000
    rainCount = 0
    rainDrops = []
    hit = False

    while run:
        rainCount += clock.tick(60)
        elapsedTime = time.time() - startTime

        if rainCount > rainAddTime:
            for _ in range(3):
                rainX = random.randint(0, ScreenWidth - RainWidth)
                rainDrop = pygame.Rect(rainX, -RainHeight, RainWidth, RainHeight)
                rainDrops.append(rainDrop)
            
            rainAddTime = max(200, rainAddTime-50)
            rainCount = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x + PlayerWidth*0.2 >0:
            player.x -= PlayerVelocity
        if keys[pygame.K_RIGHT] and player.x + PlayerWidth*0.8 < ScreenWidth:
            player.x += PlayerVelocity
        # if keys[pygame.K_UP]:
        #     player.y -= PlayerVelocity
        # if keys[pygame.K_DOWN]:
        #     player.y -= PlayerVelocity

        for rainDrop in rainDrops[:]:
            rainDrop.y += RainVelocity
            if rainDrop.y > ScreenHeight:
                rainDrops.remove(rainDrop)
            elif rainDrop.y >= player.y and rainDrop.colliderect(player):
                rainDrops.remove(rainDrop)
                hit = True
                break
        
        if hit:
            lostText = Font.render("Game Over", 1, "yellow")
            Screen.blit(lostText, (ScreenWidth/2 - lostText.get_width()/2, ScreenHeight/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break


        draw(player, elapsedTime, rainDrops)
    
    pygame.quit()

if __name__ == "__main__":
    main()