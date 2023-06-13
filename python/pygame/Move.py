import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

img = pygame.image.load("/Users/vihan/PycharmProjects/PYTHON/python/pygame/CrazySmile.bmp")

# Var
keep_going = True
picx = 700
picy = 0
timer = pygame.time.Clock()

# Loop
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
            
    #picx += 1
    picy += 1
    screen.blit(img, (picx, picy))
    timer.tick(60)

    pygame.display.update()
pygame.quit()