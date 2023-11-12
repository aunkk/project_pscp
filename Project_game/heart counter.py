import pygame
import math
import requests
import random

pygame.init()
clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ghost Run To Hell 👻")

# define variables
run = True
game_over = False
flying = False
scroll_0 = 0
scroll_1 = 0
scroll_2 = 0
scroll_3 = 0
scroll_4 = 0
scroll_5 = 0
scroll_ground = 0
speed = 1
score = 0
hit = 0
font = pygame.font.Font("Project_game/media/PressStart2P-Regular.ttf", 10)
obstacle_freq = 2000 #milliseconds
last_obs = pygame.time.get_ticks() - obstacle_freq

# weather response and city
api_key = "e1c5932f6c96b34e1263878d1f8b7931"
city = "California"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
res = requests.get(url).json()
# weather = res['weather'][0]['main']
weather = "Clear"
city = "Tokyo"

# loads button images
button_img = pygame.image.load("project_game/media/restart.png")
button_img = pygame.transform.scale(button_img, (100, 50))

# load heart counter images
heart_img = []
for i in range(4):
    img = pygame.image.load(f"Project_game/media/heart-{i}.png").convert_alpha()
    # img = pygame.transform.scale(img, (125, 25))
    heart_img.append(img)

def select_bg(weather_res, city):
    """background images list selector"""
    if weather_res == "Clear":
        clear_bg = []
        for i in range(4):
            bg_image = pygame.image.load(f"project_game/media/clear-{i}.png").convert_alpha()
            clear_bg.append(bg_image)
        bg_images = clear_bg
    elif weather_res == "Clouds":
        cloud_bg = []
        for i in range(4):
            bg_image = pygame.image.load(f"project_game/media/cloud-{i}.png").convert_alpha()
            cloud_bg.append(bg_image)
        bg_images = cloud_bg
    elif weather_res == "Rain":
        rain_bg = []
        for i in range(4):
            bg_image = pygame.image.load(f"project_game/media/rain-{i}.png").convert_alpha()
            rain_bg.append(bg_image)
        bg_images = rain_bg
    else:
        clear_bg = []
        for i in range(4):
            bg_image = pygame.image.load(f"project_game/media/clear-{i}.png").convert_alpha()
            clear_bg.append(bg_image)
        bg_images = clear_bg

    if city == "Bangkok":
        for i in range(2):
            city_bg = pygame.image.load(f"project_game/media/thai-{i}.png").convert_alpha()
            bg_images.append(city_bg)
    elif city == "Tokyo":
        for i in range(2):
            city_bg = pygame.image.load(f"project_game/media/tokyo-{i}.png").convert_alpha()
            bg_images.append(city_bg)
    elif city == "Rome":
        for i in range(2):
            city_bg = pygame.image.load(f"project_game/media/rome-{i}.png").convert_alpha()
            bg_images.append(city_bg)

    return bg_images

def draw_background(bg_images, scroll_0, scroll_1, scroll_2, scroll_3, scroll_4, scroll_5):
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
    for i in range(0, tiles):
        screen.blit(bg_images[5], (i*800 + (scroll_5), 0))

def draw_foreground(scroll):
    tiles = math.ceil(SCREEN_WIDTH/800)+1

    foreground = pygame.image.load(f"project_game/media/platform.png").convert_alpha()
    for i in range(0, tiles):
        screen.blit(foreground, (i*800 + (scroll), 0))

def count_score():
    global score, font, speed, game_over, obstacle_freq
    if game_over == False:
        score += 1
        if score%500 == 0:
            speed += 0.5
        if speed > 3:
            obstacle_freq = 1500
        elif speed > 6:
            obstacle_freq = 1000
        elif speed > 9:
            obstacle_freq = 500

def draw_score(score):
    text = font.render("score: " + str(score), True, (0, 0, 0))
    screen.blit(text, (680, 18))

def draw_heart(heart_img):
    global hit, game_over
    if hit < 23:
        screen.blit(heart_img[3], (0, 0))
    elif hit < 46:
        screen.blit(heart_img[2], (0, 0))
    elif hit < 66:
        screen.blit(heart_img[1], (0, 0))
    else:
        screen.blit(heart_img[0], (0, 0))
        game_over = True

def reset_game():
    global score, speed, hit, heart
    obstacle_group.empty()
    player.rect.x = 75
    player.rect.y = 180
    score = 0
    speed = 1
    hit = 0

# Player
class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'project_game/media/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):

        if flying == True:
            #gravity
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
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)
            self.rect.y += 1

# obstacles
class obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("project_game/media/obstacle.png")
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.x -= speed+3
        if self.rect.right < 0:
            self.kill()

# restsrt button
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def draw(self):

        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check for mouse hover the button
        if self.rect.collidepoint(pos) == True:
            if pygame.mouse.get_pressed()[0] == True:
                action = True

        #draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

ghost_group = pygame.sprite.Group()
obstacle_group = pygame.sprite.Group()

player = Ghost(100, 205)
ghost_group.add(player)

button = Button(SCREEN_WIDTH//2-10, SCREEN_HEIGHT//2, button_img)

while run:
    if game_over == False and flying == True:
        scroll_0 -= speed
        scroll_1 -= speed+0.2
        scroll_2 -= speed+0.5
        scroll_3 -= speed+0.8
        scroll_4 -= speed+1.1
        scroll_5 -= speed+1.4
        scroll_ground -= speed+3
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
        elif abs(scroll_5) > 800:
            scroll_5 = 0
        elif abs(scroll_ground) > 800:
            scroll_ground = 0

        #count score
        count_score()

        # obstacles random spawn
        time_now = pygame.time.get_ticks()
        if time_now - last_obs > obstacle_freq:
            grave = obstacle(SCREEN_WIDTH + random.randrange(300, 900, 100), 210)
            obstacle_group.add(grave)
            last_obs = time_now
        obstacle_group.update()

    scenes = select_bg(weather, city)
    # draw background
    draw_background(scenes, scroll_0, scroll_1, scroll_2, scroll_3, scroll_4, scroll_5)

    # draw obstacles
    obstacle_group.draw(screen)

    # draw player
    ghost_group.draw(screen)
    ghost_group.update()

    # draw ground
    draw_foreground(scroll_ground)

    # draw score counter
    draw_score(score)

    # draw heart counter
    draw_heart(heart_img)

    #look for collision
    if pygame.sprite.groupcollide(ghost_group, obstacle_group, False, False) or player.rect.top < 0:
        hit += 1

    # check for game over and reset
    if game_over == True:
        key_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_pressed = True
            if event.type == pygame.QUIT:
                run = False
        if button.draw() == True or key_pressed == True:
            game_over = False
            reset_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and flying == False and game_over == False:
            flying = True

    pygame.display.update()
pygame.quit()