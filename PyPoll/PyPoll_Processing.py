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


    #- Determine Vote Count
    #   Value of the dictionary contains the count for each candidate
    totalVotes = 0
    for sourceKey, sourceValue in candidates.items():
        totalVotes += sourceValue


    #- Calculate Statistics
    #   Store percentage of votes in dictionary that has the candidate name as key; the value is the percentage
    candidatePercentage = {}

    for sourceKey, sourceValue in candidates.items():
        candidatePercentage[sourceKey] = (sourceValue/totalVotes)

    print(candidatePercentage)
    print(totalVotes)
    print(type(candidates))
    print(candidates)



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