# Nicholas Kelly, Assignemnt 3 CPSC 217
# ID: 30040787
from SimpleGraphics import *
from time import sleep

# GETTING IMAGE NAMES AND LOADING
def main():
    global puzzle
    global borderColours
    global fillColour
    global puzzleName
    # fillColour = [255, 165, 0]
    fillColour = [100, 30, 91]
    borderColours = []
    try:
        # USER INPUT
        puzzleName = input("Enter the name of the puzzle file:")
        for i in range(3):
            borderColour = int(input("Enter the border colour (r, g, b):"))
            borderColours.append(borderColour)

        # TEST VALUE
        # puzzleName = "DogPuzzle.ppm"
        # borderColours = [100, 30, 90]

        # SETUP
        puzzle = loadImage(puzzleName)
        resize(getWidth(puzzle), getHeight(puzzle))

        drawImage(puzzle, 0, 0)
        getValues()

    except:
        print("Error loading, insure names are correct")
        main()

# GETTING USER INPUT (X, Y)
def getValues():
    # WILL NOT EXIT UNTIL LEFT BUTTON PRESSED
    print("Please click a puzzle peice")
    while True:
        update()
        if leftButtonPressed():
            x, y = mousePos()
            r, g, b = getPixel(puzzle, x, y)
            break
    floodFill(x, y)
    again()

# FLOOD FILL ALGORITHM
def floodFill(x, y):
    print("Please wait (this could take a while)")
    processed = []
    counter = 0
    r, g, b = getPixel(puzzle, x, y)
    if r == borderColours[0] and g == borderColours[1] and b == borderColours[2]:
        print("You clicked the Edge of a peice, try again")
        sleep(.2)
        getValues()
        exit()

    q = []
    q.append([x, y])
    processed.append([x, y])

    while len(q) > 0:
        # q NEEDS TO EMPTY BEFORE FUNCTION WILL FINISH
        try:
            noneAdded = True
            first = q[0]
            x = first[0]
            y = first[1]
            r, g, b = getPixel(puzzle, x, y)
            q.append([x, y])
            del q[0]

            if r != fillColour[0] and g != fillColour[1] and b != fillColour[2]:
                if r != borderColours[0] and g != borderColours[1] and b != borderColours[2]:
                    putPixel(puzzle, x, y, fillColour[0], fillColour[1], fillColour[2])
                    processed.append([x, y])
                    del q[0]

                    # NORTH
                    if [x, y-1] not in processed:
                        noneAdded = False
                        q.append([x, y-1])

                    # EAST
                    if [x+1, y] not in processed:
                        noneAdded = False
                        q.append([x+1, y])

                    # SOUTH
                    if [x, y+1] not in processed:
                        noneAdded = False
                        q.append([x, y+1])

                    # WEST
                    if [x-1, y] not in processed:
                        noneAdded = False
                        q.append([x-1, y])

                    # HANDLING BORDER CASES
                    if noneAdded == True:
                        del q[0]
                        # print(len(q))
                        # draw()
            # HANDLING MORE BORDER CASES
            else:
                q.remove([x, y])
        # HANDLING EDGE OF IMAGE CASES
        except:
            try:
                del q[0]
            except:
                pass
                # q EMPTY

    draw()

# DRAWS MODIFIED IMAGE
def draw():
    drawImage(puzzle, 0, 0)

# DETERMINES IF THE USER WANTS TO CLICK ANOTHER PUZZLE PIECE
def again():
    choice = input('Enter "yes" to click another piece, or "no" to draw collected pieces:')
    if choice == "yes":
        getValues()
    elif choice == "no":
        ext()
    else:
        print('Enter "yes or "no"')
        again()

# HANDLES CREATING A SEPERATE FILE WITH SELECTED PIECES
def ext():
    fresh = loadImage(puzzleName)
    pieces = createImage(getWidth(puzzle), getHeight(puzzle))
    for i in range(getWidth(puzzle)):
        for j in range(getHeight(puzzle)):
            r, g, b = getPixel(puzzle, i, j)
            if r == fillColour[0] and g == fillColour[1] and b == fillColour[2]:
                r, g, b = getPixel(fresh, i, j)
                putPixel(pieces, i, j, r, g, b)

    # resize(getWidth(puzzle) *2, getHeight(puzzle))
    # drawImage(pieces, getWidth(puzzle), 0)
    saveGIF(pieces, "pieces.gif")

main()
