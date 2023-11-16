""" In this module a class 'Particle' is defined.
    It describes same basic dynamic variables of a generic particle
    and makes it possible to manipulate them in an easy way.

    Then two other derivate classes 'Proton' and 'Alpha' are defined
    to describe more specifically those two particle
"""
import math
from loguru import logger


class Particle:
    """ Class describing a generic Particle

        Parameters
        ----------
        - mass : float
            Mass of the particle (in MeV/c^2)
        - charge: int
            Charge of the particle (in e)
        - name: string
            Name of the particle
        - beta: float
            Relativistic beta parameter (default value=0)
    """
    # Initialing the constructor
    def __init__(self, mass, charge, name, beta=0.):
        """ Constructor
        """
        # Creating instances of the class
        self._mass = mass
        self._charge = charge
        self._name = name
        self._beta = beta

    # In summary, Python properties are a mechanism for controlling
    # attribute access and adding additional logic when getting, setting,
    # or deleting attribute values. They are a powerful tool for
    # designing clean and maintainable object-oriented code.

    @property
    def mass(self):
        """ Return the mass of the particle """
        return self._mass

    @property
    def charge(self):
        """ Return the charge of the particle """
        return self._charge

    @property
    def name(self):
        """ Return the name of the particle """
        return self._name

    @property
    def beta(self):
        """ Return the beta parameter of the particle """
        return self._beta


    def print_info(self):
        """ Show particle informations in a formatted way """

        message=('Particle "{}": mass = {:.3f} MeV/c^2, charge = {} e, '\
                    'beta = {:.3f}')
        logger.info(message.format(self.name, self.mass, self.charge, self.beta))

    @beta.setter
    def beta(self, value):
        """ Set the value of the parameter beta showing a warning
            if the input is a non physical value (beta < 0)

            Parameters
            ----------
            - value: float
                Updated value of the beta parameter
        """
        if value < 0:
            logger.warning('Expected non negative value for beta. Setting 0...')
            self._beta = 0.
        else:
            self._beta = value

    @property
    def energy(self):
        """ Return the energy of the particle """
        return self.mass * math.sqrt(1/(1 - self.beta**2))

    @energy.setter
    def energy(self, value):
        """ Update 'beta' if the input energy is a physical value (E > mc^2)
            otherwise show a warning

            Parameters
            ----------
            - value: float
                Updated energy of the particle
        """
        if value < self.mass:
            logger.warning('Energy should be greater than mass = {}.'.format(self.mass))
            return
        self.beta = math.sqrt(1 - (self.mass**2 / value**2))

    @property
    def momentum(self):
        """ Return the momentum of the particle """
        return (self.mass*self.beta*math.sqrt(1/(1 - self.beta**2)))

    @momentum.setter
    def momentum(self, value):
        """ Update 'beta' if the input momentum is a physical value (p >= 0)
            otherwise show a warning

            Parameters
            ----------
            - value: float
                Updated momentum of the particle
        """
        if value < 0:
            logger.warning('Momentum must be greater than 0')
            return
        self.beta = value / (math.sqrt(value**2 + self.mass**2))


class Alpha(Particle):
    """ Class describing a 'alpha' particle that inherits from the base
        class 'Particle'

        Paramenters
        -----------
        - beta: float
            Relativistic beta parameter (default value=0)
    """
    # Defining the specifics of an alpha particle as class attributes.
    # When an instance of 'Alpha' is created they are not required as input
    MASS = 3727.3
    CHARGE = 4
    NAME = 'Alpha'
    def __init__(self, beta=0.):
        super().__init__(self.MASS, self.CHARGE, self.NAME, beta)


class Proton(Particle):
    """ Class describing a 'proton', that inherits from the base
        class 'Particle'

        Paramenters
        -----------
        - beta: float
            Relativistic beta parameter (default value=0)
    """
    # Defining the specifics of a proton as class attribute.
    # When an instance of 'Alpha' is created they are not required as input
    MASS = 938.3
    CHARGE = 1
    NAME = 'Proton'
    def __init__(self, beta=0.):
        super().__init__(self.MASS, self.CHARGE, self.NAME, beta)
