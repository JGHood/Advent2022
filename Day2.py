FILE_PATH = ".\\DataSets\\AdventDay2.txt"

def getData():
        array = []
        with open(FILE_PATH) as f:   
                for line in f:
                        array.append(line.strip('\n'))
        return array

def getPt1WinnerPoints(choices):
    #Rock: 1 pt A X
    #Paper: 2 pt B Y
    #Scissors: 3 pt C Z
    #Tie: 3pt
    #Win: 6pt
    switch = {
        'A X': 3, #tie
        'A Y': 6, #win
        'A Z': 0, #lose
        'B X': 0, #lose
        'B Y': 3, #tie
        'B Z': 6, #win
        'C X': 6, #win
        'C Y': 0, #lose
        'C Z': 3, #tie
    }
    return switch.get(choices)

def getPart1ChoicePoints(choice):
    if (choice == 'X'):
        return 1
    if (choice == 'Y'):
        return 2
    if (choice == 'Z'):
        return 3


def getPt2ChoicePoints(choices):
    switch = {
    'A X': 3, #lose rock = S
    'A Y': 1, #tie rock = R
    'A Z': 2, #win rock = P
    'B X': 1, #lose paper = R
    'B Y': 2, #tie paper = P
    'B Z': 3, #win paper = S
    'C X': 2, #lose scissors = P
    'C Y': 3, #tie scissors = S
    'C Z': 1, #win scissors = R
    }
    return switch.get(choices)

def getPt2WinnerPoints(my_choice):
    switch = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }
    return switch.get(my_choice)


def day2Part1(): 
    games = getData()
    totalSum = 0
    for game in games: 
        totalSum += getPt1WinnerPoints(game)
        my_choice = game.split(" ")[1:][0]
        totalSum += getPart1ChoicePoints(my_choice)
    return totalSum

def day2Part2():
    games = getData()
    totalSum = 0
    for game in games: 
        my_choice = game.split(" ")[1:][0]
        totalSum += getPt2WinnerPoints(my_choice)
        totalSum += getPt2ChoicePoints(game)
    return totalSum



print(day2Part1())
print(day2Part2())
  