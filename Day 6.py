##################
### 23/03/2020 ###
##################

################################################
### UNIT TESTING and test driven development ###

#would create a 'test bed' which would be a separate file that you can import and use it's methods
#fail->pass->refactor
#depending on the error thrown by the testing, you develop a solution
import unittest

#create a test bed: (this could be a different file)
class SimpleCalc():
    def add(self,arg1,arg2):
        return arg1+arg2
    def divide(self,arg1,arg2):
        return arg1/arg2
    def multiply(self,arg1,arg2):
        return arg1*arg2
    def subtract(self,arg1,arg2):
        return arg1-arg2

#Now lets create a unit test that will test the calculations above
class TestCalc(unittest.TestCase):

    calc=SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2,4),6) #testing whether the 'add' operation produces 6 as the result when 2 and 4 are passed as the arguments

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4,3),1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3,6),18)

    def test_divide(self):
        self.assertEqual(self.calc.divide(21,7),3)
#
# #if __name__ == '__main__': #this is  used to ensure the file witht the actual test in is use
unittest.main() #if there are any errors in the test it will identify them
#main just denotes the file you're in

###############
### py TEST ###

import pytest
