import pytest
import csv
from project2 import (
    Barista, Novice, Intermediate, Expert, Manager, 
    save_barista, load_baristas, save_manager, load_managers, assign_shifts
)
# HOW TO RUN:
#    python3 -m pytest project2_test.py -v


# This test function tests the creation of a barista and checks if the attributes are correctly assigned. 
# also tests the different levels of baristas to ensure they are correctly instantiated as their respective classes.
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