from opencensus.stats import aggregation
from opencensus.stats.aggregation import CountAggregation
from opencensus.stats.aggregation import SumAggregation
from opencensus.stats.aggregation import DistributionAggregation
from opencensus.stats import bucket_boundaries
from opencensus.stats import view
import rpc_measure_constants


class RPCViewConstants:
    """
    constants for exporting views on RPC stats
    """

    #buckets for distributions in defaults
    #  Common histogram bucket boundaries for bytes received/sets Views (in bytes).
    rpc_bytes_bucket_boundaries = [0, 1024, 2048, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216,
                                   67108864, 268435456, 1073741824, 4294967296]
    #  Common histogram bucket boundaries for latency and elapsed-time Views (in milliseconds).
    rpc_millis_bucket_boundaries = [0.0, 0.01, 0.05, 0.1, 0.3, 0.6, 0.8, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0,
                                    8.0, 10.0, 13.0, 16.0, 20.0, 25.0, 30.0, 40.0, 50.0, 65.0, 80.0, 100.0,
                                    130.0, 160.0, 200.0, 250.0, 300.0, 400.0, 500.0, 650.0, 800.0,
                                    1000.0, 2000.0, 5000.0, 10000.0, 20000.0, 50000.0, 100000.0]
    #  Common histogram bucket boundaries for request/response count Views (no unit).
    rpc_count_bucket_boundaries = [0.0, 1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0, 128.0, 256.0, 512.0, 1024.0,
                                   2048.0, 4096.0, 8192.0, 16384.0, 32768.0, 65536.0]

    # constants
    # mean = aggregation.mean.new_aggregation_data() # todo needs to be implemented
    count = CountAggregation.new_aggregation_data()
    sum = SumAggregation.new_aggregation_data()

    distrib_bytes = DistributionAggregation(bucket_boundaries.BucketBoundaries(rpc_bytes_bucket_boundaries))
    aggregation_with_bytes_histogram = distrib_bytes.new_aggregation_data()

    distrib_millis = DistributionAggregation(bucket_boundaries.BucketBoundaries(rpc_millis_bucket_boundaries))
    aggregation_with_millis_histogram = distrib_millis.new_aggregation_data()

    distrib_count = DistributionAggregation(bucket_boundaries.BucketBoundaries(rpc_count_bucket_boundaries))
    aggregation_with_count_histogram = distrib_count.new_aggregation_data()

    # # todo ceaate and use Duration class
    # minute =
    # hour =
    #
    # # todo
    # cumulative =
    # interval_minute =
    # interval_hour =

    """
    rpc client views:
    The following set of views are considered minimum required to monitor client-side performance:
    """
    grpc_client_sent_bytes_per_rpc_view = view.View(name="grpc.io/client/sent_bytes_per_rpc",
                                                    description="Sent bytes per RPC",
                                                    columns=[rpc_measure_constants.grpc_client_method],
                                                    measure=rpc_measure_constants.GRPC_CLIENT_SENT_BYTES_PER_RPC,
                                                    aggregation=aggregation_with_bytes_histogram)

    grpc_client_received_bytes_per_rpc_view = view.View(name="grpc.io/client/received_bytes_per_rpc",
                                                        description="Received bytes per RPC",
                                                        columns=[rpc_measure_constants.grpc_client_method],
                                                        measure=rpc_measure_constants.grpc_client_received_bytes_per_rpc,
                                                        aggregation=aggregation_with_bytes_histogram)

    grpc_client_roundtrip_latency_view = view.View(name="grpc.io/client/roundtrip_latency",
                                                   description="Latency in msecs",
                                                   columns=[rpc_measure_constants.grpc_client_method],
                                                   measure=rpc_measure_constants.GRPC_CLIENT_ROUNDTRIP_LATENCY,
                                                   aggregation=aggregation_with_millis_histogram)

    grpc_client_completed_rpc_view = view.View(name="grpc.io/client/completed_rpcs",
                                               description="Number of completed client RPCs",
                                               columns=[rpc_measure_constants.grpc_client_method, rpc_measure_constants.grpc_client_status],
                                               measure=rpc_measure_constants.grpc_client_roundtrip_latency,
                                               aggregation=count)

    grpc_client_started_rpc_view = view.View(name="grpc.io/client/started_rpcs",
                                             description="Number of started client RPCs",
                                             columns=[rpc_measure_constants.grpc_client_method],
                                             measure=rpc_measure_constants.grpc_client_started_rpcs,
                                             aggregation=count)

    # Extra Views: The following set of views are considered useful but not mandatory to monitor client side performance
    grpc_client_sent_messages_per_rpc_view = view.View(name="grpc.io/client/sent_messages_per_rpc",
                                                       description="Number of messages sent in the RPC",
                                                       columns=[rpc_measure_constants.grpc_client_method],
                                                       measure=rpc_measure_constants.grpc_client_sent_messages_per_rpc,
                                                       aggregation=aggregation_with_count_histogram)

    grpc_client_received_messages_per_rpc_view = view.View(name="grpc.io/client/received_messages_per_rpc",
                                                           description="Number of response messages received per RPC",
                                                           columns=[rpc_measure_constants.grpc_client_method],
                                                           measure=rpc_measure_constants.grpc_client_received_messages_per_rpc,
                                                           aggregation=aggregation_with_count_histogram)

    grpc_client_server_latency_view = view.View(name="grpc.io/client/server_latency",
                                                description="Server latency in msecs",
                                                columns=[rpc_measure_constants.grpc_client_method],
                                                measure=rpc_measure_constants.grpc_client_server_latency,
                                                aggregation=aggregation_with_millis_histogram)

    grpc_client_sent_messages_per_method_view = view.View(name="grpc.io/client/sent_messages_per_method",
                                                          description="Number of messages sent",
                                                          columns=[rpc_measure_constants.grpc_client_method],
                                                          measure=rpc_measure_constants.grpc_client_sent_messages_per_method,
                                                          aggregation=count)

    grpc_client_received_messages_per_method_view = view.View(name="grpc.io/client/received_messages_per_method",
                                                              description="Number of messages received",
                                                              columns=[rpc_measure_constants.grpc_client_method],
                                                              measure=rpc_measure_constants.grpc_client_received_messages_per_method,
                                                              aggregation=count)
    grpc_client_sent_bytes_per_method_view = view.View(name="grpc.io/client/sent_bytes_per_method",
                                                       description="Sent bytes per method",
                                                       columns=[rpc_measure_constants.grpc_client_method],
                                                       measure=rpc_measure_constants.grpc_client_sent_bytes_per_method,
                                                       aggregation=sum)

    grpc_client_received_bytes_per_method_view = view.View(name="grpc.io/client/received_bytes_per_method",
                                                           description="Received bytes per method",
                                                           columns=[rpc_measure_constants.grpc_client_method],
                                                           measure=rpc_measure_constants.grpc_client_received_bytes_per_method,
                                                           aggregation=sum)



