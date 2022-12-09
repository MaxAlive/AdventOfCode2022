# part 2 for https://adventofcode.com/2022/day/9

with open('Day09/input.txt') as f:
    data = [value.rstrip().split(' ') for value in f.readlines()]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def getUnitValue(self, value):
        if value:
            return value // abs(value)
        return 0

    def getDirection(self, other):
        return Point(self.getUnitValue((other - self).x), self.getUnitValue((other - self).y))

    def isNeighbour(self, other):
        temp = other - self
        return temp in (Point(0, -1), Point(0, 1), Point(1, -1), Point(1, 0), Point(1, 1), Point(-1, -1), Point(-1, 0), Point(-1, 1))

    def __str__(self):
        return f'Point({self.x}, {self.y})'


directions = {'U': Point(0, -1), 'D': Point(0, 1),
              'R': Point(1, 0), 'L': Point(-1, 0)}


def move(point, direction):
    return point + direction


def moveTail(tail, head):
    return move(tail, tail.getDirection(head))


def simulate(knots, direction):
    knots[0] = move(knots[0], directions[direction])

    for i in range(1, len(knots)):
        if not knots[i-1].isNeighbour(knots[i]):
            knots[i] = moveTail(knots[i], knots[i-1])

    return knots


head_movements = data
knots = [Point(0, 0)] * 10
visited = set()

for direction, steps in head_movements:
    for _ in range(int(steps)):
        knots = simulate(knots, direction)
        visited.add((knots[-1].x, knots[-1].y))

print(len(visited))
