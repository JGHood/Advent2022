FILE_PATH = ".\\DataSets\\AdventDay4.txt"

def getData():
        array = []
        with open(FILE_PATH) as f:   
                for line in f:
                        array.append(line.strip('\n'))
        return array

def toInt(num):
        return int(num)

def day4Part1():
        count = 0 
        pairs = getData()
        for pair in pairs:
                pair1, pair2 = pair.split(",")
                pair1Nums = pair1.split("-")
                pair2Nums = pair2.split("-")
                if ((int(pair1Nums[0]) <= int(pair2Nums[0]) and int(pair1Nums[1]) >= int(pair2Nums[1])) or (int(pair2Nums[0]) <= int(pair1Nums[0]) and int(pair2Nums[1]) >= int(pair1Nums[1]))):
                        count+= 1
        return count

def day4Part2():
        count = 0 
        pairs = getData()
        for pair in pairs:
                pair1, pair2 = pair.split(",")
                pair1Nums = list(map(toInt, pair1.split("-")))
                pair2Nums = list(map(toInt, pair2.split("-")))
                if ((pair1Nums[0] <= pair2Nums[0] <= pair1Nums[1]) or (pair1Nums[0] <= pair2Nums[1] <= pair1Nums[1]) or (pair2Nums[0] <= pair1Nums[0] <= pair2Nums[1]) or (pair2Nums[0] <= pair1Nums[1] <= pair2Nums[1])):
                        count+= 1
        return count

print(day4Part2())