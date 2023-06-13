import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

keep_going = True
yellow = (255, 255, 0)
red = (255,0,0)
green = (0,255,0)
radius = 75

#Loop
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    pygame.draw.rect(screen, yellow,[400,300,100,100])
    pygame.draw.rect(screen, red,(100,380),radius)
    pygame.draw.rect(screen, green,(100,80),radius) 
    pygame.display.update()
pygame.quit()