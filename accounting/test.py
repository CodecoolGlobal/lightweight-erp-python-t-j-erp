# Do not modify this file

import unittest
import accounting   # Accounting manager


class TestAccounting(unittest.TestCase):
    points = 0
    input_file = "game_stat.txt"

    def test_1_get_most_played(self):
        result = reports.get_most_played(self.input_file)
        self.assertEqual(result, "Minecraft")
        if result == "Minecraft":
            self.points += 2
            print("Function 'get_most_played' is passed. 2 points.")



def main():
    unittest.main()

if __name__ == '__main__':
    main()