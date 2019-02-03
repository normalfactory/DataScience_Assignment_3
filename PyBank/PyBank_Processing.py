""" Contains the processing for the PyBank assignment; separate functions for different components

Scott McEachern
"""


def start():
    """ Starting point for the function"""

    import PyBank_Data


    #- Provide User Information on start
    print(" ")
    print("->------")
    print(" PyBank Challenge")
    print(" ")


    #- Prepare Results
    resultsInfo = readDataset()


    #- Print Results
    displayResultsOnConsole(resultsInfo)



def displayResultsOnConsole(resultsInfo):
    """ Displays the results of the calculations on the console
    Accepts : resultInfo (PyBank_Data.ResultContainer) Holds the results of the calculations from dataset
    """
    import PyBank_Data

    print(" ")
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {resultsInfo.totalMonths}")
    print(f"Total: ${'{:,.2f}'.format(resultsInfo.netRevenue)}")
    print(f"Average Change: ${'{:,.2f}'.format(resultsInfo.getAverageMonthlyChange())}")

    print(f"Greatest Increase in Profits: {resultsInfo.greatestIncreaseMonth} (${'{:,.2f}'.format(resultsInfo.greatestIncreaseValue)})")

    print(f"Greatest Decrease in Profits: {resultsInfo.greatestDecreaseMonth} (${'{:,.2f}'.format(resultsInfo.greatestDecreaseValue)})")

    print(" ")



def readDataset():
    """ Reads through the dataset and does the calcualtions for the revenue
        Returns: PyBank_Data.ResultContainer, has the results
    """
    import os
    import csv
    import PyBank_Data

    #- Prepare Results
    resultsInfo = PyBank_Data.ResultsContainer


    #- Get Dataset
    previousMonthRevenue = 0.0

    path = os.path.join(".",  "Resources", "budget_data.csv")

    with open(path, 'r') as sourceFile:
        sourceReader = csv.reader(sourceFile, delimiter=',')

        # Skip header of text file
        header = next(sourceReader)


        for row in sourceReader:

            # Update counter of months
            resultsInfo.totalMonths += 1


            # Get current revenue
            currentMonthRevenue = float(row[1])
            currentMonthName = row[0]


            # Determine change between months
            if (resultsInfo.totalMonths > 1):
                resultsInfo.addMonthlyChange(previousMonthRevenue, currentMonthRevenue, currentMonthName)


            # Total net amount
            resultsInfo.netRevenue += currentMonthRevenue


            # Set Previous Month Revenue
            #   Used next loop
            previousMonthRevenue = currentMonthRevenue


    return resultsInfo