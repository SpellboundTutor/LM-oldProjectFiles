'''Logan McLaughlin
Homework 8: Bat-Shark Detector 2023
Helps Used:'''

#Modules

from graphics import * #Graphics module
import random as rand #Random module

#Initialization

x = int(0)
y = int(0)
n = int(50) #quantity of points
i = int(0) #counter of while loop
m = [1024,1024] #window size (x,y)
nm = [0,0]
pointList = []
pointSecList = []
pointTerList = []

#Random Coordinate Generation

while i < n: #Generating our points
        x = rand.randint(0, m[0]-1) #randomly generates and stores x-coord
        y = rand.randint(0, m[1]-1) #randomly generates and stores y-coord
        pointList.append([x,y])
        i += 1 #Increases the counter by 1

# print(pointList) #Prints master coord list. For troubleshooting only.

minX = int(m[0]) #Min X value in list. Initialized to screen width.
minY = int(m[1]) #Min Y value in list. Initialized to screen height.
maxX = int(0) #Max X value in list. Initialized to 0.
maxY = int(0) #Max Y value in list. Initialized to 0.

for u in range(len(pointList)): #Determining Min and Max values of list.
    if pointList[u][0] < minX:
          minX = pointList[u][0]
    if pointList[u][0] > maxX:
          maxX = pointList[u][0]
    if pointList[u][1] < minY:
          minY = pointList[u][1]
    if pointList[u][1] > maxY:
          maxY = pointList[u][1]

avgX = int(0) #Initialize Average X values
avgY = int(0) #Initialize Average Y values

avgX = ((maxX + minX) / 2) #Calculates average X value given Min and Max X values
avgY = ((maxY + minY) / 2) #Calculates average Y value given Min and Max Y values

win = GraphWin("Bat-Shark Detector 2023", m[0], m[1])
win.setCoords(0,0,m[0],m[1])
point = 0
for u in range(len(pointList)):
      point = win.plot(pointList[u][0], pointList[u][1])
      point.draw(win)

win.getMouse()
win.close()


# if avgX > avgY:
#       win.Rectangle(Point(avgX, minY), Point(maxX, maxY))
# else:
#       win.Rectangle(Point(minX, avgY), Point(maxX, maxY))
