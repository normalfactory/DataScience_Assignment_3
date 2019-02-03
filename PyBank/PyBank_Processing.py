# Purpose : 


def start():
    """ Starting point for the function"""

    import PyBank_Data


    #- Provide User Information on start
    print("->------")
    print(" PyBank Challenge")
    print(" ")


    #- Prepare Results
    resultsInfo = readDataset()


    #- Print Results
    displayResultsOnConsole(resultsInfo)

    # print(f"Total Months: {resultsInfo.totalMonths}")
    # print(f"Total net revenue: {resultsInfo.netRevenue}")
    # test = PyBank_Data.ResultsContainer

    # test.totalMonths = 9

    # print(test.totalMonths)
    # PyBank_Data.ResultsContainer


def displayResultsOnConsole(resultsInfo):
    """ Displays the results of the calculations on the console
    Accepts : resultInfo (PyBank_Data.ResultContainer) Holds the results of the calculations from dataset
    """
    import PyBank_Data

    print(" ")
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {resultsInfo.totalMonths}")
    print(f"Total: ${'{:.2f}'.format(resultsInfo.netRevenue)}")



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
    path = os.path.join(".",  "Resources", "budget_data.csv")

    with open(path, 'r') as sourceFile:
        sourceReader = csv.reader(sourceFile, delimiter=',')

        # Skip header of text file
        header = next(sourceReader)


        for row in sourceReader:

            # Update counter of months
            resultsInfo.totalMonths += 1

            # Total net amount
            resultsInfo.netRevenue += float(row[1])



    return resultsInfo