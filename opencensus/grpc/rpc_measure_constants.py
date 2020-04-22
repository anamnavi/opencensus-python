from opencensus.tags import tag_key
from opencensus.stats.measure import BaseMeasure
from opencensus.stats.measure import MeasureInt
from opencensus.stats.measure import MeasureFloat

# import measure


class RPCMeasureConstants:
    """
    constants for collecting RPC stats
    see specs in documentation for opencensus-python
    """
    byte = "by"
    count = "1"
    millisecond = "ms"

    def __init__(self):
        """
        contains all the RPC constants as in the Java implementation
        """

        # client tags

        # gRPC server status code received, e.g. OK, CANCELLED, DEADLINE_EXCEEDED
        self.grpc_client_status = tag_key.TagKey("grpc_client_status")

        # Full gRPC method name, including package, service and method,
        # e.g. google.bigtable.v2.Bigtable/CheckAndMutateRow
        self.grpc_client_method = tag_key.TagKey("grpc_client_method")

        # server tags

        # gRPC server status code returned, e.g. OK, CANCELLED, DEADLINE_EXCEEDED
        self.grpc_server_status = tag_key.TagKey("grpc_server_status")

        # Full gRPC method name, including package, service and method,
        # e.g. com.exampleapi.v4.BookshelfService/Checkout
        self.grpc_server_method = tag_key.TagKey("grpc_server_method")


        # client measures
        self.grpc_client_sent_messages_per_rpc = MeasureInt(
            name="grpc.io/client/sent_messages_per_rpc",
            description="Number of messages sent in the RPC",
            unit=self.count)

        self.grpc_client_sent_bytes_per_rpc = MeasureFloat(
            name="grpc.io/client/sent_bytes_per_rpc",
            description="Total bytes sent across all request messages per RPC",
            unit=self.byte)

        self.grpc_client_received_messages_per_rpc = MeasureInt(
            name="grpc.io/client/received_messages_per_rpc",
            description="Number of response messages received per RPC",
            unit=self.count)

        self.grpc_client_received_bytes_per_rpc = MeasureFloat(
            name="grpc.io/client/received_bytes_per_rpc",
            description="Total bytes received across all response messages per RPC",
            unit=self.byte)

        self.grpc_client_roundtrip_latency = MeasureFloat(
            name="grpc.io/client/roundtrip_latency",
            description="Time between first byte of request sent to"
                        " last byte of response received or terminal error.",
            unit=self.millisecond)

        self.grpc_client_server_latency = MeasureFloat(
            name="grpc.io/client/server_latency",
            description="Server latency in msecs",
            unit=self.millisecond)

        self.grpc_client_started_rpcs = MeasureInt(
            name="grpc.io/client/started_rpcs",
            description="Number of started client RPCs.",
            unit=self.count)

        self.grpc_client_sent_messages_per_method = MeasureInt(
            name="grpc.io/client/sent_messages_per_method",
            description="Total messages sent per method.",
            unit=self.count)

        self.grpc_client_received_messages_per_method = MeasureInt(
            name="grpc.io/client/received_messages_per_method",
            description="Total messages received per method.",
            unit=self.count)

        self.grpc_client_sent_bytes_per_method = MeasureFloat(
            name="grpc.io/client/sent_bytes_per_method",
            description="Total bytes sent per method, recorded real-time as bytes are sent.",
            unit=self.byte)

        self.grpc_client_received_bytes_per_method = MeasureFloat(
            name="grpc.io/client/received_bytes_per_method",
            description="Total bytes received per method,"
                        " recorded real-time as bytes are received.",
            unit=self.byte)

        # server measures
        self.grpc_server_received_messages_per_rpc = MeasureInt(
            name="grpc.io/server/received_messages_per_rpc",
            description="Number of messages received in each RPC",
            unit=self.count)

        self.grpc_server_received_bytes_per_rpc = MeasureFloat(
            name="grpc.io/server/received_bytes_per_rpc",
            description="Total bytes received across all messages per RPC",
            unit=self.byte)

        self.grpc_server_sent_messages_per_rpc = MeasureInt(
            name="grpc.io/server/sent_messages_per_rpc",
            description="Number of messages sent in each RPC",
            unit=self.count)

        self.grpc_server_sent_bytes_per_rpc = MeasureFloat(
            name="grpc.io/server/sent_bytes_per_rpc",
            description="Total bytes sent across all response messages per RPC",
            unit=self.byte)

        self.grpc_server_server_latency = MeasureFloat(
            name="grpc.io/server/server_latency",
            description="Time between first byte of request received"
                        " to last byte of response sent or terminal error.",
            unit=self.millisecond)

        self.grpc_server_started_rpcs = MeasureInt(
            name="grpc.io/server/started_rpcs",
            description="Number of started server RPCs.",
            unit=self.count)

        self.grpc_server_sent_messages_per_method = MeasureInt(
            name="grpc.io/server/sent_messages_per_method",
            description="Total messages sent per method.",
            unit=self.count)

        self.grpc_server_received_messages_per_method = MeasureInt(
            name="grpc.io/server/received_messages_per_method",
            description="Total messages received per method.",
            unit=self.count)

        self.grpc_server_sent_bytes_per_method = MeasureFloat(
            name="grpc.io/server/sent_bytes_per_method",
            description="Total bytes sent per method, recorded real-time as bytes are sent.",
            unit=self.byte)

        self.grpc_server_received_bytes_per_method = MeasureFloat(
            name="grpc.io/server/received_bytes_per_method",
            description="Total bytes received per method, recorded real-time as bytes are received.",
            unit=self.byte)
