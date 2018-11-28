import bikes
"""
This is the function testing for the BikeShare project.

CISC121
Nov. 30, 2018

Joel Cross
20071213
"""

# test data set 1:
allData=[[7000, 7001, 7002],["name1", "name2", "name3"],\
        [-30.5, -10.87, 5.9],[14.7, 90.52, -81.6],[15, 10, 5],\
         [15, 6, 0],[0, 4, 5]]
stationID=7000
stationID1=7000
stationID2=7002

# function testing:
print("Test data set 1: " + str(allData))
print("Test station ID: " + str(stationID))
print()

print("Test checkDocksFull():")
print(bikes.checkDocksFull(stationID, allData))
print()

print("Test getBikeAvailability():")
print(bikes.getBikeAvailability(stationID, allData))
print()

print("Test returnBike():")
bikes.returnBike(stationID, allData)
print()

print("Test rentBike():")
bikes.rentBike(stationID, allData)
print()

print("Test getStationsWithBikes():")
print(bikes.getStationsWithBikes(allData))
print()

print("Test getDirections():")
print("For test: stationID1 is " + str(stationID1) +\
      " stationID2 is " + str(stationID2))
print(bikes.getDirections(stationID1, stationID2, allData))
print()

print("Test getStationInfo():")
print(bikes.getStationInfo(stationID, allData))
print()

print("Test getFullyLoadedStations():")
print(bikes.getFullyLoadedStations(allData))
print()
print()

print("OPPOSITE SCENARIOS:")
print()

# test data set 2:
allData=[[7000, 7001, 7002],["name1", "name2", "name3"],\
        [-30.5, -10.87, 5.9],[14.7, 90.52, -81.6],[15, 10, 5],\
         [15, 6, 0],[0, 4, 5]]
stationID=7002
stationID1=7002
stationID2=7000

# function testing:
print("Test data set 2: " + str(allData))
print("Test station ID: " + str(stationID))
print()

print("Test checkDocksFull():")
print(bikes.checkDocksFull(stationID, allData))
print()

print("Test getBikeAvailability():")
print(bikes.getBikeAvailability(stationID, allData))
print()

print("Test rentBike():")
bikes.rentBike(stationID, allData)
print()

print("Test returnBike():")
bikes.returnBike(stationID, allData)
print()

print("Test getStationsWithBikes():")
print(bikes.getStationsWithBikes(allData))
print()

print("Test getDirections():")
print("For test: stationID1 is " + str(stationID1) +\
      " stationID2 is " + str(stationID2))
print(bikes.getDirections(stationID1, stationID2, allData))
print()

print("Test getStationInfo():")
print(bikes.getStationInfo(stationID, allData))
print()

print("Test getFullyLoadedStations():")
print(bikes.getFullyLoadedStations(allData))
print()
