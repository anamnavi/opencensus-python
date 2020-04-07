from deprecated import deprecated
from opencensus.tags import tag_key
from opencensus.grpc import measure, measure_double, measure_long

class RPCMeasureConstants():
    """
    constants for collecting RPC stats
    """


    def __init__(self):
        """
        needs fixing.
        todo: do I put all the RPC constant fields in here?
        """
        @deprecated(version=0.8, reason="sf")
        rpc_status = tag_key.TagKey("canonical_status") #deprecated

        rpc_method = tag_key.TagKey("method") #deprecated
        grpc_client_status = tag_key.TagKey("grpc_client_status")
        grpc_server_status = tag_key.TagKey("grpc_server_status")
        grpc_client_method = tag_key.TagKey("grpc_client_method")
        grpc_server_method = tag_key.TagKey("grpc_server_method")
        byte = "by"
        count = "1"
        millisecond = "ms"

        # the MeasureDouble and MeasureLong
        grpc_client_sent_bytes_per_rpc = measure_double.MeasureDouble("grpc.io/client/sent_bytes_per_rpc",
                                                                  "Total bytes sent across all request messages per RPC",
                                                                  byte)
        grpc_client_received_bytes_per_rpc = measure_double.MeasureDouble("grpc.io/client/received_bytes_per_rpc",
                                                                      "Total bytes received across all response messages per RPC",
                                                                      byte)
        grpc_client_sent_bytes_per_method = measure_double.MeasureDouble("grpc.io/client/sent_bytes_per_method",
                                                                         "Total bytes sent per method, recorded real-time as bytes are sent.",
                                                                         byte)
        grpc_client_received_bytes_per_method = measure_double.MeasureDouble("grpc.io/client/received_bytes_per_method",
                                                                             "Total bytes received per method, recorded real-time as bytes are received.",
                                                                             byte)
        grpc_client_sent_messages_per_method = measure_long.MeasureLong("grpc.io/client/sent_messages_per_method",
                                                                        "Total messages sent per method.",
                                                                        count)
        grpc_client_received_messages_per_method = measure_long.MeasureLong("grpc.io/client/received_messages_per_method",
                                                                            "Total messages received per method.",
                                                                            count)
        grpc_client_roundtrip_latency = measure_double.MeasureDouble("grpc.io/client/roundtrip_latency",
                                                                     "Time between first byte of request sent to last byte of response received or terminal error.",
                                                                     millisecond)
        grpc_client_sent_messages_per_rpc = measure_long.MeasureLong("grpc.io/client/sent_messages_per_rpc",
                                                                     "Number of messages sent in the RPC",
                                                                     count)
        grpc_client_received_messages_per_rpc = measure_long.MeasureLong("grpc.io/client/received_messages_per_rpc",
                                                                         "Number of response messages received per RPC",
                                                                         count)
        grpc_client_server_latency = measure_double.MeasureDouble("grpc.io/client/server_latency",
                                                                  "Server latency in msecs",
                                                                  millisecond)
        grpc_client_started_rpcs = measure_long.MeasureLong( "grpc.io/client/started_rpcs",
                                                             "Number of started client RPCs.",
                                                             count)
        @deprecated(version=0.8, reason="because error counts can be computed on your metrics backend by totalling the different per-status values")
        rpc_client_error_count = measure_long.MeasureLong("grpc.io/client/error_count",
                                                          "RPC Errors",
                                                          count)
        @deprecated()
        rpc_client_request_bytes = grpc_client_sent_bytes_per_rpc
        @deprecated()
        rpc_client_response_bytes = grpc_client_received_bytes_per_rpc
        @deprecated()
        rpc_client_roundtrip_latency = grpc_client_roundtrip_latency

        @deprecated()
        rpc_client_server_elapsed_time = grpc_client_server_latency

        @deprecated()
        rpc_client_uncompressed_request_bytes = measure_double.MeasureDouble("grpc.io/client/uncompressed_request_bytes",
                                                                             "Uncompressed Request bytes",
                                                                             byte)

        @deprecated()
        rpc_client_uncompressed_response_bytes = measure_double.MeasureDouble("grpc.io/client/uncompressed_response_bytes",
                                                                              "Uncompressed Response bytes",
                                                                              byte)

        @deprecated()
        rpc_client_started_count = grpc_client_started_rpcs

        @deprecated()
        rpc_client_finished_count = measure_long.MeasureLong("grpc.io/client/finished_count",
                                                             "Number of client RPCs (streams) finished",
                                                             count)

        @deprecated()
        rpc_client_request_count = grpc_client_sent_messages_per_rpc

        @deprecated()
        rpc_client_response_count = grpc_client_received_messages_per_rpc
        grpc_server_sent_bytes_per_rpc = measure_double.MeasureDouble("grpc.io/server/sent_bytes_per_rpc",
                                                                      "Total bytes sent across all response messages per RPC",
                                                                      byte)
        grpc_server_received_bytes_per_rpc = measure_double.MeasureDouble("grpc.io/server/received_bytes_per_rpc",
                                                                          "Total bytes received across all messages per RPC",
                                                                          byte)
        grpc_server_sent_bytes_per_method  = measure_double.MeasureDouble("grpc.io/server/sent_bytes_per_method",
                                                                          "Total bytes sent per method, recorded real-time as bytes are sent.",
                                                                          byte)
        grpc_server_received_bytes_per_method = measure_double.MeasureDouble("grpc.io/server/received_bytes_per_method",
                                                                             "Total bytes received per method, recorded real-time as bytes are received.",
                                                                             byte)
        grpc_server_sent_messages_per_method = measure_long.MeasureLong("grpc.io/server/sent_messages_per_method",
                                                                        "Total messages sent per method.",
                                                                        count)
        grpc_server_received_messages_per_method = measure_long.MeasureLong("grpc.io/server/received_messages_per_method",
                                                                            "Total messages received per method.",
                                                                            count)
        grpc_server_sent_messages_per_rpc = measure_long.MeasureLong("grpc.io/server/sent_messages_per_rpc", "Number of messages sent in each RPC", count)
        grpc_server_received_messages_per_rpc = measure_long.MeasureLong("grpc.io/server/received_messages_per_rpc",
                                                                         "Number of messages received in each RPC",
                                                                         count)
        grpc_server_server_latency = measure_double.MeasureDouble("grpc.io/server/server_latency",
                                                                  "Time between first byte of request received to last byte of response sent or terminal error.",
                                                                  millisecond)
        grpc_server_started_rpcs = measure_long.MeasureLong("grpc.io/server/started_rpcs",
                                                            "Number of started server RPCs.",
                                                            count)
        rpc_server_error_count = measure_long.MeasureLong("grpc.io/server/error_count",
                                                          "RPC Errors",
                                                          count)
        rpc_server_request_bytes = grpc_server_sent_bytes_per_rpc
        rpc_server_server_elapsed_time = measure_double.MeasureDouble("grpc.io/server/server_elapsed_time",
                                                                      "Server elapsed time in msecs",
                                                                      millisecond)
        rpc_server_server_latency = grpc_server_server_latency
        rpc_server_uncompressed_request_bytes = measure_double.MeasureDouble("grpc.io/server/uncompressed_request_bytes",
                                                                             "Uncompressed Request bytes",
                                                                             byte)
        rpc_server_uncompressed_response_bytes = measure_double.MeasureDouble("grpc.io/server/uncompressed_response_bytes",
                                                                              "Uncompressed Response bytes",
                                                                              byte)
        rpc_server_started_count =grpc_server_started_rpcs
        rpc_server_finished_count = measure_long.MeasureLong( "grpc.io/server/finished_count",
                                                              "Number of server RPCs (streams) finished",
                                                              count)
        rpc_server_request_count = grpc_server_received_messages_per_rpc
        rpc_server_response_count = grpc_server_sent_messages_per_rpc





