# Complete

file = "Day 1.txt"

# Read lines
lines = []
with open(file, 'r') as myFile:
    for line in myFile:
        lines.extend(line.split())

# lines = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234",
# "7pqrstsixteen"]

# Get individual calibration values
numberStringsLen3 = ["one", "two", "six"]
numberStringsLen4 = ["four", "five", "nine"]
numberStringsLen5 = ["three", "seven", "eight"]
calibrationStarts = []
calibrationEnds = []
for line in lines:
    start = 0
    end = len(line) - 1
    startIsDigit = False
    endIsDigit = False
    while not (startIsDigit and endIsDigit):
        if not startIsDigit:
            if line[start].isdigit():
                startIsDigit = True
                calibrationStarts.append(line[start])
            else:
                for n in range(3):
                    try:
                        if numberStringsLen3[n] in line[start:start + 3]:
                            startIsDigit = True
                            calibrationStarts.append(line[start:start + 3])
                        elif numberStringsLen4[n] in line[start:start + 4]:
                            startIsDigit = True
                            calibrationStarts.append(line[start:start + 4])
                        elif numberStringsLen5[n] in line[start:start + 5]:
                            startIsDigit = True
                            calibrationStarts.append(line[start:start + 5])
                    except:
                        pass
            if not startIsDigit:
                start += 1
        if not endIsDigit:
            if line[end].isdigit():
                endIsDigit = True
                calibrationEnds.append(line[end])
            else:
                for n in range(3):
                    try:
                        if numberStringsLen3[n] in line[end - 2:end + 1]:
                            endIsDigit = True
                            calibrationEnds.append(line[end - 2:end + 1])
                        elif numberStringsLen4[n] in line[end - 3:end + 1]:
                            endIsDigit = True
                            calibrationEnds.append(line[end - 3:end + 1])
                        elif numberStringsLen5[n] in line[end - 4:end + 1]:
                            endIsDigit = True
                            calibrationEnds.append(line[end - 4:end + 1])
                    except:
                        pass
            if not endIsDigit:
                end -= 1

    calibValue = 0
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(calibrationStarts)):
        if calibrationStarts[i].isdigit():
            calibValue += int(calibrationStarts[i]) * 10
        else:
            calibValue += 10 * (numbers.index(calibrationStarts[i]) + 1)
        if calibrationEnds[i].isdigit():
            calibValue += int(calibrationEnds[i])
        else:
            calibValue += (numbers.index(calibrationEnds[i]) + 1)

print(calibValue)
