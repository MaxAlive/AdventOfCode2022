# part 1 for https://adventofcode.com/2022/day/6

with open('Day06/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]


def is4UniqueLetters(letters):
    return len(set(letters)) == 4


def findSolution(letters):
    for index in range(4, len(letters)):
        if is4UniqueLetters(letters[index-4:index]):
            return index
    return -1


print(findSolution(data[0]))
