from collections import Counter

def processLogs(logs, threshold):
    """
    input: list of strings of format: 'senderID receiverID amount'
    output: int
    description: Given a string containing transaction details, return the IDs that have transactions equal to or more than a threshold number
    """
    l = []
    for log in logs:
        if log.split()[0]==log.split()[1]: # if same ID in both roles ignore 1
            l.append(log.split()[0])
        else:
            l.append(log.split()[0])
            l.append(log.split()[1])
    freq = Counter(l)
    # get IDs where freq more
    result = list(map(int,[i for (i,k) in freq.items() if k>=threshold])) 
    # sort them
    result.sort()
    return(result) 

processLogs(["30 99 12", "30 20 1", "12 100 2", "20 80 22"], 2)
