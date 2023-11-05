""" Importing modules"""
import math
from loguru import logger

LIGHT_SPEED=1

class Particle:
    """ Class describing a generic Particle """

    # Initialing the constructor
    def __init__(self, mass, charge, name, beta=0.):
        """ Arguments:
            -particle mass (in MeV/c^2)
            -partcle charge (in e)
            -particle name
            -beta [default value=0]
        """
        # Creating instances of the class
        # '__' indicates that instance has to be considered private
        self._mass = mass
        self._charge = charge
        self._name = name
        self._beta = beta

    # Defining methods to access private attributes by '.' operator
    # (otherwise '_' would be needed and we don't want that)
    @property
    def mass(self):
        return self._mass

    @property
    def charge(self):
        return self._charge

    @property
    def name(self):
        return self._name

    @property
    def beta(self):
        return self._beta


    def print_info(self):
        """ Shows particle informations in a formatted way """

        message=('Particle "{}": mass = {:.3f} MeV/c^2, charge = {} e, '\
                    'beta = {:.3f}')
        logger.info(message.format(self.name, self.mass, self.charge, self.beta))

    @beta.setter
    def beta(self, value):
        if value < 0:
            logger.warning('Expected non negative value for beta. Setting 0...')
            self._beta = 0.
        else:
            self._beta = value

    @property
    def energy(self):
        return self.mass*LIGHT_SPEED* math.sqrt(1/(1 + self.beta**2))

    @energy.setter
    def energy(self, value):
        if value < self.mass:
            logger.warning('Energy should be greater than mass = {}.'.format(self.mass))
            return
        self.beta = (math.sqrt(((value*2) / LIGHT_SPEED2) - ((self.mass2) * LIGHT_SPEED*2))) / value

    @property
    def momentum(self):
        return (self.mass*self.beta*math.sqrt(1/(1+self.beta**2)))

    @momentum.setter
    def momentum(self, value):
        if value < 0:
            logger.warning('Momentum must be greater than 0')
            return
        self.beta = value/(math.sqrt(value*2 + self.mass*2))
