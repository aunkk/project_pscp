import pygame
import sys
import os

# เริ่มต้น Pygame
pygame.init()

WIDTH, HEIGHT = 800, 300
WHITE = (255, 255, 255)
BUTTON_COLOR = (133, 222, 108)
BUTTON_COLOR1 = (255, 99, 71)
TEXT_COL = (77, 44, 255)
BLACK = (0, 0, 0)
SCREEN_MAIN = (100, 50, 98)

custom_font1 = pygame.font.FontType("project_game/media/PressStart2P-Regular.ttf", 30)
# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Menu")
start_img = pygame.image.load("project_game/media/start_button.png").convert_alpha()
exit_img = pygame.image.load("project_game/media/exit_button.png").convert_alpha()


def draw_text(text, font_type, text_color, x, y):
    img = font_type.render(text, True, text_color)
    screen.blit(img, (x, y))


center_x = screen.get_rect().centerx
center_y = screen.get_rect().centery
start_rect = start_img.get_rect(center=(center_x, center_y))
exit_rect = exit_img.get_rect(center=(center_x,  center_y+100))


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
                    os.system("python Project_game\\city_choose.py")
                    running = False
                elif exit_rect.collidepoint(cursor_ckeck):
                    print("Get out")
                    running = False
        else:
            draw_text("Ghost run to hell", custom_font1, TEXT_COL, 350, 50)

    cursor_ckeck = pygame.mouse.get_pos()

    screen.fill(SCREEN_MAIN)
    screen.blit(start_img, start_rect.topleft)
    screen.blit(exit_img, exit_rect.topleft)
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()
