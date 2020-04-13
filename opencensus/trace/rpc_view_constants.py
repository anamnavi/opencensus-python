from opencensus.stats import aggregation
from opencensus.stats.aggregation import CountAggregation
from opencensus.stats.aggregation import SumAggregation
from opencensus.stats.aggregation import DistributionAggregation
from opencensus.stats import view

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
    mean = aggregation.mean.new_aggregation_data() #needs to be implemented
    count = CountAggregation.new_aggregation_data()
    sum = SumAggregation.new_aggregation_data()