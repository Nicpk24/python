# Nicholas Kelly, Assignemnt 1 CPSC 217
# ID: 30040787
from SimpleGraphics import *
setWindowTitle("Assignment1")
background("turquoise1")

# CENTER
# line(400,0,400,600)
# line(0,300,800,300)

# USER INPUT
x = float(input("x Position:"))
y = float(input("y Position:"))
# OPTIONAL SCALING
d = float(input("How large do you want the Emoji (Try 100-400):"))

# TEST VALUES
# x = 400
# y = 300
# d = 400

def draw():
    # HEAD
    setOutline(255,221,103)
    setFill(255,221,103)
    ellipse(x - (d/2) ,y - (d/2) ,d ,d)

    # RIGHT EYE
    setOutline(100,78,43)
    setFill(100,78,43)
    new_x = x - (.25*d)
    new_y = y - (.3*d)
    blob(new_x-(.2*d),new_y+(.25*d),new_x, new_y,new_x+(.2*d),new_y+(.25*d),new_x,new_y+(.125*d))

    # LEFT EYE
    new_x = x + (.25*d)
    new_y = y - (.3*d)
    blob(new_x-(.2*d),new_y+(.25*d),new_x, new_y,new_x+(.2*d),new_y+(.25*d),new_x,new_y+(.125*d))

    # TOUNGE
    setOutline(255,113,127)
    setFill(255,113,127)
    new_x = x + (.25*d)
    new_y = y + (.26*d)
    blob(new_x-(.1875*d),new_y,new_x,new_y-(.1875*d),new_x+(.15*d),new_y+(.15*d))
    # TRIANGLE
    setFill(255,90,109)
    polygon(new_x-(.075*d),new_y-(.0625*d),new_x-(.05*d),new_y-(.125*d),new_x+(.075*d),new_y+(.075*d))

    # MOUTH
    setOutline(100,78,43)
    setFill(100,78,43)
    new_x = x
    new_y = y + (.3*d)
    blob(x-(.5*d),y,x,y+(.2*d),x+(.5*d),y,x,y+(.333*d))

    # TEXT
    size = int(.12*d)
    setFont("Times", size, "bold")
    text(x,y+(.65*d), "Hungry Smiley")
draw()
