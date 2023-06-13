import turtle
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
    
    #SMILEY
    T.setpos(x-15,y+30)
    T.pencolor("black")
    T.width(10)
    T.goto(x+15,y+30)
    T.width(1)

 
smiley(0,0)
input("")