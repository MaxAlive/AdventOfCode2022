# part 1 of https://adventofcode.com/2022/day/4

import re

with open('Day04/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]


def preprocess(data):
    return (map(int, re.split('[-,]', line)) for line in data)


def isContained(begin1, end1, begin2, end2):
    return (begin1 <= begin2 and end1 >= end2) or (begin1 >= begin2 and end1 <= end2)


data = preprocess(data)
print(sum((isContained(*assignment) for assignment in data)))
