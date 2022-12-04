FILE_PATH = ".\\DataSets\\AdventDay3.txt"

def getData():
        array = []
        with open(FILE_PATH) as f:   
                for line in f:
                        array.append(line)
        return array