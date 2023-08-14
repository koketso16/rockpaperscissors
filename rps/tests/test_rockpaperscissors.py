import unittest
import game.rockpaperscissors as rockpaperscissors
from io import StringIO
from unittest.mock import patch

class MyTests(unittest.TestCase):
    def test_printer(self):
        self.assertEqual(rockpaperscissors.printer(),'hello')
        
    @patch("sys.stdin",StringIO("Rock\npaper\n"))
    def test_user_choice(self):
        valid = rockpaperscissors.valid_calls
        self.assertEqual(rockpaperscissors.get_user_choice(),"rock")
        self.assertIn(rockpaperscissors.get_user_choice(),valid)
        # self.assertIsInstance(rockpaperscissors.get_user_choice(),str)

    def test_computer_choice(self):
        valid = rockpaperscissors.valid_calls
        self.assertIn(rockpaperscissors.get_computer_choice(),valid)