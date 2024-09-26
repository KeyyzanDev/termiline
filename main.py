import os

def centerX(str, adjust=0):
    consoleColums = os.get_terminal_size().columns
    currentLongerLine = 0
    for line in str.splitlines():
        if len(line) > currentLongerLine:
            currentLongerLine = len(line)

    if consoleColums > currentLongerLine:
        spaceToAdd = " "*int(((consoleColums-currentLongerLine)/2)+adjust)
        finalString = ""
        for line in str.splitlines():
            finalString = finalString + spaceToAdd + line + "\n"
            print(consoleColums, currentLongerLine)

        return finalString
    else:
        return str
    
def centerY(str, uadjust=0, dadjust=0):
    consoleLines = os.get_terminal_size().lines
    amountOfUsedLines = 0
    for line in str.splitlines():
        amountOfUsedLines += 1

    if consoleLines > amountOfUsedLines:
        spaceToAddU = int((consoleLines-amountOfUsedLines)/2)+uadjust
        spaceToAddD = int((consoleLines-amountOfUsedLines)/2)+dadjust
        finalString = ""
        for i in range (0, spaceToAddU):
            finalString = finalString + "\n" + " "

        finalString = finalString + str

        for i in range (0, spaceToAddD):
            finalString = finalString + "\n" + " "

        return finalString
    else:
        return str

def alignRight(str, ladjust=0):
    consoleColums = os.get_terminal_size().columns
    currentLongerLine = 0
    for line in str.splitlines():
        if len(line) > currentLongerLine:
            currentLongerLine = len(line)

    if consoleColums > currentLongerLine:
        spaceToAdd = " "*(consoleColums - currentLongerLine + ladjust)
        finalString = ""
        for line in str.splitlines():
            finalString = finalString + spaceToAdd +  line + "\n"
        
        return finalString

    else:
        return str