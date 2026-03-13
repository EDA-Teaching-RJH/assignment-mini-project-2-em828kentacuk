import re
import os
import sys
import random
import csv


# imports all the functions from the other files

class Barista:

    def __init__(self, name):

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

#this function is to save the information to a csv file called workers.csv.
def save_barista(barista):
    with open("workers.csv", "a", newline='') as file:
        writer = csv.writer(file)
        if isinstance(barista, Novice):
            writer.writerow([barista.name, "Novice", barista.get_pay()])
        elif isinstance(barista, Intermediate):
            writer.writerow([barista.name, "Intermediate", barista.get_pay()])
        elif isinstance(barista, Expert):
            writer.writerow([barista.name, "Expert", barista.get_pay()])

#    to run the script type into command terminal:
#    python3 project2.py add                 — Add a new barista to the system
#    python3 project2.py list                — List all baristas
#    python3 project2.py managers            — List all managers
#    python3 project2.py assign shifts       — Assign shifts to baristas and calculate their pay


def main():

    if len(sys.argv) < 2:
        print("Please enter an argument")
        sys.exit()
# tells user to enter an argument if they don't and then exits the program
    
argument = sys.argv[1].lower().strip()
# takes the first argument and converts it to lowercase and removes any leading or trailing whitespace

if argument == "add":
        name = input("Enter the barista's name: ")
        barista = Barista(name)
        level = input("Enter the barista's level (Novice, Intermediate, Expert): ").lower().strip()
        if level == "novice":
            barista = Novice(name)
        elif level == "intermediate":
            barista = Intermediate(name)
        elif level == "expert":
            barista = Expert(name)
        else:
            print("Invalid level. Please enter Novice, Intermediate, or Expert.")
            sys.exit()
        save_barista(barista)
        print(f"Barista {name} added successfully.")





if __name__ == "__main__":
    main()
