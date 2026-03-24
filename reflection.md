# Mini project 2 Summary:



I have created a database of baristas and managers and can be used to generate shifts for the workers in the csv file.
In the python file (project2.py) i created, I used object oriented programming and classes to assign different pay grades to the baristas, of which I created a main class Barista, then created subclasses which inherits from the main class, 
Novice, Intermediate, Advanced, which assigned different attributes of themselves, in this case different pay grades.

I have created functionality to add managers , baristas using csv.writer as well as to list them onto the terminal using csv.reader, by asking user for inputs in the main() function and feeding the raw data into the main Barista class listed earlier, and applying validation checks to ensure that name is not empty, that email and telephone number are of correct format. It also asks the user to assign a pay grade and the imput is fed through the subclasses, namely Novice, Intermediate, Advanced sublasses, fetches the pay value, and appends it to the barista being saved through the system.

I have also created the functionality to assign shifts randomly, by taking all the baristas and managers from both lists and randomly selecting from the list and outputting the result onto the terminal window. I have also created a function which takes the pay of the baristas, and 