import pygame
import math
import requests
import random
import os

pygame.init()
clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ghost Run To Hell 👻")

############# main menu #############
def menu():
    WIDTH, HEIGHT = 800, 300
    WHITE = (255, 255, 255)
    BUTTON_COLOR = (133, 222, 108)
    BUTTON_COLOR1 = (255, 99, 71)
    TEXT_COL = (77, 44, 255)
    BLACK = (0, 0, 0)
    SCREEN_MAIN = (100, 50, 98)
    pygame.display.set_caption("Game Menu")
    center_x = screen.get_rect().centerx
    center_y = screen.get_rect().centery + 10

    custom_font1 = pygame.font.FontType("assets/PressStart2P-Regular.ttf", 30)
    # Create a window

    bg = pygame.image.load("assets/background_sign.png").convert_alpha()
    game_name = pygame.image.load("assets/game_name.png").convert_alpha()
    game_rect = game_name.get_rect(center=(center_x, center_y-50))
    start_img = pygame.image.load("assets/start_button.png").convert_alpha()
    start_img = pygame.transform.scale(start_img, (171/1.5, 68/1.5))
    exit_img = pygame.image.load("assets/exit_button.png").convert_alpha()
    exit_img = pygame.transform.scale(exit_img, (143/1.5, 69/1.5))


    def draw_text(text, font_type, text_color, x, y):
        img = font_type.render(text, True, text_color)
        screen.blit(img, (x, y))

    # bg_rect = bg.get_rect(center = (center_x, center_y))
    start_rect = start_img.get_rect(center=(center_x, center_y))
    exit_rect = exit_img.get_rect(center=(center_x,  center_y+70))


    class Button():
        def __init__(self, x, y, image, scale):
            width = image.get_width()#get to func sth
            height = image.get_height()
            self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
            self.rect = self.image.get_rect()
            self.rect.topleft = (x, y)
            self.Clicked = False

        # create button
        def mouse_position(self, surface):

            action = False

            # get mouse position
            pos = pygame.mouse.get_pos()

            # check for mouse hover the button
            if self.rect.collidepoint(pos) == True:
                if pygame.mouse.get_pressed()[0] == True:
                    action = True

            #draw button
            surface.blit(self.image, (self.rect.x, self.rect.y))

            return action


    ################################################################################################

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_rect.collidepoint(cursor_ckeck):
                        # Start the game (add your game code here)
                        print("Starting the game!")
                        # Desktop/project_pscp-main/project_pscp-1/no main
                        # os.system("python Project_game/complete_project/Project_game/gameplay.py")
                        choose_city()
                        running = False
                    elif exit_rect.collidepoint(cursor_ckeck):
                        print("Get out")
                        running = False
            else:
                draw_text("Ghost run to hell", custom_font1, TEXT_COL, 350, 50)

        cursor_ckeck = pygame.mouse.get_pos()

        screen.fill(SCREEN_MAIN)
        screen.blit(bg, (screen.get_rect()))
        screen.blit(start_img, start_rect.topleft)
        screen.blit(exit_img, exit_rect.topleft)
        screen.blit(game_name, (screen.get_rect()))
        pygame.display.update()

