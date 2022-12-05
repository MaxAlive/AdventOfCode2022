# part 2 for https://adventofcode.com/2022/day/5

from collections import defaultdict, deque
from parse import parse, compile

with open('Day05/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]


def splitDataInParts():
    blank_line = data.index('')
    commands = data[blank_line+1:]
    boxes = data[:blank_line-1]

    return boxes, commands


def getboxDict(boxes):
    boxDict = defaultdict(deque)

    for row in boxes:
        current_stack = 1
        while row:
            if (box := row[1]) != ' ':
                boxDict[current_stack].appendleft(box)
            row = row[4:]
            current_stack += 1
        current_stack = 0

    return boxDict


def getCommandList(commands):
    pattern = compile("move {:d} from {:d} to {:d}")

    return [list(pattern.parse(c)) for c in commands]


def moveBoxes(boxDict, commandList):
    for command in commandList:
        boxDict[command[1]].rotate(command[0])
        for _ in range(command[0]):
            boxDict[command[2]].append(boxDict[command[1]].popleft())


def getSolution(boxDict):
    return ("").join([boxDict[stack+1].pop() for stack in range(len(boxDict))])


if __name__ == "__main__":
    boxes, commands = splitDataInParts()
    boxDict = getboxDict(boxes)
    commandList = getCommandList(commands)
    moveBoxes(boxDict, commandList)
    print(getSolution(boxDict))
