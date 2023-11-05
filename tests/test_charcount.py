import unittest

# Import the function 'process' from my module
from assignments.charcount import process

class TestProcess(unittest.TestCase):
    def test_test(self):
        self.assertEqual(2,2)

    def test_four(self):
        self.assertEqual(4.,4.)

if __name__=='__main__':
    unittest.main()
