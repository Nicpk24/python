from SimpleGraphics import*

def click():
    while True:
        update()

        if leftButtonPressed():
            mx,my=mousePos()
            break
    #calling extraction
    extraction(mx,my)


def extraction(mx,my):
    xpos=[]
    ypos=[]
    xpos.append(mx)
    ypos.append(my)

    while len(xpos)>0:
        r,g,b=getPixel(img,mx,my)
        if r==100 and b==30 and g==90:
            print("if")
            break
        elif r!=100 or g!=30 or b!=90:
            print("elif")
            img2=createImage(w,h)
            putPixel(img2,mx,my,r,g,b)

        xpos.remove(mx)
    drawImage(img2,w,h)
    # saveGIF(img2, "pieces2.gif")


def main():
    global img
    # imgname=input("Enter the puzzle picture name:")
    imgname = "DogPuzzle.ppm"
    img = loadImage(imgname)
    global w
    global h
    w=getWidth(img)
    h=getHeight(img)

    resize(w,h)
    drawImage(img,0,0)

    click()


main()

print("done")
