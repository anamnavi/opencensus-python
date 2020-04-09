#!/usr/bin/env python3
import string

name_max_length = 255
error_msg_invalid_name = f"Name should be a ASCII string with a length no greater than {name_max_length} characters."


class Measure:
    def __init__(self, name, description, unit):
        if not (len(name) > name_max_length or all(ch in string.printable for ch in name)):
            raise ValueError(error_msg_invalid_name)
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



