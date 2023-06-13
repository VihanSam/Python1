import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Click To Draw!")

#Variables 5
keep_going = True
yellow = (255, 255, 0)
radius = 30

#Loop
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
    if  mousedown:
            Spot = event.pos
            pygame.draw.circle(screen, yellow, Spot ,radius)
    pygame.display.update()
pygame.quit()