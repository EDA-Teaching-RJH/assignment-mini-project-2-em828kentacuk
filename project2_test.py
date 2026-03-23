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
    
    def test_missing_name(self):
        with pytest.raises(ValueError):
            Barista(name=None, email="alice@gmail.com", tel="07123456789")
    
    def test_wrong_email_format(self):
        with pytest.raises(ValueError):
            Barista(name="Alice", email="alicegmail.com", tel="07123456789")
    
    def test_wrong_tel_format(self):
        with pytest.raises(ValueError):
            Barista(name="Alice", email="alice@gmail.com", tel="0712-345-6789")

    