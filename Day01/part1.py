with open('Day01/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]

data = [int(value) if value else "" for value in data] + [""]
max_calories = 0

while data:
    if (calories := sum(data[:data.index('')])) > max_calories:
        max_calories = calories
    data = data[data.index('')+1:]

print(max_calories)
