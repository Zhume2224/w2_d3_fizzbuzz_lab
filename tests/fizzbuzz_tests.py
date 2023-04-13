import unittest

from src.fizzbuzz import * 

#solution2
class TestFizzbuzz(unittest.TestCase):
    def setUp(self):
        self.dictionary={
            3:'fizz',
            5:'buzz',
            2:'ruzz'
        }

    def test_fizzbuzz(self):
        self.assertEqual('fizzbuzz',fizzbuzz(self.dictionary,2))




#solution1
# class TestFizzbuzz(unittest.TestCase):
#     def setUp(self):
#         self.number_divisible_by_3 = 6
#         self.number_divisible_by_5 = 10
#         self.number_divisible_by_15 = 60
#         self.number_not_divisible = 23
#         self.null = 0
        
#     def test_returns_fizz(self):
#         self.assertEqual("Fizz",FizzBuzz(self.number_divisible_by_3))
                         
#     def test_returns_buzz(self):
#         self.assertEqual("Buzz",FizzBuzz(self.number_divisible_by_5))
                         
#     def test_returns_fizzbuzz(self):
#         self.assertEqual("FizzBuzz",FizzBuzz(self.number_divisible_by_15))        
        
#     def test_returns_number(self):
#         self.assertEqual("23",FizzBuzz(self.number_not_divisible)) 
                           
#     def test_returns_none__null(self):
#         self.assertEqual(None,FizzBuzz(self.null))

#     def test_returns_none__negative(self):
#         self.assertEqual(None,FizzBuzz(self.number_not_divisible*-1))
    
