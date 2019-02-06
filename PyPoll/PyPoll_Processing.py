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


    #- Gather Results
    candidates = readDataset()


    #- Determine Statistics
    resultContainer = calculateResults(candidates)

    print(type(resultContainer))
    print(resultContainer)

    #- Determine Vote Count
    #   Value of the dictionary contains the count for each candidate
    # totalVotes = 0
    # for sourceKey, sourceValue in candidates.items():
    #     totalVotes += sourceValue


    # #- Calculate Statistics
    # #   Store percentage of votes in dictionary that has the candidate name as key; the value is the percentage
    # candidatePercentage = {}

    # for sourceKey, sourceValue in candidates.items():
    #     candidatePercentage[sourceKey] = (sourceValue/totalVotes)

    # print(candidatePercentage)
    # print(totalVotes)
    # print(type(candidates))
    # print(candidates)

def calculateResults(candidates):
    """
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