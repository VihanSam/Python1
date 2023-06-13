import pygame
import random
screen = pygame.display.set_mode((1000,600))

snow = True
yellow = (255, 255, 0)
radius = 25


while snow:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            snow = False
    for y in range(550):
        pygame.draw.circle(screen,yellow,(50,y),radius)
        
    pygame.display.flip()
pygame.quit()
