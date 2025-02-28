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

def draw(player, elapsed_time, rain_drops):
    Screen.blit(BG, (0,0))

    time_text = Font.render(f"Time: {round(elapsed_time)}s", 1, "white")
    Screen.blit(time_text, (10,10))

    pygame.draw.rect(Screen, "purple", player)

    for rain_drop in rain_drops:
        pygame.draw.rect(Screen, "yellow", rain_drop)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, ScreenHeight - PlayerHeight,
                         PlayerWidth, PlayerHeight)
    
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    rain_add_time = 2000
    rain_count = 0
    rain_drops = []
    hit = False

    while run:
        rain_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if rain_count > rain_add_time:
            for _ in range(4): # 4 rain drops
                rainX = random.randint(0, ScreenWidth - RainWidth)
                rain_drop = pygame.Rect(rainX, -RainHeight, RainWidth, RainHeight)
                rain_drops.append(rain_drop)
            
            rain_add_time = max(200, rain_add_time-50) # increase rain drop speed
            rain_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x + PlayerWidth*0.2 >0:
            player.x -= PlayerVelocity
        if keys[pygame.K_RIGHT] and player.x + PlayerWidth*0.8 < ScreenWidth:
            player.x += PlayerVelocity
        if keys[pygame.K_a] and player.x + PlayerWidth*0.2 >0:
            player.x -= PlayerVelocity
        if keys[pygame.K_d] and player.x + PlayerWidth*0.8 < ScreenWidth:
            player.x += PlayerVelocity
        # if keys[pygame.K_UP]:
        #     player.y -= PlayerVelocity
        # if keys[pygame.K_DOWN]:
        #     player.y -= PlayerVelocity

        for rain_drop in rain_drops[:]:
            rain_drop.y += RainVelocity
            if rain_drop.y > ScreenHeight:
                rain_drops.remove(rain_drop)
            elif rain_drop.y >= player.y and rain_drop.colliderect(player):
                rain_drops.remove(rain_drop)
                hit = True
                break
        
        if hit:
            lost_text = Font.render("Game Over", 1, "yellow")
            Screen.blit(lost_text, (ScreenWidth/2 - lost_text.get_width()/2, ScreenHeight/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break


        draw(player, elapsed_time, rain_drops)
    
    pygame.quit()

if __name__ == "__main__":
    main()