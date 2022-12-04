# part 2 of https://adventofcode.com/2022/day/4

import re

with open('Day04/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]


def preprocess(data):
    return (map(int, re.split('[-,]', line)) for line in data)


def isOverlapped(begin1, end1, begin2, end2):
    return not (begin1 > end2 or end1 < begin2)


data = preprocess(data)
print(sum(isOverlapped(*assignment) for assignment in data))
