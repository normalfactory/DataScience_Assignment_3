# PyBank Challenge
#   This script is used to analyze the financial records for a company, using
#   records found within .CSV file.  The script reads in the values, calculates
#   the financial results, prints these results and publishes the results to file.
#   Code attempts to use classes and functions.
#   
#   Scott McEachern
#   February 3, 2019


#- Classes
# class ResultsContainer:
#     # Purpose : Object used to store the results of the calculations while processing dataset

#     # Net total amount of "profile/losses" over the entire period of data
#     netRevenue = 0.0

#     # Total number of months that is included within the dataset
#     totalMonths = 0

#     # Total of the changes between the monthly records
#     totalChange = 0.0

#     # Greatest increase in profit between the monthly records
#     greatestIncreaseValue = 0.0

#     # Name of the month that had the greatest increase in profiles
#     greatestIncreaseMonth = ""

#     # Greatest losses between the monthly records
#     greatestDecreaseValue = 0.0

#     # Name of the month that had the greatest losses in profiles
#     greatestDecreaseMonth = ""



#- Methods

# def startProcessing():
    # Purpose : Starting function for the processing
    
    #- Provide User Information on start
    # print("->------")
    # print(" PyBank Challenge")
    # print(" ")


    # #- Reference Dataset
    # path = os.path.join("./Resources", )



    # test = ResultsContainer

    # test.netRevenue = 10.0

    # test.netRevenue = test.netRevenue + 3.0

    # print("Test Test")
    # print(test.netRevenue)



#- Start
#   Starting location of the script; the classes/functions above so that they are compiled and 
#   available for use
# import PyBank_Data
import PyBank_Processing as po

po.start()
# startProcessing()
