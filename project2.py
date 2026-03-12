import re
import os
import sys
import random


# imports all the functions from the other files

class Barista:

    def __init__(self, name, pay):

        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name

class Novice(Barista):
    pay = 12.5

    def get_pay(self):
        return self.pay


class Intermediate(Barista):
    pay = 14.5

    def get_pay(self):
        return self.pay

class Expert(Barista):
    pay = 17.5

    def get_pay(self):
        return self.pay


class Manager:
    def __init__(self, name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name

"""
to run the script type into command terminal:
    python3 project2.py add                 — Add a new barista to the system
    python3 project2.py list                — List all baristas
    python3 project2.py managers            — List all managers
    python3 project2.py assign shifts       — Assign shifts to baristas and calculate their pay
"""

def main():

    if len(sys.argv) < 1:
        print("Please enter an argument")
        sys.exit()
# tells user to enter an argument if they don't and then exits the program
    
input = sys.argv[1].lower().strip()
# takes the first argument and converts it to lowercase and removes any leading or trailing whitespace

if input == "add":
    name = input("Enter the barista's name: ")
    barista = Barista(name, 0)

    print(f"Barista {barista.name} added with pay {barista.pay}")



if __name__ == "__main__":
    main()
