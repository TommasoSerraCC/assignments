import unittest
# Import Particle class from my module particle
from assignments.core import Particle

class TestParticle(unittest.TestCase):

    def setUp(self):
        # Special unittest method which sets up a clean instance
        # of Particle class for each subsequent unit test in a non
        # redundant way
        self.particle = Particle(0.511, -1, 'Electron')

    # Test if the constructor initializes the attributes correctly.
    # Note that we are accessing the variables through the property
    # methods without accessing the private attributes itself which
    # is not recommended. This also tests the correct
    # initialization of the properties
    def test_mass(self):
        self.assertAlmostEqual(self.particle.mass, 0.511)

    def test_charge(self):
        self.assertEqual(self.particle.charge, -1)

    def test_name(self):
        self.assertEqual(self.particle.name, 'Electron')

    def test_beta(self):
        self.assertAlmostEqual(self.particle.beta, 0.)

    def test_energy(self):
        self.assertAlmostEqual(self.particle.energy, 0.511)




if __name__=='__main__':
    unittest.main()
