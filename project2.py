import re
import os
import sys
import random
import csv
import requests


# imports all the functions from the other files

class Barista:

    def __init__(self, name, email=None, tel=None):
# ensures that the name of the barista is not empty and assigns it to the instance variable self.name
# ensures emails entered follow a defulat format, declines it if the email deviates from the format
# ensures that the telephone number follows a specific format (starting with +44 or 0 followed by 7 and then 9 digits),
# and raises a ValueError if the format is incorrect or if the telephone number is empty
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name
        email_pattern = r"[^@]+@[^@]+\.[^@]+"
        if email and not re.match(email_pattern, email):
            raise ValueError("Invalid email format")
        elif not email:
            raise ValueError("Email cannot be empty")
        self.email = email
        tel_num_pattern = r"^(?:\+44|0)7\d{9}$"
        if tel and not re.match(tel_num_pattern, tel):
            raise ValueError("Invalid telephone number format")
        elif not tel:
            raise ValueError("Telephone number cannot be empty")
        self.tel = tel
# ensures that the name of the barista is not empty and assigns it to the instance variable self.name
# ensures emails entered follow a defulat format, declines it if the email deviates from the format
class Novice(Barista):
    pay = 12.5
    def __init__(self, name, email=None, tel=None):
        super().__init__(name, email, tel)
# assigns the pay for a novice barista to 12.5
# repeats the same process for the intermediate and expert baristas with different pay rates
    def get_pay(self):
        return self.pay


class Intermediate(Barista):
    pay = 14.5
    def __init__(self, name, email=None, tel=None):
        super().__init__(name, email, tel)
    def get_pay(self):
        return self.pay

class Expert(Barista):
    pay = 17.5
    def __init__(self, name, email=None, tel=None):
        super().__init__(name, email, tel)
    def get_pay(self):
        return self.pay


class Manager:
    def __init__(self, name,):
        if not name:
            raise ValueError("Name cannot be empty")
        self.name = name
    pay = 27.5
    def get_pay(self):
        return self.pay

#this function is to save the information to a csv file called workers.csv.
# saves the name and rank of the barista to csv based on input from the user and the pay for that rank

def save_barista(barista, file_path="workers.csv"):
    with open(file_path, "a", newline='') as file:
        writer = csv.writer(file)
        if isinstance(barista, Novice):
            writer.writerow([barista.name, "Novice", barista.get_pay(), barista.email, barista.tel])
        elif isinstance(barista, Intermediate):
            writer.writerow([barista.name, "Intermediate", barista.get_pay(), barista.email, barista.tel])
        elif isinstance(barista, Expert):
            writer.writerow([barista.name, "Expert", barista.get_pay(), barista.email, barista.tel])
    return barista

# this displays the baristas onto the terminal window
# opens a csv file and outputs the result for every row in the file onto the command line
def load_baristas(file_path="workers.csv"):
    baristas = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        print("Baristas in the system:")
        print("-----------------------")

#creates empty list called baristas to store the barista objects that will be created from the data in the csv file
# it then reads the data from the csv file and creates barista objects 
# based on the level of the barista (Novice, Intermediate, Expert)

        for row in reader:
            if len(row) >= 5:
                name, level, pay, email, tel = row
# checks row length to ensure that it contains the expected number of columns (at least 5) 
# before attempting to unpack the values into variables
# it then uses if elif statements to check the level of the barista 
# creates an object of the correct class type based on that level
                if level == "Novice":
                    barista = Novice(name, email, tel)
                elif level == "Intermediate":
                    barista = Intermediate(name, email, tel)
                elif level == "Expert":
                    barista = Expert(name, email, tel)
                else:
                    continue

                baristas.append(barista)

                print(f"Name: {name}  Level: {level}  Pay: £{pay}/hr  Email: {email}  Telephone: {tel}")

    return baristas
#this function is to save the information to a csv file called staff.csv.
# saves the name and rank of the manager in the same manner as before

def save_manager(manager, file_path="staff.csv"):
    with open(file_path, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([manager.name, manager.get_pay()])

# this repeats the same process for loading baristas but with a new file

def load_managers(file_path="staff.csv"):
    managers = []
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        print("Managers:")
        print("-----------------------")
        for row in reader:
            if len(row) >= 2:
                name, pay = row
                manager = Manager(name)
                managers.append(manager)

            print(f"Name = {name}  Pay = £{pay}/hr")
    return managers

# this assigns shifts every time the function is called
# it starts by inilialising empty lists for workers and staff and a variable for cost

def assign_shifts(staff_file="staff.csv", workers_file="workers.csv"):
    workers = []
    staff = []
    cost = 0
# it then opens the staff csv file, reads the data and appends it to the empty 
# lists with the name and pay of each employee

    with open(staff_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                staff.append({
                    "name": row[0]
                })
# repeats the same process for the workers file, 
# but also includes the pay for each worker as well as their name
    with open(workers_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 3:
                workers.append({
                    "name" : row[0],
                    "pay" : float(row[2])
                })
# validation check to ensure that there are enough staff to assign a shift, if not it raises a ValueError
# in this case we need at least 4 workers and 1 manager to assign a shift

    if len(workers) < 4 and len(staff) < 1:
        raise ValueError("Not enough staff to assign a shift.")
    
# selects 4 random employees and 1 random manager from their respective lists
# it then calculates the total cost of the shift by summing the pay of the selected employees and adding the manager's pay

    selected_employees = random.sample(workers, 4)
    selected_manager = random.choice(staff)

    total_cost = sum(employee["pay"] for employee in selected_employees) + 27.5

    shifts = ["Morning", "Afternoon", "Evening"]
    shift = random.choice(shifts)

# lastly it prints out the details of the shift, including the shift time, manager
# and total cost and the names of the employees working that shift

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
        email = input("Enter the barista's email: ")
        tel = input("Enter the barista's telephone number: ")
# asks inputs for the name, email and telephone number of the barista and then creates 
# a new barista object with the given information
        barista = Barista(name, email, tel)
        level = input("Enter the barista's level (Novice, Intermediate, Expert): ").lower().strip()
# asks user for level, then uses if elif statements to check the level 
# create a barista object of the correct class type based on the level entered by the user
        if level == "novice":
            barista = Novice(name, email, tel)
        elif level == "intermediate":
            barista = Intermediate(name, email, tel)
        elif level == "expert":
            barista = Expert(name, email, tel)
        else:
            print("Invalid level. Please enter Novice, Intermediate, or Expert.")
            sys.exit()
#gracefully handles the case where the user enters an invalid level by printing an error message and exiting the program
        save_barista(barista)
        print(f"Barista {name} added successfully.")
elif argument == "list":
    load_baristas()
#calls the load_baristas function to display the list of baristas when the user enters the "list" argument
# now repeats the same process for managers
elif argument == "addm":
    name = input("Enter manager name: ")
    save_manager(Manager(name))
    print(f"Manager {name} added successfully.")
elif argument == "managers":
    load_managers()
elif argument == "shifts":
    assign_shifts()




# Runs main() only when the file is executed directly
# Does not run main() if the file is imported into another script

if __name__ == "__main__":
    main()