########## choose city ##########
def choose_city():
    global city, game_over, flying
    game_over = False
    flying = False
    reset_game()

    running = True
    city_name = "Choose your city!"

    center_y = (screen.get_rect().centery)-10
    center_x = (screen.get_rect().centerx)
    alpha_value = 165

    bangkok_img = pygame.image.load("assets/Bangkok_box.png")
    bangkok_img = pygame.transform.scale(bangkok_img, (300/2, 300/2))
    bangkok_rect = bangkok_img.get_rect(center = (center_x - 200, center_y - 0))
    bang_name = pygame.image.load("assets/Bangkok_sign.png")
    bang_name = pygame.transform.scale(bang_name, (297/(2.5*1.05), 51/(2.5*1.05)))
    bang_rect = bang_name.get_rect(center = (center_x - 200, center_y + 80))
    bangkok_img.set_alpha(alpha_value)
    bang_name.set_alpha(alpha_value)

    italy_img = pygame.image.load("assets/Italy_box.png")
    italy_img = pygame.transform.scale(italy_img, (300/2, 300/2))
    italy_rect = italy_img.get_rect(center = (center_x, center_y - 0))
    italy_name = pygame.image.load("assets/rome_sign.png")
    italy_name = pygame.transform.scale(italy_name, (288/(4.25*1.05), 80/(4*1.05)))
    italy_n_rect = italy_name.get_rect(center = (center_x, center_y + 80))
    italy_img.set_alpha(alpha_value)
    italy_name.set_alpha(alpha_value)

    tokyo_img = pygame.image.load("assets/Tokyo_box.png")
    tokyo_img = pygame.transform.scale(tokyo_img, (300/2, 300/2))
    tokyo_rect = tokyo_img.get_rect(center = (center_x + 200, center_y - 0))
    tokyo_name = pygame.image.load("assets/tokyo_sign.png")
    tokyo_name = pygame.transform.scale(tokyo_name, (279/(3.5*1.05), 70/(3.5*1.05)))
    tokyo_n_rect = tokyo_name.get_rect(center  = (center_x + 200, center_y + 80))
    tokyo_img.set_alpha(alpha_value)
    tokyo_name.set_alpha(alpha_value)

    play_img = pygame.image.load("assets/play.png")
    play_img = pygame.transform.scale(play_img, (157/1.5, 68/1.5))# 157x68
    play_rect = play_img.get_rect(center = (center_x, center_y+120))
    play_img.set_alpha(255)

    # font = pygame.font.FontType("assets/Pixgamer.ttf", 36)
    font = pygame.font.FontType("assets/PressStart2P-Regular.ttf", 32)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if italy_rect.collidepoint(my_mouse):
                        italy_img.set_alpha(255)
                        tokyo_img.set_alpha(alpha_value)
                        bangkok_img.set_alpha(alpha_value)

                        bang_name.set_alpha(alpha_value)
                        italy_name.set_alpha(255)
                        tokyo_name.set_alpha(alpha_value)
                        city_name = "Rome"
                        # print(italy_rect)
                    elif tokyo_rect.collidepoint(my_mouse):
                        italy_img.set_alpha(alpha_value)
                        tokyo_img.set_alpha(255)
                        bangkok_img.set_alpha(alpha_value)

                        bang_name.set_alpha(alpha_value)
                        italy_name.set_alpha(alpha_value)
                        tokyo_name.set_alpha(255)
                        city_name = "Tokyo"
                    elif bangkok_rect.collidepoint(my_mouse):
                        italy_img.set_alpha(alpha_value)
                        tokyo_img.set_alpha(alpha_value)
                        bangkok_img.set_alpha(255)

                        bang_name.set_alpha(255)
                        italy_name.set_alpha(alpha_value)
                        tokyo_name.set_alpha(alpha_value)
                        city_name = "Bangkok"
                    elif play_rect.collidepoint(my_mouse):
                        play_img.set_alpha(alpha_value)
                        #os.system("python project_game/change_color_button.py")
                        running = False
                        city = city_name
                        main(city_name)
                    else:
                        italy_img.set_alpha(alpha_value)
                        tokyo_img.set_alpha(alpha_value)
                        bangkok_img.set_alpha(alpha_value)
                        city_name = "Choose your city!"
                        bang_name.set_alpha(alpha_value)
                        italy_name.set_alpha(alpha_value)
                        tokyo_name.set_alpha(alpha_value)

            else:
                if city_name == "Choose your city!":
                    play_img.set_alpha(alpha_value)
                else:
                    play_img.set_alpha(255)

        my_mouse = pygame.mouse.get_pos()
        # print(my_mouse)

        text = font.render(f"{city_name}", True, (255, 255, 255))
        text_rect = text.get_rect(center=(center_x, center_y - 107))

        screen.fill((100, 50, 98))
        # bangkok_bg.fill((255, 255, 255))
        # screen.blit(bangkok_bg, bangkok_rect.topleft)

        screen.blit(text, text_rect.topleft)
        screen.blit(italy_img, italy_rect.topleft)
        screen.blit(italy_name, italy_n_rect.topleft)
        screen.blit(bangkok_img, bangkok_rect.topleft)
        screen.blit(bang_name, bang_rect.topleft)
        screen.blit(tokyo_img, tokyo_rect.topleft)
        screen.blit(tokyo_name, tokyo_n_rect.topleft)
        screen.blit(play_img, play_rect.topleft)

        pygame.display.update()


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
highest_score = 0
hit = 0
font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 10)
obstacle_freq = 2000 #milliseconds
last_obs = pygame.time.get_ticks() - obstacle_freq


# loads button images
restart_button_img = pygame.image.load("assets/restart_button.png")
restart_button_img = pygame.transform.scale(restart_button_img, (110, 55))
exit_button_img = pygame.image.load("assets/exit_button.png")
exit_button_img = pygame.transform.scale(exit_button_img, (95, 45))
menu_button_img = pygame.image.load("assets/menu_button.png")
menu_button_img = pygame.transform.scale(menu_button_img, (100, 50))

# load heart counter images
heart_img = []
for i in range(4):
    img = pygame.image.load(f"assets/heart-{i}.png").convert_alpha()
    img = pygame.transform.scale(img, (667, 250))
    heart_img.append(img)

