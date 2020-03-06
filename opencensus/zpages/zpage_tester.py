#Tags.java, Tagger.java, TagValue.java
from opencensus.tags import tag_value as tag_value_module
from opencensus.stats import stats
from opencensus.trace import tracer
from opencensus.tags import tag
from opencensus.tags import tag_value
from opencensus.tags import tag_key
from opencensus.zpages import zpage_handlers
from opencensus.stats import measurement_map
from opencensus.stats import stats_recorder


"""
these classes are not present within Python
"""
# import io.opencensus.tags.Tagger;
# import io.opencensus.trace.SpanBuilder;
# import io.opencensus.trace.Tracing;
# from io.opencensus.common.Scope import scope

"""
this is present within Python but the code is under opencensus.trace.samplers.__init__.py
and I'm not sure if you can import a __init__.py module like that
"""
# import io.opencensus.trace.samplers.Samplers

"""
constants for rpc measurements
todo: move to other file with just these constants or use dict with Tag_Key objects
and then import with similar statements:

import io.opencensus.contrib.grpc.metrics.RpcMeasureConstants;
import io.opencensus.contrib.grpc.metrics.RpcViews;
"""

# client measurements
GRPC_CLIENT_STARTED_RPCS = tag_key("client/started_rpcs")
RPC_CLIENT_FINISHED_COUNT = tag_key("client/finished_count")
GRPC_CLIENT_ROUNDTRIP_LATENCY = tag_key("client/roundtrip_latency")
GRPC_CLIENT_SENT_MESSAGES_PER_RPC = tag_key("client/sent_messages_per_rpc")
GRPC_CLIENT_RECEIVED_MESSAGES_PER_RPC = tag_key("client/received_messages_per_rpc")
GRPC_CLIENT_SENT_BYTES_PER_RPC = tag_key("client/sent_bytes_per_rpc")
GRPC_CLIENT_RECEIVED_BYTES_PER_RPC = tag_key("client/received_bytes_per_rpc")
RPC_CLIENT_UNCOMPRESSED_REQUEST_BYTES = tag_key("client/uncompressed_request_bytes")
RPC_CLIENT_UNCOMPRESSED_RESPONSE_BYTES = tag_key("client/uncompressed_response_bytes")

#server measurements
GRPC_SERVER_STARTED_RPCS = tag_key("server/started_rpcs")
RPC_SERVER_FINISHED_COUNT = tag_key("server/finished_count")
GRPC_SERVER_SERVER_LATENCY = tag_key("server/server_latency")
GRPC_SERVER_RECEIVED_MESSAGES_PER_RPC = tag_key("server/received_messages_per_rpc")
GRPC_SERVER_SENT_MESSAGES_PER_RPC = tag_key("server/sent_messages_per_rpc")
GRPC_SERVER_RECEIVED_BYTES_PER_RPC = tag_key("server/uncompressed_request_bytes")
GRPC_SERVER_SENT_BYTES_PER_RPC = tag_key("server/sent_bytes_per_rpc")
RPC_SERVER_UNCOMPRESSED_REQUEST_BYTES = tag_key("server/uncompressed_request_bytes")
RPC_SERVER_UNCOMPRESSED_RESPONSE_BYTES = tag_key("server/uncompressed_response_bytes")



class ZPage_Tester():
    """
    class used to represent the application that sends data over to the zpagehandler classes
    """

    # tagger = tag.getTagger(); #of type Tagger in java todo: create this class?
    tracer = tracer.tracer #of type Tracer
    statsRecorder = stats.stats_recorder #of type StatsRecorder

    SPAN_NAME = "EXAMPLE_SPAN"
    METHOD = tag_value("ExampleMethod")

    def __init__(self):
        pass


    def record_example_data(self):
        Tracing.getExportComponent().getSampledSpanStore().registerSpanNamesForCollection(Collections.singletonList(SPAN_NAME));
        #use old rpc constants to get interval stats
        RpcViews.registerAllViews();

        #try to create the scope
        try:
            spanBuilder = tracer.spanbuilder(SPAN_NAME).setRecordEvents(true).setSampler(Sampler.alwaysSample())
        except:
            print("some error happened")
        else:
            tracer.current_span() #or maybe tracer.current_span().add_attribute_to_current_span() last one is in tracer
            tracer.span().add_annotation("Starts recording")

            measure_map = stats_recorder.new_measurement_map()
            measure_map[GRPC_CLIENT_STARTED_RPCS] = 1
            measure_map[RPC_CLIENT_FINISHED_COUNT] = 1
            measure_map[GRPC_CLIENT_ROUNDTRIP_LATENCY] = 1.0
            measure_map[GRPC_SERVER_RECEIVED_MESSAGES_PER_RPC] = 1
            measure_map[GRPC_CLIENT_RECEIVED_MESSAGES_PER_RPC] = 1
            measure_map[GRPC_CLIENT_SENT_BYTES_PER_RPC] = 1e5
            measure_map[GRPC_CLIENT_RECEIVED_BYTES_PER_RPC] = 1e5
            measure_map[RPC_CLIENT_UNCOMPRESSED_REQUEST_BYTES] = 1e5
            measure_map[RPC_CLIENT_UNCOMPRESSED_RESPONSE_BYTES] = 1e5
            # server measurements
            measure_map[GRPC_SERVER_STARTED_RPCS] = 1
            measure_map[RPC_SERVER_FINISHED_COUNT] = 1
            measure_map[GRPC_SERVER_SERVER_LATENCY] = 1.0
            measure_map[GRPC_SERVER_RECEIVED_MESSAGES_PER_RPC] = 1
            measure_map[GRPC_SERVER_SENT_MESSAGES_PER_RPC] = 1
            measure_map[GRPC_SERVER_RECEIVED_BYTES_PER_RPC] = 1e5
            measure_map[GRPC_SERVER_SENT_BYTES_PER_RPC] = 1e5
            measure_map[RPC_SERVER_UNCOMPRESSED_REQUEST_BYTES] = 1e5
            measure_map[RPC_SERVER_UNCOMPRESSED_RESPONSE_BYTES] = 1e5

            measure_map.record(tagger) #don't have a tagger object

            tracer.span().add_annotation("Finish recording")



if __name__ == '__main__':
    zpage_handlers.start_http_server_and_register_all(8080)
    ZPage_Tester.record_example_data()





