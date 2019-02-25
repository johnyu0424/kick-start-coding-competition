# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051060/00000000000588f4
import sys, random

def doGuess(lowerEnd, upperEnd, maxTries):
    tries = 0 # how many times we have tried
    while tries < maxTries:
        guess = random.randint(lowerEnd + 1, upperEnd) # our guess
        print(guess, flush=True)
        response = input() # system's response
        print("{0} {1}".format(guess, response), file=sys.stderr)

        if response == "TOO_SMALL":
            lowerEnd = guess
        elif response == "TOO_BIG":
            upperEnd = guess
        elif response == "CORRECT":
            break

        tries += 1 

def start():
    numTests = int(input()) # T
    for test in range(1, numTests + 1):
        print(test)
        abStr = input()
        abList = abStr.split(" ")
        lowerEnd = int(abList[0]) # A
        upperEnd = int(abList[1]) # B
        maxTries = int(input()) # N
        doGuess(lowerEnd, upperEnd, maxTries)

start()