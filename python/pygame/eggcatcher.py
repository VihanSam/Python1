from itertools import cycle
from random import randrange
from tkinter import Canvas,Tk,messagebox,font

Canvas_width = 1000
Canvas_height = 600

root = Tk()
root.title("Egg Catcher!)")
C = Canvas(root, width = Canvas_width, height = Canvas_height,background = "Sky Blue")
C.create_rectangle(-5, Canvas_height-100, Canvas_width+5, Canvas_height+5, fill="sea green", width=0) # width=0 for border
C.create_oval(-80, -80, 120, 120, fill='orange', width=0)
C.pack()

color_cycle = cycle(["Light Yellow","Light Green","Red","Blue","Purple"])
egg_width = 45
egg_height = 55
egg_speed = 500
difficulty = .9
egg_interval = 4000

catcher_color = "Orange"
catcher_width = 100
catcher_height = 100
catcher_startx = Canvas_width / 2 - catcher_width / 2
catcher_starty = Canvas_height - catcher_height - 20
catcher_startx2 = catcher_startx + catcher_width
catcher_starty2 = catcher_starty + catcher_height
catcher = C.create_arc(catcher_startx, catcher_starty, catcher_startx2, catcher_starty2, start=200, extent=140, style="arc", outline=catcher_color, width=10)

game_font = font.nametofont("TkFixedFont")
game_font.config(size=18)

score = 0
score_text = C.create_text(10,10,anchor="nw",font = game_font,fill = "Black",text = "Score: "+str(score))

Lives_remaining = 3
Lives_text = C.create_text(Canvas_width-10,10,anchor="ne",font = game_font,fill = "Black",text = "Lives: "+str(Lives_remaining))
eggs = []
def create_egg():
    x = randrange(10, 740)
    y = 40
    new_egg = C.create_oval(x, y, x+egg_width, y+egg_height, fill=next(color_cycle), width=0)
    eggs.append(new_egg)
    root.after(egg_interval, create_egg)
    
def move_eggs():
    for egg in eggs:
        (eggx, eggy, eggx2, eggy2) = C.coords(egg)
        C.move(egg, 0, 10)
        if eggy2 > Canvas_height:
            egg_drop(egg)
    root.after(egg_speed, move_eggs)

def move_left(event):
    (x1,y1,x2,y2)=C.coords(catcher)
    if x1 > 0:
        C.move(catcher,-20,0)

def move_right(event):
    (x1,y1,x2,y2)=C.coords(catcher)
    if x2 < Canvas_width:
        C.move(catcher,20,0)

def egg_drop(egg):
    eggs.remove(egg)
    C.delete(egg)
    lose_alife()
    if Lives_remaining == 0:
        messagebox.showinfo("Game Over!"," Game Over:D Final Score: "+str(score))
        root.destroy()
def lose_alife():
    global Lives_remaining
    Lives_remaining -= 1
    C.itemconfigure(Lives_text,text="Lives: "+str(Lives_remaining))
def check_catch():
    global score,egg_speed
    (catcherx1,catchery1,catcherx2,catchery2)=C.coords(catcher)
    for egg in eggs:
        (eggx1,eggy1,eggx2,eggy2)=C.coords(egg) 
        if catcherx1 < eggx1 and eggx2 < catcherx2 and catchery2 - eggy2 < 40:
            eggs.remove(egg)
            C.delete(egg)
            increase_score(10)
    root.after(100,check_catch)

def increase_score(points):
    global score, egg_speed, egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty)
    egg_interval = int(egg_interval * difficulty)
    C.itemconfigure(score_text, text="Score: " + str(score))
C.bind("<Left>",move_left)
C.bind("<Right>",move_right)
C.focus_set()
root.after(1000, create_egg)
root.after(1000, move_eggs)
root.after(100,check_catch)
root.mainloop()