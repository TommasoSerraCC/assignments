""" Here we implement unit tests for 'voltage' package """

import unittest
import numpy as np
from assignments.voltage import VoltageData

class TestVoltage(unittest.TestCase):
    """ Unit tests class """

    def setUp(self):
        self.array1 = [1.,2.]
        self.array2 = [3.,4.]
        self.measurements = VoltageData(self.array1, self.array2)

    def test_load(self):
        """ Check if the two numpy arrays are correctly initialized """
        self.assertTrue(np.allclose(self.array1, [1.,2.]))
        self.assertTrue(np.allclose(self.array2, [3.,4.]))

    def test_constructor_up_left(self):
        """ Check if the upper left 2D matrix element is correctly
        initialized using a 2x2 test matrix """
        self.assertAlmostEqual(self.measurements[0][0], 1.)

    def test_constructor_up_right(self):
        """ Check if the upper right 2D matrix element is correctly
        initialized using a 2x2 test matrix """
        self.assertAlmostEqual(self.measurements[0][1], 3.)

    def test_constructor_down_left(self):
        """ Check if the lower left 2D matrix element is correctly
        initialized using a 2x2 test matrix """
        self.assertAlmostEqual(self.measurements[1][0], 2.)

    def test_constructor_down_right(self):
        """ Check if the lower right 2D matrix element is correctly
        initialized using a 2x2 test matrix """
        self.assertAlmostEqual(self.measurements[1][1], 4.)

    def test_len(self):
        """ Check if the lenght of the matrix side is 2 """
        self.assertEqual(len(self.measurements), 2)

    def test_slicing(self):
        """ Check if the slicing is correctly implemented """
        self.assertTrue(np.allclose(self.measurements[0:1,1],
            self.array2[0:1]))


if __name__ == '__main__':
    unittest.main()
