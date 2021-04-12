import sys
import math
import random

def add():
    if len(sys.argv) > 1:
        string=sys.argv[1]
        if string.upper().isupper():
            print("invalid")
        else:
            numbers=[]
            ID=0
            moveOn=True
            for letter in string:
                if letter.isdigit() and moveOn == False:
                    numbers[ID]=numbers[ID]+letter
                if letter.isdigit() and moveOn == True:
                    numbers.insert(ID, letter)
                    moveOn=False
                if letter == "+" and moveOn == False:
                    ID=ID+1
                    moveOn=True
            print(ID, numbers)
            result=0
            for item in numbers:
                result=result+int(item)
            print(result)
    else:
        print("invalid")

add()