import pygame
pygame.init()
clock = pygame.time.Clock()
FPS = 60
SCREEN_W = 1100
SCREEN_H = 700

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Ghost run to hell")
sys_font = pygame.font.SysFont("roboto", 80)

background = pygame.image.load("im/bg-1.jpg").convert_alpha()
text_score = sys_font.render("score", False, "Black")#ยังไม่เเสดงมา
# bg_width = background.get_width()
# bg_hight = background.get_height()

ghost = pygame.image.load("im/12.1.png")
ghost = pygame.transform.scale(ghost, (120,120))
# ghostrect = ghost.get_rect(m = (80, 300))
GHOST_X_POS = 200

scroll = 0

run = True
while run:
    key = pygame.key.get_pressed()
    if key[pygame.K_a] and scroll > 0:
        scroll -= 5
    if key[pygame.K_d]:
        scroll += 5
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        GHOST_X_POS = 0.2
        if GHOST_X_POS > 1100: GHOST_X_POS = 500
    
    screen.blit(background, (0, 0))
    screen.blit(text_score, (20, 700))
    screen.blit(ghost, (GHOST_X_POS, 400))
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()

