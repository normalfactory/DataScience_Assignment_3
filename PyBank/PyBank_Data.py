"""
File contains the classes used in the PyBank calculations
"""

class ResultsContainer:
    """Object used to store the results of the calculations while processing dataset"""

    #- Properties

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


    #- Methods
    @classmethod
    def getAverageMonthlyChange(clr):
        """ Determines the average change in the revenue; totalChange / (totalMonths - 1)
        Must subtract one from the total months as the first month has not change; nothing
        to compare it to.

        Returns: float - average monthly change
        """

        return (clr.totalChange/(clr.totalMonths -1) )
    

    @classmethod
    def addMonthlyChange(clr, previousMonthRevenue, currentMonthRevenue, currentMonthName):
        """ With the current month information provided, calculates the change in revenue and 
        determines if the month provided is the greatest increase or decrease

        Accepts:
            clr (ResultsContainer) instance of itself
            previousMonthRevenue (float) revenue from the previous month
            currentMonthRevenue (float) revenue of the current month
            currentMonthName (string) name of the current month

        Returns: nothing
        """
        
        #- Calculate change in revenue
        changeBetweenMonthRevenue = (currentMonthRevenue - previousMonthRevenue)


        #- Update running total
        clr.totalChange += changeBetweenMonthRevenue


        #- Check for greatest increase
        if (changeBetweenMonthRevenue > clr.greatestIncreaseValue):
            clr.greatestIncreaseValue = changeBetweenMonthRevenue
            clr.greatestIncreaseMonth = currentMonthName
        

        #- Check for greatest decrease
        if (changeBetweenMonthRevenue < clr.greatestDecreaseValue):
            clr.greatestDecreaseValue = changeBetweenMonthRevenue
            clr.greatestDecreaseMonth = currentMonthName


