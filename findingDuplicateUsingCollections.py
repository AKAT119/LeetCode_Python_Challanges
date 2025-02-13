from collections import Counter

def duplicateFind(a):
    #normalize each items, string will be lower case, others will remain same.
    normalized = [item.lower() if isinstance(item,str) else item for item in a]
    counts = Counter(normalized)


    #get the items which are occuring more that once.
    duplicate = [item for item, counts in counts.items() if counts > 1 ]
    return duplicate



a = [1, "Az", 6, 7, "az", 9, 10, 20, 6, 20]
result = duplicateFind(a)
print(result)