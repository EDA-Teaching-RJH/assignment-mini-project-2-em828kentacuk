#start with our imports

import pytest
import csv
from project2 import (
    Barista, Novice, Intermediate, Expert, Manager, 
    save_barista, load_baristas, save_manager, load_managers, assign_shifts
)
"""
# HOW TO RUN:
    python3 -m pytest project2_test.py -v

# This test function tests the creation of a barista and checks if the attributes are correctly assigned. 
# also tests the different levels of baristas to ensure they are correctly instantiated as their respective classes.
"""
class TestBarista:
    def test_barista_creation(self):
        barista = Barista("Alice", "alice@gmail.com", "07123456789")

        assert barista.name == "Alice"
        assert barista.email == "alice@gmail.com"
        assert barista.tel == "07123456789"

    def test_barista_levels(self):
        novice = Novice("Bob", "bob@gmail.com", "07987654321")
        intermediate = Intermediate("Charlie", "charlie@gmail.com", "07111111111")
        expert = Expert("David", "david@gmail.com", "07222222222")

        assert novice.__class__.__name__ == "Novice"
        assert intermediate.__class__.__name__ == "Intermediate"
        assert expert.__class__.__name__ == "Expert"

# this test function checks for various edge cases and error handling in the Barista class. 
# It tests for missing name, incorrect email format, and incorrect telephone number format, 
# ensuring that the appropriate exceptions are raised when invalid data is provided.

    def test_missing_name(self):
        with pytest.raises(ValueError):
            Barista(name=None, email="alice@gmail.com", tel="07123456789")
    
    def test_wrong_email_format(self):
        with pytest.raises(ValueError):
            Barista(name="Alice", email="alicegmail.com", tel="07123456789")
    
    def test_wrong_tel_format(self):
        with pytest.raises(ValueError):
            Barista(name="Alice", email="alice@gmail.com", tel="0712-345-6789")



# repeats the same process for the Manager class, 
# testing the creation of a manager and ensuring that the name attribute is correctly assigned.

class TestManager:
    def test_manager_creation(self):
        manager = Manager("joe")
        assert manager.name == "joe"
    # tests if value error raised id name is missing when creating a manager

    def test_missing_name(self):
        with pytest.raises(ValueError):
            Manager(name=None)

# this test function checks the file operations for both baristas and managers.
# It tests the saving and loading of barista and manager data to and from CSV files,
# ensuring that the data is correctly saved and loaded, 
# and that the correct types of objects are created when loading the data.

class TestFileOperations:   
    def test_save_and_load_barista(self, tmp_path):
        file = tmp_path / "workers.csv"

        barista = Novice("Eve", "eve@gmail.com", "07123456789")

        save_barista(barista, file)
        baristas = load_baristas(file)

# asserts that the loaded barista has the same attributes as the original barista and is of the correct class type.

        assert len(baristas) == 1
        assert baristas[0].name == "Eve"
        assert baristas[0].email == "eve@gmail.com"
        assert baristas[0].tel == "07123456789"
        assert isinstance(baristas[0], Novice)

    def test_save_and_load_manager(self, tmp_path):
        file = tmp_path / "managers.csv"
# repeats the same process for a manager, ensuring that the manager's name is correctly saved and loaded, 
# and that the loaded object is of the correct class type.
        manager = Manager("Frank")

        save_manager(manager, file)
        managers = load_managers(file)

        assert len(managers) == 1
        assert managers[0].name == "Frank"
        assert isinstance(managers[0], Manager)

    def test_not_enough_staff(self, tmp_path):
        staff_file = tmp_path / "staff.csv"
        workers_file = tmp_path / "workers.csv"

    # No staff
        with open(staff_file, "w") as f:
            f.write("")

    # Only 2 workers
        with open(workers_file, "w") as f:
            f.write("john,Novice,12.5\n")
            f.write("jane,Novice,12.5\n")

        with pytest.raises(ValueError):
            assign_shifts(staff_file, workers_file)
    
