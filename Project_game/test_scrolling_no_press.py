#for test frame scroll but don't want any key press
import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Parallax")

bg_images = []
for i in range(4):
    #ใช้ชื่อไฟล์ในคอมเค้า เพราะงั้นใครจะหยิบไปเทสต์แก้ชื่อไฟล์ด้วย
    #เซฟชื่องานฉากเป็น bg-(int) จะได้ง่ายเวลาเอามารัน
    bg_image = pygame.image.load(f"PSCP/Project_game/picture/bg-{i}.png").convert_alpha()
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
    # if key[pygame.K_LEFT] and scroll > 0:
    #     scroll -= 5
    if key[pygame.K_LEFT]:
        scroll -= 5
    else: #ถ้ามีการกดปุ่มที่ไม่ใช่ปุ่ม K_LEFT ให้ฉากไหลไปเรื่อยๆ
        scroll += 3

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
