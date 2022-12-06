# part 2 for https://adventofcode.com/2022/day/6

with open('Day06/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]


def is14UniqueLetters(letters):
    return len(set(letters)) == 14


def findSolution(letters):
    for index in range(14, len(letters)):
        if is14UniqueLetters(letters[index-14:index]):
            return index
    return -1


print(findSolution(data[0]))
