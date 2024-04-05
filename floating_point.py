import unittest

def divide(a, b):
    return a / b

class TestDivision(unittest.TestCase):
    def test_divide_floats(self):
        # Define some test cases
        test_cases = [
            (10.5, 2.5, 4.2),  # 10.5 / 2.5 = 4.2
            (15.0, 3.0, 5.0),  # 15.0 / 3.0 = 5.0
            (7.0, 1.5, 4.666666666666667)  # 7.0 / 1.5 = 4.666666666666667
        ]
        
        # Iterate through test cases
        for a, b, expected_result in test_cases:
            with self.subTest(a=a, b=b, expected_result=expected_result):
                # Call the function and assert the result
                result = divide(a, b)
                self.assertAlmostEqual(result, expected_result, delta=0.000001)

if __name__ == '__main__':
    unittest.main()
