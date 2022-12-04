FILE_PATH = ".\\DataSets\\AdventDay1.txt"

def getData():
        array = []
        with open(FILE_PATH) as f:   
                for line in f:
                        array.append(line)
        return array

def sumCalories():
    elfCalories = getData()
    cals = []
    runningCal = 0
    while(len(elfCalories) > 0):
        currentCal = elfCalories.pop(0)
        if (currentCal == '\n'):
            cals.append(runningCal)
            runningCal = 0
        else:
            runningCal += int(currentCal)
    return cals

def day1Part1():
    return max(sumCalories())

def day1Part2():
    sum = 0
    for item in sorted(sumCalories())[-3:]:
        sum += item
    return sum


print(day1Part1())
print(day1Part2())