import unittest
import measure

class MeasureTest(unittest.TestCase):
    """
    MeasureTest has PyUnit tests for measure.py
    """

    def setUp(self):
        """
        setup performed before each test
        """
        self.measure = measure.Measure("grpc_client_sent_messages_per_rpc",
                                       "Number of messages sent in the RPC",
                                       "1")
        self.measure_exceeds_max_length = None
        self.measure_non_printable = None

    def test_measure_name(self):
        """
        tests measure module's get_name() method
        """
        self.assertEqual(self.measure.name,
                         "grpc_client_sent_messages_per_rpc",
                         "get_name() method not working")

    def test_measure_description(self):
        """
        tests measure module's get_description() method
        """
        self.assertEqual(self.measure.description,
                         "Number of messages sent in the RPC",
                         "get_description() method not working")

    def test_measure_unit(self):
        """
        tests measure module's get_unit() method
        """
        self.assertEqual(self.measure.unit,
                         "1",
                         "get_unit() not working correctly")

    def test_long_name_init(self):
        """
        tests measure module's __init__() if the name str exceeds max length
        and assert that it raises ValueError as expected
        """
        with self.assertRaises(ValueError):
            self.measure_exceeds_max_length = measure.Measure("a"*256, "some description", "1")

    def test_unprintable_name_init(self):
        """
        tests measure module's __init__() if the name str contains a non-printable ascii character
        and assert that it raises ValueError as expected
        """
        with self.assertRaises(ValueError):
            chr_list = ['0x41', '0x1B', '0x42']
            non_printable_str = "".join([chr(int(x, 16)) for x in chr_list])  # 'AB\x1b'
            self.measure_non_printable = measure.Measure(non_printable_str, "some description", "1")


if __name__ == '__main__':
    unittest.main()
