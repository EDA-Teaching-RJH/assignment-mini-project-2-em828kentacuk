from multiprocessing import managers
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
    pay = 27.5
    def get_pay(self):
        return self.pay

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

def load_baristas():
    with open("workers.csv", "r") as file:
        reader = csv.reader(file)
        print("Baristas in the system:")
        print("-----------------------")
        for row in reader:
            if len(row) >= 3:
                name = row[0]
                level = row[1]
                pay = row[2]

 
            print(f"Name: {name}  Level: {level}  Pay: £{pay}/hr")

def save_manager(manager):
    with open("staff.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([manager.name, manager.get_pay()])

def load_managers():
    with open("staff.csv", "r") as file:
        reader = csv.reader(file)
        print("Managers:")
        print("-----------------------")
        for row in reader:
            name = row[0]
            pay = row[1]

            print(f"Name = {name}  Pay = £{pay}/hr")

def assign_shifts():
    workers = []
    staff = []
    cost = 0

    with open("staff.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                staff.append({
                    "name": row[0]
                })

    with open("workers.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 3:
                workers.append({
                    "name" : row[0],
                    "pay" : float(row[2])
                })


    if len(workers) < 4 or len(staff) < 1:
        raise ValueError("Not enough staff to assign a shift.")
    
    selected_employees = random.sample(workers, 4)
    selected_manager = random.choice(staff)

    total_cost = sum(employee["pay"] for employee in selected_employees) + 27.5

    shifts = ["Morning", "Afternoon", "Evening"]
    shift = random.choice(shifts)

    print(f"Shift: {shift}")
    print(f"Manager: {selected_manager['name']}")
    print(f"Total cost of shift: £{total_cost:.2f}")
    print("Employees:")
    for baristas in selected_employees:
        print(f"- {baristas['name']}")
    
    







#    to run the script type into command terminal:
#    python3 project2.py add                 — Add a new barista to the system
#    python3 project2.py list                — List all baristas
#    python3 project2.py addm                — Add a new manager to the system
#    python3 project2.py managers            — List all managers
#    python3 project2.py shifts              — Assign shifts to baristas and calculate their pay


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
elif argument == "list":
    load_baristas()
elif argument == "addm":
    name = input("Enter manager name: ")
    save_manager(Manager(name))
    print(f"Manager {name} added successfully.")
elif argument == "managers":
    load_managers()
elif argument == "shifts":
    assign_shifts()





if __name__ == "__main__":
    main()
