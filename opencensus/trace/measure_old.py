#!/usr/bin/env python3
from opencensus.trace import tracer

class Measure:
    """
    defines Measurement taken by OpenCensus library
    """

    def __new__(cls):
        name_max_length = 255
        error_msg_invalid_name = f"Name should be a ASCII string with a length no greater than {name_max_length} characters."
        return object.__new__(cls)

    def get_name(self):
        return

    def get_description(self):
        return

    def get_unit(self):
        return

    def create_double(self):
        return

