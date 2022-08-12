# Nicholas Kelly, Assignemnt 2 CPSC 217
# ID: 30040787
from SimpleGraphics import *
from random import randint
setWindowTitle("Assignment 2")

# CHOOSE TYPE
def graphType():
    global chartType
    chartType = input("Enter pie for a pie chart or bar for a bar graph:")
    if chartType == "pie":
        getValues()
        calcWeights()
        newPieChart = pieChart(chartTitle, sectionNum, sectionSum, sectionList, sectionValues, sectionWeights)
        newPieChart.drawPie()

    elif chartType == "bar":
        getValues()
        newBarGraph = barGraph(chartTitle, xLabel, yLabel, familyNum, userList, phoneCosts, shoppingCosts, transCosts)
        newBarGraph.drawBar()

    else:
        print("Wrong type, check your caps lock")
        graphType()

# USER INPUT
def getValues():
    global chartTitle
    global sectionNum
    global sectionSum
    global sectionList
    global sectionValues
    global sectionWeights
    global xLabel
    global yLabel
    global familyNum
    global userList
    global phoneCosts
    global shoppingCosts
    global transCosts
    chartTitle = None
    sectionNum = None
    sectionSum = None
    xLabel = None
    yLabel = None
    familyNum = None
    sectionList = []
    sectionValues = []
    sectionWeights = []
    userList = []
    phoneCosts = []
    shoppingCosts = []
    transCosts = []

    if chartType == "pie":
        try:
        # USER INPUT
            chartTitle = input("Title:")
            sectionNum = int(input("How many sections:"))
            sectionSum = int(input("Total value of combined sections:"))

        # TEST VALUES
            # chartTitle = "Title"
            # sectionNum = 4
            # sectionSum = 100
            # sectionList = ["One", "Two", "Three", "Four"]
            # sectionValues = [70, 10, 15, 5]

        # SECTIONS
            for i in range(sectionNum):
                sectionName = input("Enter a section name:")
                sectionList.append(sectionName)

                sectionValue = int(input("Enter the value:"))
                sectionValues.append(sectionValue)
            testValues()

        except:
            print("There was an error in the data you entered, please try again")
            getValues()

    # BAR GRAPH
    else:
        try:
        # USER INPUT
            chartTitle = input("Title:")
            xLabel = input("X axis label:")
            yLabel = input("y axis label:")
            familyNum = int(input("How many family members:"))

        # TEST VALUES
            # chartTitle = "Title"
            # xLabel = "x axis"
            # yLabel = "y axis"
            # familyNum = 10
            #
            # userList = ["father", "mother", "daughter", "son", "5", "6", "7", "8", "9", "10"]
            # phoneCosts = [300, 100, 300, 300, 200, 300, 300, 300, 200, 100]
            # shoppingCosts = [100, 200, 200, 200, 300, 200, 200, 200, 200, 200]
            # transCosts = [200, 300, 100, 100, 100, 100, 100, 100, 300, 300]

            if familyNum > 0:
                print("The total values for one member can't exceed $600")

            for i in range(familyNum):
                memberName = input("Enter members name:")
                userList.append(memberName)

                phoneCost = int(input("Enter the money spent on phone bill:"))
                phoneCosts.append(phoneCost)

                shoppingCost = int(input("Enter the money spent on shopping:"))
                shoppingCosts.append(shoppingCost)

                transCost = int(input("Enter the money spent on transportation:"))
                transCosts.append(transCost)
            #
            testValues()

        except:
            print("There was an error in the data you entered, please try again")
            getValues()

# ERROR TESTING
def testValues():
    try:
        test = 0
        # TESTING PIE VALUES
        if chartType == "pie":
            for i in range(sectionNum):
                if sectionValues[i] <= 0:
                    print("There value can't be less than or equal to 0")
                    getValues()
                test += sectionValues[i]

            if sectionNum  <= 0:
                print("The number of sections cant be less than or equal to 0")
                getValues()

            elif sectionSum <= 0:
                print("There must be sections")
                getValues()

            if test != sectionSum:
                print("Total sum didn't match values")
                getValues()

        # TESTING BAR VALUES
        else:
            if familyNum <= 0:
                print("The Family needs to have members")
                getValues()

            for i in range(familyNum):
                if phoneCosts[i] < 0 or shoppingCosts[i] < 0 or transCosts[i] < 0:
                    print("Values need to be positive")
                    getValues()

                total = phoneCosts[i] + shoppingCosts[i] + transCosts[i]

            if total > 600:
                print("Spending limit was exceeded")
                getValues()

    except:
        print("There was an error testing values")
        getValues()

# WEIGHT CALCULATION
def calcWeights():
    try:
        denom = 0
        for i in range(sectionNum):
            denom += sectionValues[i]

        for i in range(sectionNum):
            sectionWeights.append(sectionValues[i] / denom)

    except:
        print("There was an error calculating weights")
        getValues()

