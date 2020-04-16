import unittest
import rpc_view_constants

class RPCVCTests(unittest.TestCase):
    """
    RPVMTest tests the rpc_view_constants module
    """

    def setUp(self):
        self.rpc_view = rpc_view_constants.RPCViewConstants()

    def test_client_measures(self):
        self.assertEquals(rpc_view_constants.grpc_client_sent_bytes_per_rpc_view.get_metric_descriptor().name, "grpc.io/client/sent_bytes_per_rpc", "view not set right")


if __name__ == '__main__':
    unittest.main()