import turtle
import random
T = turtle.Pen()
turtle.bgcolor("white")
T.speed(0)
T.hideturtle()

def smiley(x,y):
    T.penup()
    T.setpos(x,y)
    T.pendown()
    
    #FACE
    T.pencolor("yellow")
    T.fillcolor("yellow")
    T.begin_fill()
    T.circle(50)
    T.end_fill()
    
    #EYE 1
    T.setpos(x-15,y+55)
    T.fillcolor("black")
    T.begin_fill()
    T.circle(10)
    T.end_fill()

    
    #EYE 2
    T.setpos(x+15,y+55)
    T.fillcolor("black")
    T.begin_fill()
    T.circle(10)
    T.end_fill()  
    
    #SAD face
    T.setpos(x-10,y+10)
    T.pencolor("black")
    T.width(10)
    T.goto(x+0,y+20)
    T.goto(x+10,y+10)
    

for n in range(50):
    x = random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
    y = random.randrange(-turtle.window_height()//2,turtle.window_height()//2)
    smiley(x,y)
input("")