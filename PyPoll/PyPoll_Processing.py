"""
Contains processing for the PyPoll assignment

Scott McEachern
"""

def start():
    """ Start of the processing of the election results """

    #- Provide User Information on start
    print(" ")
    print("->------")
    print("PyPoll Challenge")
    print(" ")
    print("Calculating results...")


    #- Gather Results
    candidates = readDataset()


    #- Determine Statistics
    resultContainer = calculateResults(candidates)


    #- Print Results to Console
    printResultsToConsole(resultContainer)


    #- Store Results to Disk
    saveResultsToFile(resultContainer)

    
def saveResultsToFile(resultsContainer):
    """ Using the dictionary provided, stores the results to a file in the Resources/Election_Results.csv with the 
    columns of 'Candidate', 'VoteCount', 'VotePercentage'

    Accepts : resultContainer (Dictionary) holds the results of the calculations
                key- totalvotes     value: (int) number of votes
                key- winner         value: (str) name of the candidate that won; had most votes
                key- candidates     value: (list) list of the candidates; dictionary object with the following:
                                                key: name   value: (str) name of the candiate, in title case
                                                key: count  value: (int) total number of votes of the candidate
                                                key: percentage  value: (numeric) percentage of the votes
    """
    
    import csv
    import os


    #- Create Path
    path = os.path.join(".", "Resources", "Election_Results.csv")


    #- Create File
    with open(path, 'w', newline='') as sourceFile:

        # Create Writer
        sourceWriter = csv.writer(sourceFile, delimiter=",")

        # First Row of Headers
        sourceWriter.writerow(["Candidate", "VoteCount", "VotePercentage"])

        # Write Row for each candidate
        for candidateInfo in resultsContainer["candidates"]:
            candidateRow = [candidateInfo['name'], candidateInfo['count'], candidateInfo['percentage'] ]

            sourceWriter.writerow(candidateRow)
    
    print("Completed file to disk; Election_Results.csv")
    print(" ")


def printResultsToConsole(resultContainer):
    """ Using the dictionary provided, prints the results of the election to the console

    Accepts : resultContainer (Dictionary) holds the results of the calculations
                key- totalvotes     value: (int) number of votes
                key- winner         value: (str) name of the candidate that won; had most votes
                key- candidates     value: (list) list of the candidates; dictionary object with the following:
                                                key: name   value: (str) name of the candiate, in title case
                                                key: count  value: (int) total number of votes of the candidate
                                                key: percentage  value: (numeric) percentage of the votes
    """

    #- Print Header
    print(" ")
    print(" ")
    print("Election Results")
    print("----------------------------")

    #- Print Total Votes
    print(f"Total Votes: {'{:,}'.format(resultContainer['totalvotes'])}")
    print("----------------------------")


    #- Print Candidate Results
    for candidateInfo in resultContainer["candidates"]:

        print(f"{candidateInfo['name']}: {'{:.2f}'.format(candidateInfo['percentage'])}%  ({'{:,}'.format(candidateInfo['count'])})")

    
    #- Print Winner
    print("----------------------------")
    print(f"Winner: {resultContainer['winner']}")
    print("----------------------------")
    print(" ")



def calculateResults(candidates):
    """ Calculates the total votes, winner and percentage of each of the candidates.  Package the results in dictionary.

    Accepts :
        candidates (dictionary) holds the information from the dataset; key- candidate name in lower case value - number of votes
    
    Returns : Dictionary holds the results of the caclulations so that it can be displayed and printed
                key- totalvotes     value: (int) number of votes
                key- winner         value: (str) name of the candidate that won; had most votes
                key- candidates     value: (list) list of the candidates; dictionary object with the following:
                                                key: name   value: (str) name of the candiate, in title case
                                                key: count  value: (int) total number of votes of the candidate
                                                key: percentage  value: (numeric) percentage of the votes 
    """

    #- Determine Vote Count and Winner
    #   Loop through the dictionary that contains the count for each candidate
    totalVotes = 0
    winnerTotalVotes = 0
    winnerCandidate = ""

    for sourceKey, sourceValue in candidates.items():
        # Total Votes
        totalVotes += sourceValue

        # Determine Winner
        if (sourceValue > winnerTotalVotes):
            winnerTotalVotes = sourceValue
            winnerCandidate = sourceKey.title()


    #- Determine Percentage
    candidateResults = []

    for sourceKey, sourceValue in candidates.items():

        result = {}
        result["name"] = sourceKey.title()
        result["count"] = sourceValue
        result["percentage"] = ((sourceValue/totalVotes) * 100)

        candidateResults.append(result)


    #- Package Results
    resultsContainer = {}

    # Total Count
    resultsContainer["totalvotes"] = totalVotes

    # Winner
    resultsContainer["winner"] = winnerCandidate

    # Candidates
    resultsContainer["candidates"] = candidateResults


    return resultsContainer



def readDataset():
    """" Reads through the dataset, election_data.csv, and determines the election results that are stored
    within a dictionary.

    Returns: Dictionary, key is the candidates name, lower case  and value is the number of records the candidate received
    """

    import os
    import csv


    #- Prepare Path
    path = os.path.join(".", "Resources", "election_data.csv")


    #- Create dictionary of candidates; key is the candidates name, value is the count
    candidates = {}


    with open(path, 'r') as sourceFile:

        # Open Reader
        sourceReader = csv.reader(sourceFile, delimiter=",")


        # Skip Header
        next(sourceReader)


        # Loop through rows
        for sourceRow in sourceReader:

            # Get Candidate Name
            candidateName = sourceRow[2]

            # Search dictionary for candidate name; found add vote
            hasCandidate = False
            for sourceKey, sourceValue in candidates.items():
                if (sourceKey == candidateName.lower()):
                    hasCandidate = True
                    candidates[sourceKey] = sourceValue + 1

            # Candidate not found in dictionary; add item and set single vote
            if (hasCandidate == False):
                candidates[candidateName.lower()] = 1


    return candidates