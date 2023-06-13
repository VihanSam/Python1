import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

img = pygame.image.load("/Users/vihan/PycharmProjects/PYTHON/python/pygame/CrazySmile.bmp")

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
    screen.blit(img,(400,500))
    
    pygame.display.update()
pygame.quit()