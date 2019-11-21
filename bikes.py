import urllib.request

"""
This function reads the BikeShare data from the text file.
It sorts it into separate lists, then combines these lists into another.
"""
def readHtml():
    response = urllib.request.urlopen("http://research.cs.queensu.ca/home/cords2/bikes.txt")

    # Create list for each section of data
    stationId=[]
    name=[]
    lat=[]
    lon=[]
    capacity=[]
    bikesAvailable=[]
    docksAvailable=[]
    
    # iterate through each line in the text file
    check=True
    while check==True: # goes through line by line
        html = response.readline()  #reads current line
        data = html.decode('utf-8').split()   #splits this line into a list of "tokens"

        if len(data)==0: # If the line is empty, we are at the end of the text file
            break # So, the loop breaks

        # Add the correct information in the current line to each list
        stationId.append(data[0])
        name.append(" ".join(data[1:len(data)-5]))
        lat.append(data[len(data)-5])
        lon.append(data[len(data)-4])
        capacity.append(data[len(data)-3])
        bikesAvailable.append(data[len(data)-2])
        docksAvailable.append(data[len(data)-1])

    # deletes the first entry of each list (ex. "station_id" and "name")
    del stationId[0]
    del name[0]
    del lat[0]
    del lon[0]
    del capacity[0]
    del bikesAvailable[0]
    del docksAvailable[0]

    # turn each list of strings into a list of ints or floats (except for "name")
    # ex. "7005" becomes 7005
    for x in range(len(stationId)):
        stationId[x]=int(stationId[x])
        lat[x]=float(lat[x])
        lon[x]=float(lon[x])
        capacity[x]=int(capacity[x])
        bikesAvailable[x]=int(bikesAvailable[x])
        docksAvailable[x]=int(docksAvailable[x])
    
    # add each list into a bigger list of all data
    allData=[]
    allData.append(stationId)
    allData.append(name)
    allData.append(lat)
    allData.append(lon)
    allData.append(capacity)
    allData.append(bikesAvailable)
    allData.append(docksAvailable)
    
    return allData # return list of all text file data


def checkDocksFull(stationID, allData):
# Checks if all docks at the specified station are full
    
    index=allData[0].index(stationID) # index of the station entered
    
    if allData[6][index]==0: # if the # of open docks at that station is > 0
        return True # all docks are full, no room to return bike
    else:
        return False # at least one open dock, there is room to return bike


def getBikeAvailability(stationID, allData):
# Checks if there is a bike available at a certain station

    index=allData[0].index(stationID) # index of the station entered
    if allData[5][index]>0: # if the number of bikes at that station is > 0
        return True #there is at least 1 bike available
    else:
        return False # no more bikes at that station


def rentBike(stationID, allData):
# Rents a bike from a specified station
        
    index=allData[0].index(stationID) # index of the station entered

    # if there is a bike available at that station
    if getBikeAvailability(stationID, allData) == True:
        print("Bike has successfully been rented.") # then, bike can be rented
        
        # Subtract 1 bike from # of available bikes at requested station
        allData[5][index]=allData[5][index]-1

        # Add 1 to the # of docks available at requested station
        allData[6][index]=allData[6][index]+1
        
    else: # no bikes at that staion to rent
        print("Sorry, there are no available bikes at this station.")

    
def returnBike(stationID, allData):
# Returns a bike to a specified station

    index=allData[0].index(stationID) # index of the station entered

    # the docks at that station are not full- there is space to return bike
    if checkDocksFull(stationID, allData) == False:

        # Add 1 bike to # bikes available at specified station
        allData[5][index]=allData[5][index]+1

        # Subtract 1 from # of available docks at requested station
        allData[6][index]=allData[6][index]-1

        print("Bike has successfully been returned.")

    else: # all docks at that station are full- no room to return bike
        print("Sorry, this station is full so the bike cannot be returned.")


