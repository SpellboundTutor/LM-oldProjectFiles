'''Logan McLaughlin
Homework 6: The One About Sportsball
Helps: Python Documentation on CSV module: https://docs.python.org/3/library/csv.html'''


import csv


# def DefineYear():
#     yearParameters = False
#     while yearParameters == False:
#         baseballYear = int(input("Please input a year between 1871 and 2020."))
#         if baseballYear > 2020:
#             print(f"We don't have data for {baseballYear}. Please try again.")
#         elif baseballYear < 1871:
#             print(f"We don't have data for {baseballYear}. Please try again.")
#         else:
#             yearCheck = False
#             yearConfirm = ""
#             while yearCheck == False:
#                 yearConfirm = input(f"Accessing statistics for the year {baseballYear}. Is that correct? Please say (Y)es or (N)o.")
#                 if yearConfirm == "N" or "No":
#                     yearConfirm = True
#                     continue
#                 elif yearConfirm == "Y" or "Yes":
#                     yearConfirm = True
#                     yearParameters = True
#                 else:
#                     print(f"You entered {yearConfirm}. Sorry, I don't understand. Please try again.")
#     return(baseballYear)

def yearReader(baseballYear):
    yearTeams = []
    with open('Homework\Teams.csv', newline='') as csvfile:
        years = csv.DictReader(csvfile)
        for row in years:
            if row['yearID'] == baseballYear:
                yearTeam = row['name']
                yearTeams.append[yearTeam]
    return(yearTeams)