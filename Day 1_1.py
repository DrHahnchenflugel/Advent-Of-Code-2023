# Complete

file = "Day 1.txt"

# Read lines
lines = []
with open(file, 'r') as myFile:
    for line in myFile:
        lines.extend(line.split())

# Get individual calibration values
calibrations = []
for line in lines:
    start = 0
    end = len(line) - 1
    while line[start].isalpha() or line[end].isalpha():
        if line[start].isalpha():
            start += 1
        if line[end].isalpha():
            end -= 1

    # string addition of start, end
    calibrations.append(int(line[start] + line[end]))

# Final result
print(sum(calibrations))
