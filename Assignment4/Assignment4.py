# Nicholas Kelly, Assignemnt 4 CPSC 217
# ID: 30040787

# MAIN FUNCTION, LOADS/PROCESSES FILE, CALLS FUNCTIONS
def main():
    flightLog = {}
    sentences = []
    date = input("Enter flight Information Date (DDMMYYYY):")
    print("")
    try:
        file = open("Flight-Information-{}.dat".format(date), "r")
    except:
        print("No such date, check your format")
        exit()

    # TEST INPUT
    # file = open("Flight-Information-26062018.dat", "r")

    for line in file:
        words = line.split()
        sentences.append(words)

    for word in sentences:
        # WORD[1] IS FLIGHT NUMBER, WORD[3] IS DEPARTURE CITY, WORD[5] IS ARRIVAL CITY
        key = (word[3], word[1])
        flightLog[key] = word[5]

    try:
        getPaths(flightLog)
        sinkSource(flightLog)
        most(flightLog)
        connecting(flightLog)
        file.close()
    except:
        print("Error")
        exit()

# FUNCTION TO GET THE DEPARTURE FLIGHTS
def getPaths(flightLog):
    added = []
    departures = []
    multiple = {}

    for key in flightLog:
        added.append(key[0])

    for city in added:
        if city not in departures:
            departures.append(city)
            multiple[city] = 1
        else:
            multiple[city] += 1

    for city in multiple:
        if multiple[city] == 1:
            destination = getDest(city, flightLog)
            print("There is 1 flight from {}, to {}.".format(city, destination))

        else:
            destination = getDest(city, flightLog)
            print("There are {} flights from {}, to {}".format(multiple[city], city, destination))

# FUNCTION THAT FINDS WHERE THE DEPARTUE FLIGHTS GO
def getDest(city, flightLog):
    destinations = []
    destination = ""
    for key in flightLog:
        if city in key:
            destinations.append(flightLog[key])

    if len(destinations) > 1:
        destination = destinations[0]
        for i in range(1, len(destinations)):
            destination += ", and {}".format(destinations[i])
            if i == len(destinations)-1:
                destination += "."
    else:
        destination = destinations[0]
    # DESTINATION LIST BASES ON A DEPARTURE CITY
    return destination

# FUNCTION THAT FINDS OUT WHAT CITIES ARE SINKS/SOURCES
def sinkSource(flightLog):
    arrivalCities = []
    departureCities = []
    sources = []
    sinks = []

    for key in flightLog:
        if key[0] not in departureCities:
            departureCities.append(key[0])
        if flightLog[key] not in arrivalCities:
            arrivalCities.append(flightLog[key])

    for city in arrivalCities:
        if city not in arrivalCities and city not in sources:
            sources.append(city)

        if city not in departureCities and city not in sinks:
            sinks.append(city)

    for city in departureCities:
        if city not in arrivalCities and city not in sources:
            sources.append(city)

        if city not in departureCities and city not in sinks:
            sinks.append(city)

    print("\nSources:", sources)
    print("Sinks:", sinks)

# FUNCTION THAT DETERMINES MOST INCOMING AND OUTGOING FLIGHTS
def most(flightLog):
    mostOut = {}
    mostIn = {}
    for key, value in flightLog.items():
        if value not in mostIn:
            mostIn[value] = 0

        else:
            mostIn[value] += 1

        if key[0] not in mostOut:
            mostOut[key[0]] = 0

        else:
            mostOut[key[0]] += 1

    print("\nThe city with the most outgoing flights is {}.".format(max(mostOut, key = mostOut.get)))
    print("The city with the most incoming flights is {}.".format(max(mostIn, key = mostIn.get)))

# FUNCTION THAT FINDS CONNECTING FLIGHTS
def connecting(flightLog):
    print("\nEnter \"q\" any time to quit")
    departure = input("\nEnter a departure city:")
    if departure == "q":
        # RETURNING OUT OF THE FUNCTION
        return

    arrival = input("Enter an arrival city:")
    if arrival == "q":
        # RETURNING OUT OF THE FUNCTION
        return

    # TEST INPUT
    # departure = "Calgary"
    # arrival = "Newyork"

    destinations = []
    keys = []
    ask = False
    connections = 0
    count = 0
    reversed = False
    altCount = 0

    while departure != "q" and arrival != "q":
        count += 1
        for key in sorted(flightLog, reverse = reversed):
            if flightLog[key] == arrival:
                # KEY IS FLIGHT TO FINAL DESTINATION
                if key[0] == departure:
                    # DEPARTURE LOCATION THAT TAKES YOU TO DESTINATION IS ALSO SAME FLIGHT
                    connections += 1
                    ask = True
                    if connections == 1:
                        destinations.append(arrival)
                        print("{} can be reached with 1 connected flight".format(destinations[0], connections))
                        ask = True
                    else:
                        print("{} can be reached with {} connecting flights".format(destinations[0], connections))
                        ask = True
                else:
                    keys.append(key)
                    connections += 1
                    destinations.append(arrival)
                    # SET ARRIVAL DESTINATION TO FLIGHT THAT CONNECTS FROM DESTINATION,
                    # this causes error if multiple flights exist
                    arrival = key[0]
                    if connections > len(flightLog.values()):
                        print("No flights connecting those locations")
                        print("CONNECTIONS TOO LONG")
                        ask = True

        # IF FLIGHT NOT FOUND TRY TO GO THROUGH THE LOG BACKWARDS, THIS HELPS WITH MULTIPLE FLIGHTS LEAVING A CITY
        if count > len(flightLog.values()):
            altCount += 1
            reversed = True
            keys = []
            ask = False
            connections = 0
            count = 0
            try:
                arrival = destinations[0]
            except:
                print("Flight not found try again (this is case sensitive)")
                ask = True
            destinations = []

        # CATCH ALL SO THE FUNCTION WILL ASK FOR INPUT
        if altCount > 10:
            print("No flights found")
            ask = True


        if ask == True:
            altCount = 0
            reversed = False
            connections = 0
            destinations = []
            ask = False
            departure = input("\nEnter a departure city:")
            if departure == "q":
                # BREAK OUT OF FUNCTION
                return
            arrival = input("Enter an arrival city:")

main()
