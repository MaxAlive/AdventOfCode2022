with open('Day03/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]


def makeGroupsOf3(d):
    return [convertItemsToSet(d[i:i+3]) for i in range(0, len(d), 3)]


def convertItemsToSet(items):
    return [set(item) for item in items]


def getSharedBadge(elves):
    return set.intersection(*elves).pop()


def getPriority(item):
    if item.isupper():
        return ord(item) - 38
    return ord(item) - 96


data = makeGroupsOf3(data)
print(sum(getPriority(getSharedBadge(d)) for d in data))
