"""
File contains the classes used in the PyBank calculations
"""

class ResultsContainer:
    """Object used to store the results of the calculations while processing dataset"""

    # Net total amount of "profile/losses" over the entire period of data
    netRevenue = 0.0

    # Total number of months that is included within the dataset
    totalMonths = 0

    # Total of the changes between the monthly records
    totalChange = 0.0

    # Greatest increase in profit between the monthly records
    greatestIncreaseValue = 0.0

    # Name of the month that had the greatest increase in profiles
    greatestIncreaseMonth = ""

    # Greatest losses between the monthly records
    greatestDecreaseValue = 0.0

    # Name of the month that had the greatest losses in profiles
    greatestDecreaseMonth = ""