import unittest
from math_quiz import get_random_integer, pick_random_math_operator, generate_math_question

class TestMathGame(unittest.TestCase):

    def test_get_random_integer(self):
        # Check if the random integers are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Run a large number of tests to ensure accuracy
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_pick_random_math_operator(self):
        # Test if the function returns one of the specified operators
        valid_operators = ['+', '-', '*']
        for _ in range(100):  # Test multiple times to check randomness
            operator = pick_random_math_operator()
            self.assertIn(operator, valid_operators)

    def test_generate_math_question(self):
        # Test if the function generates correct question and answer pairs
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (10, 5, '+', '10 + 5', 15),
            (10, 5, '-', '10 - 5', 5),
            (10, 5, '*', '10 * 5', 50)
        ]

        for num1, num2, operator, expected_question, expected_answer in test_cases:
            question, answer = generate_math_question(num1, num2, operator)
            self.assertEqual(question, expected_question)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
