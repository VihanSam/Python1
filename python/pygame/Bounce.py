import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

img = pygame.image.load("/Users/vihan/PycharmProjects/PYTHON/python/pygame/CrazySmile.bmp")

# Var
keep_going = True
picx = 0
picy = 0
timer = pygame.time.Clock()
speedx = 3
speedy = 5 
#Black = (0,0,0,)
# Loop
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
            
    picx += speedx
    picy += speedy
    if picx  <= 0 or picx + img.get_width()>= 800:
        speedx = -speedx
    if picy <= 0 or picy + img.get_height()>= 600:
        speedy = -speedy
    #screen.fill(Black)
    screen.blit(img, (picx, picy))
    timer.tick(60)

    pygame.display.update()
pygame.quit()