'''
Author: Reilly Parent (R3IXY)
Copyright (c) Reilly Parent 2021

https://r3ixy.com/
'''

import sys
import os

def verifyArg(arg):
    startQuote = arg.startswith("\"") or arg.startswith("'")
    endQuote = arg.endswith("\"") or arg.endswith("'")
    return (not startQuote and not endQuote) or (startQuote and endQuote)

def preprocessLine(line, preprocs):
    newLine = line.rstrip()
    for search, replace in preprocs.items():
        newLine = newLine.replace(search, replace)
    return newLine

# gather preproc lines
def readPreprocessorDirectives(inLines):
    preprocs = {}
    for line in inLines:
        line = line.rstrip()
        if line.startswith("#def "):
            data = line.split()
            if not len(data) == 3:
                print(f"Preprocessor directive {line} is not set up correctly. An example of a correct directive is:\n\t#def a \"b\"\nSkipping this one.")
                continue
            if verifyArg(data[2]):
                preprocs[data[1]] = data[2]
            else:
                print(f"{data[2]} found in preprocessor diretive must either be fully surrounded by single/double quotes or not quoted at all. Skipping this one.")
                continue
    return preprocs

# preprocess all lines
def preprocessLines(inLines, preprocs):
    outLines = []
    for line in inLines:
        line = line.rstrip()
        if not line.startswith("#def "):
            outLines.append(preprocessLine(line, preprocs))
    return outLines

def runPreprocessedFile():
    print("==PROGRAM OUTPUT===================================")
    os.system("python3 temp1112.py")
    if "--proc" in sys.argv:
        print("==REGISTERED PREPROCESSOR DIRECTIVES===============")
        print("\n".join([f"{x}\t->\t{y}" for x, y in preprocs.items()]))
    if "--show" in sys.argv:
        print("==PREPROCESSED PYTHON FILE=========================")
        os.system("cat temp1112.py")
    if "--orig" in sys.argv:
        print("==ORIGINAL FILE====================================")
        os.system(f"cat {sys.argv[1]}")
    os.system("rm temp1112.py")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        inFile = open(sys.argv[1], "r")
        inLines = inFile.readlines()
        inFile.close()

        preprocs = readPreprocessorDirectives(inLines)
        outLines = preprocessLines(inLines, preprocs)

        outFile = open("temp1112.py", "w")
        outFile.write("\n".join(outLines) + "\n")
        outFile.close()

        runPreprocessedFile()
    else:
        print("Invalid command syntax. Example usage:\n\tpiethon example.py [--show] [--proc] [--orig]\n")
