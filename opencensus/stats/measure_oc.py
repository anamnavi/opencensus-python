import string

NAME_MAX_LENGTH = 255
ERROR_MSG_INVALID_NAME = "Name should be a ASCII string with a length " \
                         "no greater than " + str(NAME_MAX_LENGTH) + " characters."


class BaseMeasure(object):
    """ A measure is the type of metric that is being recorded with
    a name, description, and unit

    :type name: str
    :param name: string representing the name of the measure

    :type description: str
    :param description: a string representing the description of the measure

    :type unit: str
    :param unit: the units in which the measure values are measured

    """
    def __init__(self, name, description, unit=None):
        if len(name) > NAME_MAX_LENGTH or not all(ch in string.printable for ch in name):
            raise ValueError(ERROR_MSG_INVALID_NAME)
        self._name = name
        self._description = description
        self._unit = unit

    @property
    def name(self):
        """The name of the current measure"""
        return self._name

    @property
    def description(self):
        """The description of the current measure"""
        return self._description

    @property
    def unit(self):
        """The unit of the current measure"""
        return self._unit


class MeasureInt(BaseMeasure):
    """Creates an Integer Measure"""

    def __init__(self, name, description, unit):
        super(MeasureInt, self).__init__(name, description, unit)


class MeasureFloat(BaseMeasure):
    """Creates a Float Measure"""

    def __init__(self, name, description, unit=None):
        super(MeasureFloat, self).__init__(name, description, unit)
