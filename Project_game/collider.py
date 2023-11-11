import pygame
import math


pygame.init()
clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ghost Run To Hell 👻")

# define variables
scroll_0 = 0
scroll_ground = 0
speed = 1
flying = False
game_over = False
obstacle_freq = 2000 #milliseconds
last_obs = pygame.time.get_ticks() - obstacle_freq

run = True

bg_image = pygame.image.load("Project_game/media/city_test.png").convert_alpha()


def draw_background(bg_image, scroll_0):
    tiles = math.ceil(SCREEN_WIDTH/800)+1

    for i in range(0, tiles):
        screen.blit(bg_image, (i*800 + scroll_0, 0))


def draw_foreground(scroll):
    tiles = math.ceil(SCREEN_WIDTH/800)+1

    foreground = pygame.image.load(f"Project_game/media/platform.png").convert_alpha()
    for i in range(0, tiles):
        screen.blit(foreground, (i*800 + (scroll), 0))


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'Project_game/media/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):
        #gravity
        if flying == True:
            self.vel += 0.4
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 220:
                self.rect.y += int(self.vel)

        if game_over == False:
            # jumping
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_SPACE] == True and self.clicked == False and self.rect.top > 100:
                self.clicked == True
                self.vel = -8
                self.rect.y += int(self.vel)
                # self.rect.x += 10
            if key_pressed[pygame.K_SPACE] == False:
                self.clicked = False

            # animation
            self.counter += 1
            flap_cooldown = 15
            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

        # rotate
        # self.image = pygame.transform.rotate(self.images[self.index], self.vel)

        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)
            self.rect.y += 1

class obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Project_game/media/obstacle.png")
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.x -= speed+4
        if self.rect.right < 0:
            self.kill()


bird_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()

flappy = Bird(100, 205)

bird_group.add(flappy)

# add obstacle
# grave = obstacle(500, 220)
# obstacle_group.add(grave)

while run:
    clock.tick(FPS)

    # draw background
    draw_background(bg_image, scroll_0)
    

    # draw player
    bird_group.draw(screen)
    bird_group.update()

    # draw obstacles
    obstacle_group.draw(screen)

    # draw ground
    draw_foreground(scroll_ground)

    # check for bird hit ground
    # if flappy.rect.bottom > 205:
    #     game_over = True
    #     flying = False

    #look for collision
    if pygame.sprite.groupcollide(bird_group, obstacle_group, False, False) or flappy.rect.top < 0:
        game_over = True



    # make endless scrolling
    # scroll_0 -= speed
    # scroll_ground -= speed+4
    # if abs(scroll_0) > 800:
    #     scroll_0 = 0
    # elif abs(scroll_ground) > 800:
    #     scroll_ground = 0

    if game_over == False:
        # make endless scrolling
        scroll_0 -= speed
        scroll_ground -= speed+4
        if abs(scroll_0) > 800:
            scroll_0 = 0
        elif abs(scroll_ground) > 800:
            scroll_ground = 0

        time_now = pygame.time.get_ticks()
        if time_now - last_obs > obstacle_freq:
            grave = obstacle(SCREEN_WIDTH, 220)
            obstacle_group.add(grave)
            last_obs = time_now
        obstacle_group.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and flying == False and game_over == False:
            flying = True

    pygame.display.update()
pygame.quit()