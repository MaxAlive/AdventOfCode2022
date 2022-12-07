# part 1 for https://adventofcode.com/2022/day/7

with open('Day07/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = {}
        self.files = {}

    def getSize(self):
        return sum((f.size for f in self.files.values())) + sum((child.getSize() for child in self.children.values()))

    def appendDir(self, newDirectory):
        self.children[newDirectory.name] = newDirectory

    def appendFile(self, newFile):
        self.files[newFile.name] = newFile


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def moveToDir(current_directory, target_directory):
    if target_directory == "..":
        return current_directory.parent
    if target_directory == '/':
        while current_directory.parent:
            current_directory = current_directory.parent
        return current_directory
    return current_directory.children[target_directory]


def parseInput():
    return [d.split(" ") for d in data]


def walkThroughInput(current_directory):
    for line in data:
        if line[:2] == ["$", "cd"]:
            current_directory = moveToDir(current_directory, line[2])
        elif line[0] == "dir":
            if line[1] not in current_directory.children.keys():
                current_directory.appendDir(
                    Directory(line[1], current_directory))
        elif line[0].isnumeric():
            current_directory.appendFile(File(line[1], int(line[0])))


def listAllDirectories(current_directory):
    visited = set()
    next_directories = [current_directory]

    while next_directories:
        for child in next_directories[0].children.values():
            if child not in visited:
                next_directories.append(child)
        visited.add(next_directories.pop(0))

    return visited


if __name__ == "__main__":
    data = parseInput()
    current_directory = Directory('/', None)

    walkThroughInput(current_directory)

    print(sum(d.getSize() for d in listAllDirectories(
        current_directory) if d.getSize() < 100000))
