import unittest

import rpn

class TestBasics(unittest.TestCase):
    '''def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_exp(self):
        result = rpn.calculate("2 2 ^")
        self.assertEqual(4, result)
    def test_percentage(self):
        result = rpn.calculate("72 5 %")
        self.assertTrue(abs(75.6 - result) < 1e-9)
    def test_intdiv(self):
        result = rpn.calculate("5 2 //")
        self.assertEqual(2, result)
    def test_bitwise(self):
        try:
            r1 = rpn.calculate("1 2 &")
            self.assertEqual(0, r1)
            r2 = rpn.calculate("1 2 |")
            self.assertEqual(3, r2)
            r3 = rpn.calculate("1 ~")
            self.assertEqual(-2, r3)
        except:
            try:
                r2 = rpn.calculate("1 2 |")
                self.assertEqual(3, r2)
            except:
                    r3 = rpn.calculate("1 ~")
                    self.assertEqual(-1, r3)'''
    def test_prev_ans(self):
        result = rpn.calculate("2 3 + :ans 7 +")
        self.assertEqual(12, result)
