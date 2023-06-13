import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Ping Pong By Vihan')

pic = pygame.image.load("/Users/vihan/PycharmProjects/PYTHON/python/pygame/real_ball.png")
keep_going = True
#Colors
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
white = (255,255,255)
black = (0,0,0)
Timer = pygame.time.Clock()
speedx = 5
speedy = 5
paddlew = 200
paddleh = 25
paddlex = 300
paddley = 450
#Image
picw = 100
pich = 100
#Score
Points = 0
Font = pygame.font.SysFont("Times",24)
#Game Loop
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    picx += speedx
    picy += speedy
#Bounce back after hitting ball to the screen.
    if picx <= 0 or picx + pic.get_width() >= 800:
        speedx = -speedx *1.1
    if picy <= 0:
        speedy = -speedy +1
    if picy >= 500:
        speedy = 0
        speedx = 0
    screen.fill(black)
    screen.blit(pic,(picx,picy))
    #DRAW Paddle
    paddlex = pygame.mouse.get_pos()[0]
    paddlex -= paddlew / 2
    pygame.draw.rect(screen, white,[paddlex,paddley,paddlew,paddleh])
    if picy + pich >= paddley and picy + pich <= paddley + paddleh and speedy > 0:
        if picx + picw / 2 >= paddlex and picx + picw / 2 <= paddlex + paddlew:
                    Points += 1
                    speedy = -speedy
    #Display Points ->
    Drawstring = "Points: " + str(Points)
    if picy >= 500:
        Drawstring = "Gamer Over Your Score is " + str(Points)
    Text = Font.render(Drawstring,True,white)
    Text_rect = Text.get_rect()
    Text_rect.centerx = screen.get_rect().centerx
    Text_rect.y = 10
    screen.blit(Text,Text_rect)
    pygame.display.update()
    Timer.tick(60)
pygame.quit()