def getStationsWithBikes(allData):
# Prints which stations have bikes available for rent in order greatest to least

    stationsWithBikes = [] # create empty list
    # loop through every station
    for x in range(len(allData[0])):
        # if there is at least one bike available at the current station
        if allData[5][x] > 0:
            # add a sublist with the station and bike number to stationsWithBikes
            stationsWithBikes.append([allData[0][x],allData[5][x]])

    # sort sublists greatest to least by their second element
    stationsWithBikes.sort(key=lambda x: x[1], reverse=True)
    
    orderedStations=[] # create new list
    # loop through new sorted list of stations with bikes
    for x in range (len(stationsWithBikes)):
        # add only the stations numbers to the list
        orderedStations.append(stationsWithBikes[x][0])
        # this list now contains the stations with bikes (greatest to least)

    return "Stations with Available Bikes: " + ", ".join(str(x) for x in orderedStations)


def getDirections(stationID1, stationID2, allData):
# Determines the direction (northeast, southwest, etc) the user must travel to get from station1 to station 2

    index1=allData[0].index(stationID1) # the index of the starting station
    index2=allData[0].index(stationID2) # the index of the ending station

    # If the latitude of stationID2 > latitude of stationID1, the user must travel north
    if allData[2][index2] > allData[2][index1]:
        direction1="north"
    else: # otherwise, they must travel south
        direction1="south"

    # If the longitude of stationID2 > longitude of stationID1, the user must travel east
    if allData[3][index2] > allData[3][index1]:
        direction2="east"
    else: # otherwise, the must travel west
        direction2="west"

    return ("You must travel " + direction1 + direction2 + ".")


def getStationInfo(stationID, allData):
# Prints all information about a specific station

    # index of station the user in inquiring about
    index=allData[0].index(stationID)

    # return name, latitude, longitude, capacity, bikes available, docks available
    return "Station " + str(stationID) + ":\nLocation: " + allData[1][index] +\
    "\nCoordinates: " + str(allData[2][index]) + ", " + str(allData[3][index]) +\
    "\nCapacity: " + str(allData[4][index]) + "\nBikes available: " +\
    str(allData[5][index]) + "\nDocks available: " + str(allData[6][index])


def getFullyLoadedStations(allData):
# Prints the stations whose docks are fully loaded with bikes

    fullyLoadedStations=[] # create empty list

    # loops through every station
    for x in range(len(allData[0])):
        # if the docks are full at the current station
        if checkDocksFull(allData[0][x], allData) == True:
            # the, add that station ID to the list
            fullyLoadedStations.append(allData[0][x])

    # return list of stations which are fully loaded with bikes
    return "Fully loaded stations: " + ", ".join(str(x) for x in fullyLoadedStations)


