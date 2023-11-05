""" Import module for unit tests """
import unittest
# Import Particle class from my module particle
from assignments.core import Particle

class TestParticle(unittest.TestCase):
    """ Class for unit tests """

    def setUp(self):
        # Special unittest method which sets up a clean instance
        # of Particle class for each subsequent unit test in a non
        # redundant way
        self.particle = Particle(0.511, -1, 'Electron')

    def test_mass(self):
        # Test if the constructor initializes mass correctly
        self.assertAlmostEqual(self.particle.mass, 0.511)

    def test_charge(self):
        self.assertEqual(self.particle.charge, -1)

    def test_name(self):
        self.assertEqual(self.particle.name, 'Electron')

if __name__=='__main__':
    unittest.main()
