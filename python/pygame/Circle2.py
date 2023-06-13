import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

#Variable
catch = True
#Colors
silver = (192,192,192)
radius = 100

#Loop 
while catch:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            catch = False
    pygame.draw.circle(screen, silver,(350,230),radius)
    pygame.display.update()

pygame.quit()