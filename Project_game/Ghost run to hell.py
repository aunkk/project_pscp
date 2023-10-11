import pygame
pygame.init()
clock = pygame.time.Clock()
FPS = 60


SCREEN_W = 1100
SCREEN_H = 700
WHITE = (255,255,255)

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Ghost run to hell")
screen.fill(WHITE)

background = pygame.image.load("im/bg-1.jpg").convert_alpha()
bg_width = background.get_width()
bg_hight = background.get_height()
font_ = pygame.font.SysFont("zillaslab", 20)
text = font_.render("game", False, "Black")

ghost = pygame.image.load("im/12.1.png")
GHOST_X_POS = 200

def draw_bg():
    for x in range(10):
        speed = 1
        screen.blit(background, (x*bg_width - scroll, 0))#run in x
        speed += 2
    # for y in range(10):
    #     speed = 1
    #     screen.blit(background, (0, y*bg_hight - upanddown))#run in y
    #     speed += 2
scroll = 0
upanddown = 0

run = True
while run:

    clock.tick(FPS)
    draw_bg()#call function
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and scroll > 0:
        scroll -= 5
    if key[pygame.K_d]:
        scroll += 5

# run = True
# while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    GHOST_X_POS = 0.2
    if GHOST_X_POS > 1100: GHOST_X_POS = 500
    screen.blit(ghost, (GHOST_X_POS, 260))
    pygame.display.update()
pygame.quit()

