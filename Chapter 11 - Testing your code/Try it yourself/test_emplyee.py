# Write a test case for Employee. Write two test methods, test_give_default_raise() and
# test_give_custom_raise(). Use the setUp() method so you don’t have to create a new employee instance
# in each test method. Run your test case, and make sure both tests pass.

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the class Employee"""

    def setUp(self):
        """ Test for module Employee"""
        self.anera = Employee('anera', 'svarc', 20_000)

    def test_give_default_raise(self):
        """Test for automatic 5000 raise"""
        # da nemam setUp onda bi bilo:
        # anera = Employee('anera', 'svarc', 20_000)
        # a ove ispod ne bi imale self.
        self.anera.give_raise() # prazno tako da bude automatski zadan iznos
        self.assertEqual(self.anera.salary, 25_000) # objasni dio sa self!

    def test_give_custom_raise(self):
        """Test for custom raise"""
        self.anera.give_raise(10_000) # izmislila custom vrijednost
        self.assertEqual(self.anera.salary, 30_000)

if __name__ == '__main__':
    unittest.main()