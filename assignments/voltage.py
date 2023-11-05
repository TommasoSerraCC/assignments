""" Here we implement a class that handles times and voltages measurements.
The class should have an adeguate amount of feature described in the second
advanced assignment on professor Baldini github cmepda repository """

import logging
import numpy as np

logging.basicConfig(level=logging.INFO)


class ArrayLenghtError(Exception):
    """ Custom exception raised when we pass two iterables of
    different lenght to VoltageData instances """


class VoltageData:
    """ Class that handles two iterables containing
        time and voltage measurements """

    def __init__(self, times, voltages):
        """ times and voltages are two iterables of the same lenght.
        Private attribute _data is a 2D matrix with time and voltages
        as columns """
        time_measures = np.array(times, dtype = np.float64)
        volt_measures = np.array(voltages, dtype = np.float64)
        # Check if the arrays are of the same lenght
        try:
            assert len(time_measures) == len(volt_measures)
        except AssertionError as original_exception:
            logging.warning('Iterable arguments are not of the same lenght')
            raise ArrayLenghtError from original_exception
        self._data = np.column_stack([time_measures, volt_measures])
        print(self._data)

    def __len__(self):
        """ Returns the lenght of the two itrables """
        return len(self._data)

    def __getitem__(self, index):
        """ Gives access to our iterables with '[]' operator (Random access).
        'index' doesn't need to be a number, it could also be a couple of
        numbers or a 'slice' """
        return self._data[index]


    @property
    def voltages(self):
        """ Property that access the voltage measurments array """
        return self._data[:,1]

    @property
    def timestamps(self):
        """ Property that access the timestamps array """
        return self._data[:,0]
