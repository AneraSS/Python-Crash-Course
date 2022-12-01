# a passing test
# we import 'unitest' and the function we want to test

import unittest
from name_function import get_formatted_name

# we create a class which will contain a unit test for get_formatted_name()
# you can name it whatever you want, but name it related to function


class NamesTestCase(unittest.TestCase):
    """"Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work? """

        # within the test method, we call the function we want to test
        # in this example we give the arguments 'janis' and 'joplin' and assign the result to formatted_name
        formatted_name = get_formatted_name('janis', 'joplin')

        # we use one of the unittest's most useful features: an assert method
        # they verify that the result you received matches the result you expect to receive
        # in this case, we know we want to get capitalized full name
        # unittest's assertEqual() - to check if this is true, using this we pass it formated_name() andn 'Janis
        # Joplin' . This line:
        self.assertEqual(formatted_name, 'Janis Joplin')
        # says: compare the value of formatted_name to the string 'Janis Joplin'
        # if they are equal - fine, but if they don't match - let me know

# we're going to run this file directly
# but - many testing frameworks import your test files before running them
    def test_first_middle_last_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work? """
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
# this block below
# looks at a special variable __name__ which is set when the program is executed
# if the file is being run as the main program, the value of __name_ won't be '__main__' and the block
# won't be executed
if __name__ == '__main__':
    unittest.main()
