with open('Day01/input.txt') as f:
    data = [value.rstrip() for value in f.readlines()]

data = [int(value) if value else "" for value in data] + [""]
sums_of_calories = []

while data:
    sums_of_calories.append(sum(data[:data.index('')]))
    data = data[data.index('')+1:]

print(sum(sorted(sums_of_calories)[-3:]))
