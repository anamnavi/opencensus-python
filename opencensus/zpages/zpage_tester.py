from opencensus.stats import view_manager as view_manager_module

#Tags.java, Tagger.java, TagValue.java
from opencensus.tags import tag_value as tag_value_module
from opencensus.stats import stats
from opencensus.trace import tracer
from opencensus.tags import tag
from opencensus.tags import tag_value
from opencensus.zpages import zpage_handlers

class ZPage_Tester():

    # tagger = tag.getTagger(); #of type Tagger in java todo
    tracer = tracer.tracer #of type Tracer
    statsRecorder = stats.stats_recorder #of type StatsRecorder

    SPAN_NAME = "EXAMPLE_SPAN"
    METHOD = tag_value("ExampleMethod")

    def __init__(self):
        # no body, does nothing


    def record_example_data():
        pass

    def  main(self):
        record_example_data()

if __name__ == '__main__':
    zpage_Handlers.start_http_server_and_register_all(8080)
    ZPage_Tester.record_example_data()





