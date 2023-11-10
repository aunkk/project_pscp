import pygame
import math

# from pygame.sprite import _Group

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 300
FPS = 60

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

    def update(self):
        self.counter += 1
        flap_cooldown = 15
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]

bird_group = pygame.sprite.Group()

flappy = Bird(100, 200)

bird_group.add(flappy)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ghost Run To Hell 👻")
bg = pygame.image.load("game\media\city_test.png").convert_alpha()
bg_width = bg.get_width()

def draw_bg(scroll):
    tiles = math.ceil(SCREEN_WIDTH/bg_width)+1
    for i in range(0, tiles):
        screen.blit(bg, (i*bg_width + scroll, 0))

clock = pygame.time.Clock()
scroll = 0
run = True
while run == True:
    clock.tick(FPS)
    scroll -= 3
    if abs(scroll) > bg_width:
        scroll = 0
    draw_bg(scroll)

    bird_group.draw(screen)
    bird_group.update()

    # key = pygame.key.get_pressed()
    # if key[pygame.K_LEFT] == True and scroll > 0:
    #     scroll -= 3
    # if key[pygame.K_RIGHT] == True:
    #     scroll +=3

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()