# loads sound effect
jump_sfx = pygame.mixer.Sound("assets/jump.mp3")
hit_sfx = pygame.mixer.Sound("assets/hit.mp3")
game_start_sfx = pygame.mixer.Sound("assets/start game.mp3")
game_over_sfx = pygame.mixer.Sound("assets/game over.mp3")

def select_bg(weather_res, city):
    """background images list selector"""
    if weather_res == "Clear":
        clear_bg = []
        for i in range(4):
            bg_image = pygame.image.load(f"assets/clear-{i}.png").convert_alpha()
            clear_bg.append(bg_image)
        bg_images = clear_bg
    elif weather_res == "Clouds":
        cloud_bg = []
        for i in range(4):
            bg_image = pygame.image.load(f"assets/cloud-{i}.png").convert_alpha()
            cloud_bg.append(bg_image)
        bg_images = cloud_bg
    elif weather_res == "Rain":
        rain_bg = []
        for i in range(4):
            bg_image = pygame.image.load(f"assets/rain-{i}.png").convert_alpha()
            rain_bg.append(bg_image)
        bg_images = rain_bg
    else:
        clear_bg = []
        for i in range(4):
            bg_image = pygame.image.load(f"assets/clear-{i}.png").convert_alpha()
            clear_bg.append(bg_image)
        bg_images = clear_bg

    if city == "Bangkok":
        for i in range(2):
            city_bg = pygame.image.load(f"assets/thai-{i}.png").convert_alpha()
            bg_images.append(city_bg)
    elif city == "Tokyo":
        for i in range(2):
            city_bg = pygame.image.load(f"assets/tokyo-{i}.png").convert_alpha()
            bg_images.append(city_bg)
    elif city == "Rome":
        for i in range(2):
            city_bg = pygame.image.load(f"assets/rome-{i}.png").convert_alpha()
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

    foreground = pygame.image.load(f"assets/platform.png").convert_alpha()
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
    text = font.render("pt %06d" %score, True, (0, 0, 0))
    screen.blit(text, (680, 18))

def higher(val1, val2):
    if val1 > val2:
        return val1
    return val2

def draw_highest_score():
    global score, highest_score
    highest_score = higher(highest_score, score)
    text = font.render("hi %06d" %highest_score, True, (0, 0, 0))
    screen.blit(text, (680, 40))

def draw_heart(heart_img):
    global hit, game_over, city, weather
    text = font.render("%s's weather is %s" %(city, weather), True, (0, 0, 0))
    screen.blit(text, (18, 18))
    if hit < 23:
        screen.blit(heart_img[3], (5, 15))
    elif hit < 46:
        screen.blit(heart_img[2], (5, 15))
    elif hit < 66:
        screen.blit(heart_img[1], (5, 15))
    else:
        screen.blit(heart_img[0], (5, 15))
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
            img = pygame.image.load(f'assets/ghost{num}.png')
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
            if key_pressed[pygame.K_SPACE] == True:
                jump_sfx.play()
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
            if self.rect.y < 250:
                game_over_sfx.play()

# obstacles
class obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/obstacle.png")
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.x -= speed+3
        if self.rect.right < 0:
            self.kill()

# restart button
class RestartButton():
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

# exit button
class ExitButton():
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

# menu button
class MenuButton():
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

restart_button = RestartButton(SCREEN_WIDTH//2-10, SCREEN_HEIGHT//2-53, restart_button_img)
menu_button = MenuButton(SCREEN_WIDTH//2-10, SCREEN_HEIGHT//2, menu_button_img)
exit_button = ExitButton(SCREEN_WIDTH//2-10, SCREEN_HEIGHT//2+50, exit_button_img)

def main(city):
    global run, game_over, flying, score, speed,\
            scroll_0, scroll_1, scroll_2, scroll_3, scroll_4, scroll_5, scroll_ground, \
            last_obs, obstacle_freq, hit, weather
    # weather response and city
    api_key = "e1c5932f6c96b34e1263878d1f8b7931"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    res = requests.get(url).json()
    weather = res['weather'][0]['main']
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

        # draw highest score
        draw_highest_score()

        # draw heart counter
        draw_heart(heart_img)

        #look for collision
        if pygame.sprite.groupcollide(ghost_group, obstacle_group, False, False) or player.rect.top < 0:
            hit += 1
            hit_sfx.play()

        # check for game over and reset
        if game_over == True:
            restart_button.draw()
            menu_button.draw()
            exit_button.draw()
            key_pressed = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key_pressed = True
                if event.type == pygame.QUIT or exit_button.draw() == True:
                    run = False
            if restart_button.draw() == True or key_pressed == True:
                game_over = False
                reset_game()
            if menu_button.draw() == True:
                choose_city()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and flying == False and game_over == False:
                flying = True
                game_start_sfx.play()

        pygame.display.update()
    pygame.quit()

menu()