# COLOUR PICKER
def randCol():
    global randRed
    global randGreen
    global randBlue

    try:
        randRed = randint(0,255)
        randGreen = randint(0,255)
        randBlue = randint(0,255)
    except:
        print("There was an error choosing the colour")
        getValues()

# PIE MAKER :D
class pieChart:
    def __init__(self, chartTitle, sectionNum, sectionSum, sectionList, sectionValues, sectionWeights):
        self.chartTitle = chartTitle
        self.sectionNum = sectionNum
        self.sectionSum = sectionSum
        self.sectionList = sectionList
        self.sectionValues = sectionValues
        self.sectionWeights = sectionWeights

    def drawPie(self):
        try:
            # TITLE
            setFont("Times", 20, "bold")
            text(400, 50, self.chartTitle)

            # OUTLINE
            setFill("aquamarine")
            setOutline("black")
            ellipse(200, 125, 400, 400)

            theta = 0
            incrament = 0
            colourChange = 0

            # SECTIONS
            for i in range(self.sectionNum):
                randCol()
                setOutline("black")
                setFill(randRed, randGreen, randBlue)
                pieSlice(210, 130, 380, 390, theta, (self.sectionWeights[i] * 360))
                theta += (sectionWeights[i] * 360)

            # LEGEND
                setColor(randRed, randGreen, randBlue)
                setFont("Times", 16)
                text(675, 125 + incrament, self.sectionList[i] + " " + str(round(self.sectionWeights[i]*100)) + "%")
                incrament += (200 / sectionNum)
        except:
            print("There was an error drawing")
            getValues()

# BAR MAKER
class barGraph:
    def __init__(self, chartTitle, xLabel, yLabel, familyNum, userList, phoneCosts, shoppingCosts, transCosts):
        self.chartTitle = chartTitle
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.familyNum = familyNum
        self.userList = userList
        self.phoneCosts = phoneCosts
        self.shoppingCosts = shoppingCosts
        self.transCosts = transCosts

    def drawBar(self):
        try:
            # TITLE
            setFont("Times", 20, "bold")
            text(400, 50, self.chartTitle)

            # AXIS
            setFont("Times", 12, "bold")
            setColor("azure4")
            text(600, 525, self.xLabel)
            text(75, 150, self.yLabel)

            # OUTLINE
            setFill("aquamarine")
            setOutline("black")
            rect(150, 150, 650, 350)

            # SCALING X AXIS
            setColor("black")
            setFont("Times", 10)
            scale = 0
            for i in range(11):
                line(150 + scale, 150, 150 + scale, 140)
                percent = str((scale / 600) * 100)
                text(150+scale, 130, percent + "%")
                scale += 60

            randCol()
            phoneRed = randRed
            phoneGreen = randGreen
            phoneBlue = randBlue

            randCol()
            shoppingRed = randRed
            shoppingGreen = randGreen
            shoppingBlue = randBlue

            randCol()
            transRed = randRed
            transGreen = randGreen
            transBlue = randBlue

            # LEGEND
            setColor("black")
            setFont("Times", 16, "bold")

            text(100, 520, "Phone")
            setFill(phoneRed, phoneGreen, phoneBlue)
            rect(100, 540, 20, 20)

            text(210, 520, "Shopping")
            setFill(shoppingRed, shoppingGreen, shoppingBlue)
            rect(210, 540, 20, 20)

            text(320, 520, "Transit")
            setFill(transRed, transGreen, transBlue)
            rect(320, 540, 20, 20)

            offset = 0
            ySize = (120 / familyNum)
            for i in range(familyNum):
                xFix = 0
                # NAMES
                setColor("black")
                setFont("Times", 14, "bold")
                text(100, 180 + offset, self.userList[i])

                # BARS
                setColor(phoneRed, phoneGreen, phoneBlue)
                setOutline("black")
                if self.phoneCosts[i] != 0:
                    rect(151 + xFix, 180 + offset, self.phoneCosts[i], ySize)
                    xFix += self.phoneCosts[i]

                setColor(shoppingRed, shoppingGreen, shoppingBlue)
                setOutline("black")
                if self.shoppingCosts[i] != 0:
                    rect(151 + xFix, 180 + offset, self.shoppingCosts[i], ySize)
                    xFix += self.shoppingCosts[i]

                setColor(transRed, transGreen, transBlue)
                setOutline("black")
                if self.transCosts[i] != 0:
                    rect(151 + xFix, 180 + offset, self.transCosts[i], ySize)
                    xFix += self.transCosts[i]

                offset += 300 / familyNum

        except:
            print("There was an error drawing")
            getValues()

graphType()
