with open('Day03/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]


def preprocessData(d):
    return [get2Compartments(value) for value in d]


def findMiddle(string):
    return len(string) // 2


def get2Compartments(string):
    middle = findMiddle(string)
    return [set(string[:middle]), set(string[middle:])]


def getSharedItem(compartment1, compartment2):
    return compartment1.intersection(compartment2).pop()


def getPriority(item):
    if item.isupper():
        return ord(item) - 38
    return ord(item) - 96


data = preprocessData(data)
print(sum(getPriority(getSharedItem(*d)) for d in data))
