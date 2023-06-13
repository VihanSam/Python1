import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

keep_going = True
yellow = (255, 255, 0)
red = (255,0,0)
green = (0,255,0)
silver = (192,192,192)
radius = 75

#Loop
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    pygame.draw.line(screen, green,[200,250],[350,250],1)
    pygame.draw.line(screen, silver,[500,250],[500,400],1)
    pygame.display.update()
pygame.quit()