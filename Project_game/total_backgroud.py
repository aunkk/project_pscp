import pygame
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ghost Run To Hell 👻")

# BACKGROUND

def draw_bg(weather_res, city, scroll):
    if weather_res == "clear":
        clear_bg = []
        for i in range(4):
            bg_image = pygame.image.load(f"game/media/clear-{i}.png").convert_alpha()
            clear_bg.append(bg_image)
        bg_images = clear_bg
    elif weather_res == "cloud":
        cloud_bg = []
        for i in range(4):
            bg_image = pygame.image.load(f"game/media/cloud-{i}.png").convert_alpha()
            cloud_bg.append(bg_image)
        bg_images = cloud_bg
    elif weather_res == "rain":
        rain_bg = []
        for i in range(3):
            bg_image = pygame.image.load(f"game/media/rain-{i}.png").convert_alpha()
            rain_bg.append(bg_image)
        bg_images = rain_bg


    building = pygame.image.load(f"game/media/buildings.png").convert_alpha()
    bg_images.append(building)

    if weather_res == "rain":
        x = pygame.image.load(f"game/media/rain-{3}.png").convert_alpha()
        rain_bg.append(x)


    if city == "tokyo":
        city_bg = pygame.image.load(f"game/media/tokyo.png").convert_alpha()
        bg_images.append(city_bg)
    elif city == "italy":
        city_bg = pygame.image.load(f"game/media/italy.png").convert_alpha()
        bg_images.append(city_bg)
    elif city == "singapore":
        city_bg = pygame.image.load(f"game/media/merlion.png").convert_alpha()
        bg_images.append(city_bg)

    

    bg_width = bg_images[0].get_width()
    for i in range(999):
        speed = 0.5
        for bg in bg_images:
            screen.blit(bg, ((i*bg_width) - scroll*speed, 0))
            speed += 0.15

def draw_foreground(scroll):
    foreground = pygame.image.load(f"game/media/platform.png").convert_alpha()
    fg_width = foreground.get_width()
    fg_height = foreground.get_height()
    for i in range(999):
        screen.blit(foreground, ((i*fg_width) - scroll * 1.5, SCREEN_HEIGHT - fg_height))

def main():
    """GAME LOOP"""
    clock = pygame.time.Clock()
    scroll = 0
    run = True
    while run == True:
        clock.tick(FPS)
        draw_bg("clear", "singapore", scroll)
        draw_foreground(scroll)

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] == True and scroll > 0:
            scroll -= 3
        if key[pygame.K_RIGHT] == True:
            scroll += 3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()

# if __name__ == "__main__":
#     main(screen)

main()
