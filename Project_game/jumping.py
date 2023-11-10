import pygame
import math

pygame.init()
clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ghost Run To Hell 👻")

def select_bg(weather_res, city):
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

    if city == "bangkok":
        city_bg = pygame.image.load(f"game/media/buildings.png").convert_alpha()
        bg_images.append(city_bg)
    elif city == "italy":
        city_bg = pygame.image.load(f"game/media/italy.png").convert_alpha()
        bg_images.append(city_bg)
    elif city == "singapore":
        city_bg = pygame.image.load(f"game/media/merlion.png").convert_alpha()
        bg_images.append(city_bg)

    return bg_images

def draw_background(bg_images, scroll_0, scroll_1, scroll_2, scroll_3, scroll_4):
    tiles = math.ceil(SCREEN_WIDTH/800)+1

    for i in range(0, tiles):
        screen.blit(bg_images[0], (i*800 + scroll_0, 0))
    for i in range(0, tiles):
        screen.blit(bg_images[1], (i*800 + (scroll_1), 0))
    for i in range(0, tiles):
        screen.blit(bg_images[2], (i*800 + (scroll_2), 0))
    for i in range(0, tiles):
        screen.blit(bg_images[3], (i*800 + (scroll_3), 0))
    for i in range(0, tiles):
        screen.blit(bg_images[4], (i*800 + (scroll_4), 0))

def draw_foreground(scroll):
    tiles = math.ceil(SCREEN_WIDTH/800)+1

    foreground = pygame.image.load(f"game/media/platform.png").convert_alpha()
    for i in range(0, tiles):
        screen.blit(foreground, (i*800 + (scroll), 0))

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'game/media/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):
        self.vel += 0.5
        if self.vel > 8:
            self.vel = 8
        if self.rect.bottom < 220:
            self.rect.y += int(self.vel)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE] == True and self.clicked == False and self.rect.top > 100:
            self.clicked == True
            self.vel = -8
            self.rect.y += int(self.vel)
        if key_pressed[pygame.K_SPACE] == False:
            self.clicked = False


        self.counter += 1
        flap_cooldown = 15
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]

def main():
    # game loop
    run = True

    #define variables
    scroll_0 = 0
    scroll_1 = 0
    scroll_2 = 0
    scroll_3 = 0
    scroll_4 = 0
    scroll_ground = 0
    speed = 1.5

    bird_group = pygame.sprite.Group()

    y_position = 205
    flappy = Bird(100, y_position)

    bird_group.add(flappy)

    while run:
        clock.tick(FPS)
        scroll_0 -= speed
        scroll_1 -= speed+0.2
        scroll_2 -= speed+0.5
        scroll_3 -= speed+0.8
        scroll_4 -= speed+1.1
        scroll_ground -= speed+1.5
        if abs(scroll_0) > 800:
            scroll_0 = 0
        elif abs(scroll_1) > 800:
            scroll_1 = 0
        elif abs(scroll_2) > 800:
            scroll_2 = 0
        elif abs(scroll_3) > 800:
            scroll_3 = 0
        elif abs(scroll_4) > 800:
            scroll_4 = 0
        elif abs(scroll_ground) > 800:
            scroll_ground = 0
        scenes = select_bg("clear", "bangkok")
        draw_background(scenes, scroll_0, scroll_1, scroll_2, scroll_3, scroll_4)
        draw_foreground(scroll_ground)

        bird_group.draw(screen)
        bird_group.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

main()
