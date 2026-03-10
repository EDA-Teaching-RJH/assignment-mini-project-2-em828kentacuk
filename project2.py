import re
import os
import sys
import random


# imports all the functions from the other files

class Barista:

    def __init__(self, name, pay):

        if not name:
            raise ValueError("Name cannot be empty")
        if pay < 0:
            raise ValueError("Pay cannot be negative")
        # checks if the name is empty or if the pay is negative, and raises an error

        self.name = name
        self.pay = pay
        self.pay = 0
        # initializes the Barista class with a name and pay, and sets pay to 0

class Novice(Barista):
    def __init__(self, name, pay):
        super().__init__(name, pay)
        self.pay = 12.5


class Intermediate(Barista):
    def __init__(self, name, pay):
        super().__init__(name, pay)
        self.pay = 14.5

class Expert(Barista):
    def __init__(self, name, pay):
        super().__init__(name, pay)
        self.pay = 17.5

"""
to run the script type into command terminal:
    python3 project2.py add                 — Add a new barista to the system
    python3 project2.py list                — List all baristas
    python3 project2.py managers            — List all managers
    python3 project2.py assign shifts       — Assign shifts to baristas and calculate their pay
"""

def main():

    if len(sys.argv) < 2:
        print("Please enter an argument")
        sys.exit()
# tells user to enter an argument if they don't and then exits the program
    
input = sys.argv[1].lower()
# takes the first argument and converts it to lowercase

if __name__ == "__main__":
    main()
