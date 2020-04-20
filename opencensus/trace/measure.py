#!/usr/bin/env python3
import string

NAME_MAX_LENGTH = 255
ERROR_MSG_INVALID_NAME = "Name should be a ASCII string with a length " \
                         "no greater than {NAME_MAX_LENGTH} characters."


class Measure:
    """
    Measure is for the definition of a measurement that is taken by OpenCensus library

    attributes and their specifications taken from specs docuemntation in opencensus-python

    :type str
    :param name: name of the measurement

    :type str
    :param description: description of the measurement

    :type str
    :param unit: unit of the measurement, either: "ms" (for latencies in milliseconds),
                                                  "by" (for sizes measured in bytes),
                                                  "1"  (for count of messages per RPC)
    """
    def __init__(self, name, description, unit):
        if len(name) > NAME_MAX_LENGTH or not all(ch in string.printable for ch in name):
            raise ValueError(ERROR_MSG_INVALID_NAME)
        self._name = name
        self._description = description
        self._unit = unit

    @property
    def name(self):
        """
        the name of the measure
        """
        return self._name

    @property
    def description(self):
        """
        the description of the measure
        """
        return self._description

    @property
    def unit(self):
        return self._unit

