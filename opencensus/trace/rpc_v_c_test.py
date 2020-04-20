import unittest
import rpc_view_constants
from opencensus.metrics.export.metric_descriptor import MetricDescriptorType

class RPCVCTests(unittest.TestCase):
    """
    RPVMTest tests the rpc_view_constants module
    """

    def setUp(self):
        self.rpc_view = rpc_view_constants.RPCViewConstants()

    def test_client_measures(self):
        self.assertEqual(self.rpc_view.grpc_client_sent_bytes_per_rpc_view.name,
                          "grpc.io/client/sent_bytes_per_rpc",
                          "grpc_client_sent_bytes_per_rpc_view not set correctly")
        self.assertEqual(self.rpc_view.grpc_client_received_bytes_per_rpc_view.description,
                         "Received bytes per RPC",
                         "grpc_client_received_bytes_per_rpc_view not set correctly")
        self.assertEqual(self.rpc_view.grpc_client_roundtrip_latency_view.measure.get_name(),
                         "grpc.io/client/roundtrip_latency",
                         "grpc_client_roundtrip_latency_view not set correctly")
        self.assertEqual(self.rpc_view.grpc_client_completed_rpc_view.measure.get_name(),
                         "grpc.io/client/roundtrip_latency",
                         "grpc_client_completed_rpc_view not set correctly")
        self.assertEqual(self.rpc_view.grpc_client_started_rpc_view.description,
                         "Number of started client RPCs",
                         "grpc_client_started_rpc_view not set correctly")
        self.assertEqual(self.rpc_view.grpc_client_sent_messages_per_rpc_view.name,
                         "grpc.io/client/sent_messages_per_rpc",
                         "grpc_client_sent_messages_per_rpc_view not set correctly")
        self.assertEqual(self.rpc_view.grpc_client_received_messages_per_rpc_view.description,
                         "Number of response messages received per RPC",
                         "grpc_client_received_messages_per_rpc_view not set correctly")
        self.assertEqual(self.rpc_view.grpc_client_server_latency_view.measure.get_unit(),
                         "ms",
                         "grpc_client_server_latency_view not set correctly")
        self.assertEqual(self.rpc_view.grpc_client_sent_messages_per_method_view.name,
                         "grpc.io/client/sent_messages_per_method",
                         "grpc_client_sent_messages_per_method_view not set correctly")
        self.assertEqual(self.rpc_view.grpc_client_received_messages_per_method_view.description,
                         "Number of messages received",
                         "grpc_client_received_messages_per_method_view not set correctly")
        self.assertEqual(self.rpc_view.grpc_client_sent_bytes_per_method_view.measure.get_unit(),
                         "by",
                         "grpc_client_sent_bytes_per_method_view not set correctly")
        self.assertEqual(self.rpc_view.grpc_client_received_bytes_per_method_view.name,
                         "grpc.io/client/received_bytes_per_method",
                         "grpc_client_received_bytes_per_method_view not set correctly")

    def test_server_measures(self):
        # Test default server views
        self.assertEqual(self.rpc_view.grpc_server_received_bytes_per_rpc.name,
                         "grpc.io/server/received_bytes_per_rpc",
                         "grpc_server_received_bytes_per_rpc view not set correctly")

<<<<<<< HEAD
        self.assertEqual(self.rpc_view.grpc_server_sent_bytes_per_rpc.name,
                         "grpc.io/server/sent_bytes_per_rpc",
                         "grpc_server_sent_bytes_per_rpc view not set correctly")

        self.assertEqual(self.rpc_view.grpc_server_server_latency.name,
                         "grpc.io/server/server_latency",
                         "grpc_server_server_latency view not set correctly")

        self.assertEqual(self.rpc_view.grpc_server_completed_rpcs.name,
                         "grpc.io/server/completed_rpcs",
                         "grpc_server_completed_rpcs view not set correctly")
        
        self.assertEqual(self.rpc_view.grpc_server_started_rpcs.name,
                         "grpc.io/server/started_rpcs",
                         "grpc_server_started_rpcs view not set correctly")
        
        # Test extra server views
        self.assertEqual(self.rpc_view.grpc_server_received_messages_per_rpc.name,
                         "grpc.io/server/received_messages_per_rpc",
                         "grpc_server_received_messages_per_rpc view not set correctly")

        self.assertEqual(self.rpc_view.grpc_server_sent_messages_per_rpc.name,
                         "grpc.io/server/sent_messages_per_rpc",
                         "grpc_server_sent_messages_per_rpc view not set correctly")

        self.assertEqual(self.rpc_view.grpc_server_sent_messages_per_method.name,
                         "grpc.io/server/sent_messages_per_method",
                         "grpc_server_sent_messages_per_method view not set correctly")

        self.assertEqual(self.rpc_view.grpc_server_received_messages_per_method.name,
                         "grpc.io/server/received_messages_per_method",
                         "grpc_server_received_messages_per_method view not set correctly")

        self.assertEqual(self.rpc_view.grpc_server_sent_bytes_per_method.name,
                         "grpc.io/server/sent_bytes_per_method",
                         "grpc_server_sent_bytes_per_method view not set correctly")

        self.assertEqual(self.rpc_view.grpc_server_received_bytes_per_method.name,
                         "grpc.io/server/received_bytes_per_method",
                         "grpc_server_received_bytes_per_method view not set correctly")

=======
>>>>>>> 75179e5b9254b5296c4771146b5d3d00d861a813
if __name__ == '__main__':
    unittest.main()
