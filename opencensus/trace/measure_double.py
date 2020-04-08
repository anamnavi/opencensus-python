from opencensus.trace import measure
import string

class MeasureDouble(measure.Measure):

    def __init__(self, name, description, unit):
        if not (len(name) > self.name_max_length or all(ch in string.printable for ch in name)):
            raise ValueError(self.error_msg_invalid_name)
        self.name = name
        self.description = description
        self.unit = unit

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_unit(self):
        return self.unit

    def match(self):
        """
        todo: implement later
        will distinguish measure double from measure long
        """
        pass



