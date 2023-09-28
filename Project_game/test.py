import pygame

pygame.init() #start pygame
pygame.display.set_caption("peenoi") #Title

screen = pygame.display.set_mode((970, 720)) #screen size

running = True
while running: #control game running
    for event in pygame.event.get(): #check current event
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
