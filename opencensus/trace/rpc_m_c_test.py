import unittest

# from opencensus.trace import rpc_measure_constants
import rpc_measure_constants

# from opencensus.grpc.rpc_measure_constants import RPCMeasureConstants

class RPCMCTests(unittest.TestCase):

    def setUp(self):
        self.rpc_measure = rpc_measure_constants.RPCMeasureConstants()

    def test_client_measures(self):
        self.assertEqual(self.rpc_measure.grpc_client_sent_messages_per_rpc.get_unit(), "1", "unit not set correctly on init")


    def test_client_measures_2(self):
        self.assertEqual(self.rpc_measure.grpc_client_sent_bytes_per_rpc.get_description(), "Total bytes sent across all request messages per RPC", "description not set correctly on init")
        self.assertEqual(self.rpc_measure.grpc_client_received_messages_per_rpc.get_name(), "grpc.io/client/received_messages_per_rpc", "name not set correctly on init")
        self.assertEqual(self.rpc_measure.grpc_client_received_bytes_per_rpc.get_unit(), "by", "unit not set correctly upon init")

if __name__ == '__main__':
    unittest.main()