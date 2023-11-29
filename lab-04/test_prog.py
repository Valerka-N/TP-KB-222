import unittest
from prog import*

class TestInfixToRPN(unittest.TestCase):
    def test_basic_expression(self):
        inpt = "4+3*2"
        expected_rpn = "432*+"
        self.assertEqual(infix_to_rpn(inpt), list(expected_rpn))

    def test_expression_with_parentheses(self):
        inpt = "(4+3)*2"
        expected_rpn = "43+2*"
        self.assertEqual(infix_to_rpn(inpt), list(expected_rpn))

    def test_complex_expression(self):
        inpt = "3+5*(7-2)/4"
        expected_rpn = "3572-*4/+"
        self.assertEqual(infix_to_rpn(inpt), list(expected_rpn))

class TestEvaluateRPN(unittest.TestCase):
    def test_basic_expression(self):
        rpn_expression = "32*5+"
        expected_result = 11.0
        self.assertEqual(evaluate_rpn(list(rpn_expression)), expected_result)

    def test_expression_with_parentheses(self):
        rpn_expression = "43+2*"
        expected_result = 14.0
        self.assertEqual(evaluate_rpn(list(rpn_expression)), expected_result)

    def test_complex_expression(self):
        rpn_expression = "3572-*4/+"
        expected_result = 9.25
        self.assertEqual(evaluate_rpn(list(rpn_expression)), expected_result)

if __name__ == "__main__":
    unittest.main()
