from difflib import SequenceMatcher
# Online Python - IDE, Editor, Compiler, Interpreter

FILE_PATH = ".\\DataSets\\AdventDay3.txt"

def getData():
        array = []
        with open(FILE_PATH) as f:   
                for line in f:
                        array.append(line)
        return array

rucksacks = rucksacks = getData()
dict = {
    'a':'1',
    'b':'2',
    'c':'3',
    'd':'4',
    'e':'5',
    'f':'6',
    'g':'7',
    'h':'8',
    'i':'9',
    'j':'10',
    'k':'11',
    'l':'12',
    'm':'13',
    'n':'14',
    'o':'15',
    'p':'16',
    'q':'17',
    'r':'18',
    's':'19',
    't':'20',
    'u':'21',
    'v':'22',
    'w':'23',
    'x':'24',
    'y':'25',
    'z':'26'}

def day3part1(): 
    dupes = []
    for rucksack in rucksacks:
        halfLength = int(len(rucksack)/2)
        compartment1, compartment2 = rucksack[:halfLength], rucksack[halfLength:]
        match = SequenceMatcher(None, compartment1, compartment2).find_longest_match()
        dupes.append(compartment1[match.a:match.a + match.size])
    return sumValueForDuplicateItems(dupes)


def day3part2():
    dupes = []
    while(len(rucksacks) > 0):
        elf1 = rucksacks.pop(0)
        elf2 = rucksacks.pop(0)
        elf3 = rucksacks.pop(0)
        elfGroup = [elf1, elf2, elf3]
        dupe = find_substr(elfGroup)
        dupes.append(dupe)
    return sumValueForDuplicateItems(dupes)


def sumValueForDuplicateItems(dupes):
    count = 0
    for dupe in dupes:
        if dupe[0].isupper() is True:
            count += (int(dict[dupe[0].lower()]) + 26)
        else:
            count += int(dict[dupe[0].lower()])
    return count

def find_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True

print(day3part1())
print(day3part2())
