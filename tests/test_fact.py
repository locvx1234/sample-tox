# import sys
import unittest

from maths import factorial

# Add the ptdraft folder path to the sys.path list
# sys.path.append('/home/locvu/test_py/simple_tox/source')


class TesFactorial(unittest.TestCase):
    """
    Our basic test class
    """
    def test_fact(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        res = factorial.fact(5)
        self.assertEqual(res, 120)

    def test_error(self):
        """
        To test exception raise due to run time error
        """
        self.assertRaises(ZeroDivisionError, factorial.div, 0)


if __name__ == '__main__':
    unittest.main()
