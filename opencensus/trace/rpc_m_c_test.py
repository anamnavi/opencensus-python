import unittest

# from opencensus.trace import rpc_measure_constants
import rpc_measure_constants

# from opencensus.grpc.rpc_measure_constants import RPCMeasureConstants

class RPCMCTests(unittest.TestCase):

    def setUp(self):
        self.rpc_measure = rpc_measure_constants.RPCMeasureConstants()

    def test_client_measure_1(self):
        assert self.rpc_measure.grpc_client_sent_messages_per_rpc.get_description == "Number of messages sent in the RPC", "description not set"

if __name__ == '__main__':
    unittest.main()