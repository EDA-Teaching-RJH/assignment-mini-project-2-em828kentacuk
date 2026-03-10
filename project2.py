import re
import os
import sys
import random

# imports all the functions from the other files

class Barista:

    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
        pay = 0
        # initializes the Barista class with a name and pay, and sets pay to 0
        if not name:
            raise ValueError("Name cannot be empty")


        



def main():

    if len(sys.argv) < 2:
        print("Please enter an argument")
        sys.exit()
# tells user to enter an argument if they don't and then exits the program
    
input = sys.argv[1].lower()
# takes the first argument and converts it to lowercase

if __name__ == "__main__":
    main()
