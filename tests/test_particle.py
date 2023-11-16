import unittest
import math
# Import Particle class from my module particle
from assignments.core import Particle
from assignments.core import Proton
from assignments.core import Alpha

class TestParticle(unittest.TestCase):

    def setUp(self):
        # Special unittest method which sets up clean instancies
        # of the classes for each subsequent unit test in a non
        # redundant way
        self.particle = Particle(0.511, -1, 'Electron')
        self.proton = Proton()
        self.alpha = Alpha()

    # Test if the constructor initializes the attributes correctly.
    # Note that we are accessing the variables through the property
    # methods without accessing the private attributes itself which
    # is not recommended. This also tests the correct
    # initialization of the properties
    def test_mass(self):
        self.assertAlmostEqual(self.particle.mass, 0.511)
        self.assertAlmostEqual(self.proton.mass, 938.3)
        self.assertAlmostEqual(self.alpha.mass, 3727.3)

    def test_charge(self):
        self.assertEqual(self.particle.charge, -1)
        self.assertEqual(self.proton.charge, 1)
        self.assertEqual(self.alpha.charge, 4)

    def test_name(self):
        self.assertEqual(self.particle.name, 'Electron')
        self.assertEqual(self.proton.name, 'Proton')
        self.assertEqual(self.alpha.name, 'Alpha')

    def test_beta(self):
        self.assertAlmostEqual(self.particle.beta, 0.)
        self.assertAlmostEqual(self.proton.beta, 0.)
        self.assertAlmostEqual(self.alpha.beta, 0.)

    def test_energy(self):
        self.assertAlmostEqual(self.particle.energy, 0.511)
        self.assertAlmostEqual(self.proton.energy, 938.3)
        self.assertAlmostEqual(self.alpha.energy, 3727.3)

    def test_show_info(self):
        # To be implemented
        pass

    def test_set_non_physical_beta(self):
        # Should return zero
        self.particle.beta = -1.
        self.proton.beta = -1.
        self.alpha.beta = -1.
        self.assertAlmostEqual(self.particle.beta, 0.)
        self.assertAlmostEqual(self.proton.beta, 0.)
        self.assertAlmostEqual(self.alpha.beta, 0.)

    def test_set_physical_beta(self):
        self.particle.beta = 0.1
        self.proton.beta = 0.1
        self.alpha.beta = 0.1
        self.assertAlmostEqual(self.particle.beta, 0.1)
        self.assertAlmostEqual(self.proton.beta, 0.1)
        self.assertAlmostEqual(self.alpha.beta, 0.1)

    def test_set_non_physical_energy(self):
        # Store last value of beta
        last_particle_beta = self.particle.beta
        last_proton_beta = self.proton.beta
        last_alpha_beta = self.alpha.beta
        # Try to set non physical energy value
        self.particle.energy = 0.
        self.proton.energy = 0.
        self.alpha.energy = 0.
        self.assertAlmostEqual(self.particle.beta, last_particle_beta)
        self.assertAlmostEqual(self.proton.beta, last_proton_beta)
        self.assertAlmostEqual(self.alpha.beta, last_alpha_beta)

    def test_set_physical_energy(self):
        # Try to set E = 2m
        self.particle.energy = 1.022 # MeV/c^2
        self.proton.energy = 1876.6 # MeV/c^2
        self.alpha.energy = 7454.6 # MeV/c^2
        self.assertAlmostEqual(self.particle.energy, 1.022)
        self.assertAlmostEqual(self.proton.energy, 1876.6)
        self.assertAlmostEqual(self.alpha.energy, 7454.6)
        self.assertAlmostEqual(self.particle.beta, math.sqrt(3/4))
        self.assertAlmostEqual(self.proton.beta, math.sqrt(3/4))
        self.assertAlmostEqual(self.alpha.beta, math.sqrt(3/4))

    def test_set_non_physical_momentum(self):
        last_particle_beta = self.particle.beta
        last_proton_beta = self.proton.beta
        last_alpha_beta = self.alpha.beta
        self.particle.momentum = -1.
        self.proton.momentum = -1.
        self.alpha.momentum = -1.
        self.assertAlmostEqual(self.particle.beta, 0.)
        self.assertAlmostEqual(self.proton.beta, 0.)
        self.assertAlmostEqual(self.alpha.beta, 0.)

    def test_set_physical_momentum(self):
        # Try to set p=m so that beta=1/sqrt(2)
        self.particle.momentum = 0.511
        self.proton.momentum = 938.3
        self.alpha.momentum = 3727.3
        self.assertAlmostEqual(self.particle.momentum, 0.511)
        self.assertAlmostEqual(self.proton.momentum,938.3)
        self.assertAlmostEqual(self.alpha.momentum, 3727.3)
        self.assertAlmostEqual(self.particle.beta, math.sqrt(1/2))
        self.assertAlmostEqual(self.proton.beta, math.sqrt(1/2))
        self.assertAlmostEqual(self.alpha.beta, math.sqrt(1/2))



if __name__=='__main__':
    unittest.main()
