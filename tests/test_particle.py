import unittest
import numpy as np
# Import Particle class from my module particle
from assignments.core import Particle

class TestParticle(unittest.TestCase):

    def setUp(self):
        # Special unittest method which sets up a clean instance
        # of the Particle class for each subsequent unit test in a non
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

    def test_show_info(self):
        # To be implemented
        pass

    def test_set_non_physical_beta(self):
        # Should return zero
        self.particle.beta = -1.
        self.assertAlmostEqual(self.particle.beta, 0.)

    def test_set_physical_beta(self, 0.1):
        self.particle.beta = 0.1
        self.assertAlmostEqual(self.particle.beta, 0.1)

    def test_set_non_physical_energy(self):
        # Store last value of the energy
        last_energy = self.particle.energy
        # Try to set non physical energy value
        self.particle.energy = 0.
        self.assertAlmostEqual(self.particle.beta, last_energy)

    def test_set_physical_energy(self):
        # Try to set E = 2m
        self.particle.energy = 1.022 # MeV/c^2
        self.assertAlmostEqual(self.particle.energy, np.sqrt(3/4))




if __name__=='__main__':
    unittest.main()
