import pygame
import os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("City Choose")
center = screen.get_rect().centery

running = True
city_name = "Choose your city!"

center_y = (screen.get_rect().centery)-10
center_x = (screen.get_rect().centerx)
alpha_value = 165

bangkok_img = pygame.image.load("project_game/city_choosing/Bangkok_box.png")
bangkok_img = pygame.transform.scale(bangkok_img, (300/2, 300/2))
bangkok_rect = bangkok_img.get_rect(center = (center_x - 200, center_y - 0))
bang_name = pygame.image.load("project_game/media/Bangkok_sign.png")
bang_name = pygame.transform.scale(bang_name, (297/(2.5*1.05), 51/(2.5*1.05)))
bang_rect = bang_name.get_rect(center = (center_x - 200, center_y + 80))
bangkok_img.set_alpha(alpha_value)
bang_name.set_alpha(alpha_value)

italy_img = pygame.image.load("project_game/city_choosing/Italy_box.png")
italy_img = pygame.transform.scale(italy_img, (300/2, 300/2))
italy_rect = italy_img.get_rect(center = (center_x, center_y - 0))
italy_name = pygame.image.load("project_game/media/rome_sign.png")
italy_name = pygame.transform.scale(italy_name, (288/(4.25*1.05), 80/(4*1.05)))
italy_n_rect = italy_name.get_rect(center = (center_x, center_y + 80))
italy_img.set_alpha(alpha_value)
italy_name.set_alpha(alpha_value)

tokyo_img = pygame.image.load("project_game/city_choosing/Tokyo_box.png")
tokyo_img = pygame.transform.scale(tokyo_img, (300/2, 300/2))
tokyo_rect = tokyo_img.get_rect(center = (center_x + 200, center_y - 0))
tokyo_name = pygame.image.load("project_game/media/tokyo_sign.png")
tokyo_name = pygame.transform.scale(tokyo_name, (279/(3.5*1.05), 70/(3.5*1.05)))
tokyo_n_rect = tokyo_name.get_rect(center  = (center_x + 200, center_y + 80))
tokyo_img.set_alpha(alpha_value)
tokyo_name.set_alpha(alpha_value)

play_img = pygame.image.load("project_game/city_choosing/play.png")
play_img = pygame.transform.scale(play_img, (157/1.5, 68/1.5))# 157x68
play_rect = play_img.get_rect(center = (center_x, center_y+120))
play_img.set_alpha(255)

font = pygame.font.FontType("project_game/font/Pixgamer.ttf", 36)

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
                    os.system("python project_game/change_color_button.py")
                    running = False
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

    text = font.render(f"{city_name}", True, (0, 0, 0))
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

pygame.quit()
