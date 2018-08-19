"""
https://docs.python.org/3/library/unittest.html#unittest.TestCase
This link has unittest assertions
"""
import unittest

class AssertDemo(unittest.TestCase):

    # Error messages below are only logged if the test fails
    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is not true")
        b = False
        self.assertFalse(b, "b is not false")

    def test_assertEqual(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a, b, msg="'a' is not equal to 'b'")


if __name__ == '__main__':
    unittest.main(verbosity=2)