def runMenu():
# Prints menu with different options for the user to choose

    # Load data
    allData=readHtml()

    # Loop through menu until user quits
    while True:
        # print options
        print("""\nWhat would you like to do?
        1. Rent a bike
        2. Return a bike
        3. Check which stations have bikes available
        4. Check certain station for number of available bikes
        5. Check which stations are full with bikes
        6. get all info for a certain station
        7. Get directions from one station to another
        8. Quit""")
        answer=input("Enter a number from the list above: ")
        
        # If user chooses "1. Rent a bike"
        if answer == "1":
            # loop runs until user enters a valid station ID
            validStation = False
            while validStation == False:
                try: # expects user to enter an integer
                    stationID=int(input("What station do you wish to rent from? "))
                except: # if user does not enter an integer
                    print("Please enter a valid station ID. ")
                    continue # loop starts again
                
                if stationID in allData[0]: # if the stationID is valid
                    validStation = True # The station entered exists, loop ends
                else:
                    # The station entered does not exist
                    print("Please enter a valid station ID. ") 

            # valid station ID was entered, so rentBike() function can be called
            # prints whether or not a bike from that station has been rented
            rentBike(stationID, allData)


        # If user chooses "2. Return a bike"
        elif answer == "2":

            # loop runs until user enters a valid station ID
            validStation = False
            while validStation == False:
                try: # expects user to enter an integer
                    stationID=int(input("What station do you wish to return your bike to? "))
                except: # if user does not enter an integer
                    print("Please enter a valid station ID. ")
                    continue # loop starts again
                if stationID in allData[0]: # if the stationID is valid
                    validStation = True # The station entered exists, loop ends
                else:
                    # The station entered does not exist
                    print("Please enter a valid station ID. ")

            # valid station ID was entered, so returnBike() function can be called
            # prints whether or not a bike from that station has been returned
            returnBike(stationID, allData)


        # If user chooses "3. Check which stations have bikes available"
        elif answer == "3":
            # Returns stations with bikes available for rent
            print(getStationsWithBikes(allData))

        # If user chooses "4. Check certain station for number of available bikes"
        elif answer == "4":

            # loop runs until user enters a valid station ID
            validStation = False
            while validStation == False:
                try: # expects user to enter an integer
                    stationID=int(input("Which specific station do you wish to check? "))
                except: # if user does not enter an integer
                    print("Please enter a valid station ID. ")
                    continue # loop starts again
                if stationID in allData[0]: # if the stationID is valid
                    validStation = True # The station entered exists, loop ends
                else:
                    # The station entered does not exist
                    print("Please enter a valid station ID. ")


            # valid station ID was entered, so we continue
            if getBikeAvailability(stationID, allData) == True:
            # there is at least one bike available at that station
                index=allData[0].index(stationID)
                # check number of bikes available at the station entered
                numBikes=allData[5][index]
                # print number of bikes:
                print("There are " + str(numBikes) + " bikes available at this station. ")
            else: # otherwise, no bikes are available at that station
                print("There are no bikes available at this station. ")

            
        # If user chooses "5. Check which stations are full with bikes"
        elif answer == "5":
            # prints list of stations which are full with bikes
            print(getFullyLoadedStations(allData))


        # If user chooses "6. get all info for a certain station"
        elif answer == "6":

            # loop runs until user enters a valid station ID
            validStation = False
            while validStation == False:
                try: # expects user to enter an integer
                    stationID=int(input("Which specific station do you wish to check? "))
                except: # if user does not enter an integer
                    print("Please enter a valid station ID. ")
                    continue # loop starts again
                if stationID in allData[0]: # if the stationID is valid
                    validStation = True # The station entered exists, loop ends
                else:
                    # The station entered does not exist
                    print("Please enter a valid station ID. ")

            # Print all info for entered station
            print(getStationInfo(stationID, allData))

            
        # If user chooses "7. Get directions from one station to another"
        elif answer == "7":
            stationID1 = 1
            stationID2 = 1

            # runs until user enters two different stations
            while stationID1 == stationID2:

                # runs until user enters valid station
                validStation1 = False 
                while validStation1 == False:
                    try: # expects user to enter integer
                        stationID1=int(input("What is your starting station? "))
                    except: #if user does not enter an integer
                        print("Please enter a valid starting station. ")
                        continue
                    if stationID1 in allData[0]: # if they enter a valid station
                        validStation1 = True
                    else:
                        print("Please enter a valid starting station. ")
                
                # same block of code, but for their ending station
                validStation2 = False 
                while validStation2 == False:
                    try:
                        stationID2=int(input("What is your end station? "))
                    except:
                        print("Please enter a valid end station. ")
                        continue
                    if stationID2 in allData[0]:
                        validStation2 = True
                    else:
                        print("Please enter a valid end station. ")

                # if they entered the same stations, go through loop again
                if stationID1==stationID2:
                    print("Please enter different station IDs.")

            # returns the direction the user must travel
            print(getDirections(stationID1, stationID2, allData))


        # If user chooses "8. Quit"
        elif answer == "8":
            exit() # quit program


        # If user enters any other number:
        else:
            print("Invalid option! ")
            # menu prints again until user chooses valid option
        
    
def main():
# Reads data and runs the menu

    readHtml() # Imports data necessary to use any other function
    runMenu() # Prints the menu, allowing the user to choose what they wish to do


if __name__=="__main__":
    # doesn't run in testing file
    main()
