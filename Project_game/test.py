import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_WIDTH))
#ขนาดจอเกมจากโค้ดนี้จะเป็น 700x700
pygame.display.set_caption("Parallax")

bg_images = []
for i in range(4):
    bg_image = pygame.image.load(f"im/bg-{i}.png").convert_alpha()
    bg_images.append(bg_image)
bg_width = bg_images[0].get_width()
def draw_bg():
    for x in range(4):
        speed = 1
        for i in bg_images:
            screen.blit(i, (x*bg_width - scroll*speed, 0))
            speed += 0.2
scroll = 0
#game loop
run = True
while run:
    
    clock.tick(FPS)
    
    draw_bg()
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and scroll > 0: #ถ้ากดลูกศรซ้ายกล้องจะขยับไปทางซ้าย5หน่วย(ถอยหลัง)
        #ใส่ and scroll > 0 เพราะกันฉากไหลตกขอบ
        scroll -= 5
    if key[pygame.K_RIGHT]: #ถ้ากดลูกศรขวากล้องจะขยับไปทางขวา5หน่วย(ไปข้างหน้า)
        scroll += 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
