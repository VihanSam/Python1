import random
import turtle
#Pen Hold
T = turtle.Pen()
#Background Color Set
turtle.bgcolor("white")
#list of colors 
colors = ["Purple","Blue","Green","Yellow","Pink","Coral","Navy","Orange","Lime","Red"]
#for loop
for n in range(50):
    T.pencolor(random.choice(colors))
    #Defining size
    size = random.randint(10,40)
    #X & Y
    x = random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,turtle.window_height()//2)
    #First spiral
    T.penup()
    #Define x,y
    T.setpos(x,y)
    T.pendown()
    #for loop2
    for m in range(size):
        #Spiral Size
        T.forward(m*2)
        T.left(91)
        
    #Second spiral
    T.penup()
    #Define x,y
    T.setpos(-x,y)
    T.pendown()
    #for loop2
    for m in range(size):
        #Spiral Size
        T.forward(m*2)
        T.left(91)
    T.penup()
    #Define x,y
    T.setpos(x,-y)
    T.pendown()
    #for loop2
    for m in range(size):
        #Spiral Size
        T.forward(m*2)
        T.left(91)
    T.penup()
    #Define x,y
    T.setpos(-x,-y)
    T.pendown()
    #for loop2
    for m in range(size):
        #Spiral Size
        T.forward(m*2)
        T.left(91)