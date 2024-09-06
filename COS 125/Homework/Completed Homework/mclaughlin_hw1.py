'''
Logan McLaughlin
Homework 1: The Garden Plot Exercise
Helps used:
1.) GeeksforGeeks "Loops in Python" By Unknown / 13 Apr, 2023 https://www.geeksforgeeks.org/loops-in-python/
2.) AskPython "How To Use goto/label In Python3?" By Snehal Gokhale / June 10, 2023 https://www.askpython.com/python/examples/goto-label-python3
3.) StackOverflow "Python | TypeError: unsupported operand type(s) for /: 'NoneType' and 'int' |use Variable to divide" https://stackoverflow.com/questions/72688157/python-typeerror-unsupported-operand-types-for-nonetype-and-int-use

Other Notes: I did actively try to use While loops and Functions to replace what I understood to be Label and Goto commands to circumvent the assumptions
in the homework and show off, but I ran out of time to figure out how to get the blasted thing to work. Was also trying to figure out a way to clear print
lines in order to keep the border in view and only show immediately relevant information while collecting inputs, but I could not get it to work. Ah well!
'''

##Establishing Base and Constant Variables##

sizeOnions = 10*10 #10x10 Centimeters. We will be operating in meters, so ensure the necessary multipliers are there, self!
sizeSpinach = 16*16 #16x16 Centimeters.
sizeLettuce = 30*30 #30x30 Centimeters.
sizePeppers = 38*38 #38x38 Centimeters.

##Stereotypically gaudy ASCII beautification##

prettyBorderTop = "x-+-x-+-x-+-x-+-x-+-x-+-x-+-x-+-x-+-x-+-x-+-x-+-x" #Tried to figure out how to duplicate just "x-+-", but couldn't get that to work.
prettyBorderSides = "|" #Couldn't quite figure out how to avoid making this a variable. C'est la vie.
prettyBorderTitle = "Intensive Gardening Square Calculator" #The title of our calculator. I was going to go with something clever and punny, but... KISS method this time.
totalBorderLine = "==================================================================" #Same as the BorderTop, I wanted to just have something that repeated over and over, but couldn't figure it out.
print(f"{prettyBorderTop:20}\n" f"{prettyBorderSides:<5} {prettyBorderTitle:5} {prettyBorderSides:>5}\n" f"{prettyBorderTop:30}\n") #Pretty border nonsense. Yay!

##User Input and Value Checks##
plotHeight = float(input('What is the height of the plot (in meters)?\n')) #Retrieving the height of the plot
plotWidth = float(input('What is the width of the plot (in meters)?\n')) #Retrieving the width of the plot
sizePlot = plotHeight * plotWidth #Getting our square meters... meterage? Anyway, converting plotHeight and plotWidth to Square Meters.
percentOnion = float(input('What percentage of this plot will be onions?\n(Please write percentages as a decimal value with up to 2 decimal places.)\n')) #Retrieving the percentage of onions for the plot.
percentSpinach = float(input('What percentage of this plot will be spinach?\n(Please write percentages as a decimal value with up to 2 decimal places.)\n')) #Retrieving the percentage of spinach for the plot.
percentLettuce = float(input('What percentage of this plot will be lettuce?\n(Please write percentages as a decimal value with up to 2 decimal places.)\n')) #Retrieving the percentage of lettuce for the plot.
percentPeppers = float(input('What percentage of this plot will be peppers?\n(Please write percentages as a decimal value with up to 2 decimal places.)\n')) #Retrieving the percentage of peppers for the plot.
percentTotal = (percentOnion + percentSpinach + percentLettuce + percentPeppers) #Getting the percentages tabulated for the totals. Was originally going to use this for a check to ensure the totals equaled 1.0, but scrapped the idea when I couldn't make it work. Unused Variable.

totalOnion = sizePlot * percentOnion #How much of the total plot will be onions. I detest onions.
totalSpinach = sizePlot * percentSpinach #How much of the total plot will be spinach.
totalLettuce = sizePlot * percentLettuce #How much of the total plot will be lettuce.
totalPeppers = sizePlot * percentPeppers #How much of the total plot will be peppers.

plotOnions = round((totalOnion / sizeOnions)*100, 2) #How many total revolting onion things go into the assigned square meterage (I'm sticking with meterage) of the garden plot.
plotSpinach = round((totalSpinach / sizeSpinach)*100, 2) #How many total spinach plants go into the assigned square meterage.
plotLettuce = round((totalLettuce / sizeLettuce)*100, 2) #How many total lettuce plants go into the assigned square meterage.
plotPeppers = round((totalPeppers / sizePeppers)*100, 2) #How many total pepper plants go into the assigned square meterage.

print(f"With the values provided, your garden plot of {plotHeight} x {plotWidth} meters, or {sizePlot} square meters, you should be able to find room for:\n {totalBorderLine}\n {plotOnions:10} Onion Crops within {totalOnion} square meters.\n {plotSpinach:10} Spinach Crops within {totalSpinach} square meters.\n {plotLettuce:10} Lettuce Crops in {totalLettuce} square meters.\n {plotPeppers:10} Pepper Crops in {totalPeppers} square meters.\n {totalBorderLine}\n Thank you very much for using this calculator! Have a wonderful day!")
#The above line is incredibly long, so comment here so it's visible! This returns all the values as output to the user to be displayed in a less fancy, but still functional bordered and readable format.

##Variable Troubleshooting##
'''
print(f"PercentOnion: {percentOnion}")
print(f"percentSpinach: {percentSpinach}")
print(f"percentLettuce: {percentLettuce}")
print(f"percentPeppers: {percentPeppers}")
print(f"percentTotal: {percentTotal}")'''

