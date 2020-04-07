# Copyright 2018, OpenCensus Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
app.py is a test Python application script that calls 3 methods, each of which
are wrapped around a Tracer.span object that traces that call/request and represents
that data within a span.
"""

import random
import time
from pprint import pprint
import requests

from opencensus.trace.samplers import AlwaysOnSampler
from opencensus.trace.tracer import Tracer
from opencensus.stats import aggregation as aggregation_module
from opencensus.stats import measure as measure_module
from opencensus.stats import stats as stats_module
from opencensus.stats import view as view_module
from opencensus.tags import tag_key as tag_key_module
from opencensus.tags import tag_map as tag_map_module
from opencensus.tags import tag_value as tag_value_module

from opencensus.trace import config_integration
from opencensus.trace import file_exporter
from opencensus.trace import tracer as tracer_module
from opencensus.trace.propagation import google_cloud_format
from opencensus.trace.samplers import ProbabilitySampler


# constants within the video example on examples/helloworld/main.py
MIB = 1 << 20
FRONTEND_KEY = tag_key_module.TagKey("my.org/keys/frontend")
VIDEO_SIZE_MEASURE = measure_module.MeasureInt(
    "my.org/measures/video_size", "size of processed videos", "By")
VIDEO_SIZE_VIEW_NAME = "my.org/views/video_size"
VIDEO_SIZE_DISTRIBUTION = aggregation_module.DistributionAggregation(
    [0.0, 16.0 * MIB, 256.0 * MIB])
VIDEO_SIZE_VIEW = view_module.View(
    VIDEO_SIZE_VIEW_NAME, "processed video size over time", [FRONTEND_KEY],
    VIDEO_SIZE_MEASURE, VIDEO_SIZE_DISTRIBUTION)


def main():
    """
    Initializes the objects required for recording the rpc data, creates
    the spans, and prints out collected data.
    """

    config_integration.trace_integrations(['httplib'])

    tracer = tracer_module.Tracer(
        exporter=file_exporter.FileExporter(file_name='anam_traces.json'),
        propagator=google_cloud_format.GoogleCloudFormatPropagator(),
        sampler=ProbabilitySampler(rate=0.5),
    )

    stats = stats_module.stats
    view_manager = stats.view_manager
    stats_recorder = stats.stats_recorder
    tracer = Tracer(sampler=AlwaysOnSampler())

    # Register view.
    view_manager.register_view(VIDEO_SIZE_VIEW)

    # Sleep for [0, 10] milliseconds to fake work.
    time.sleep(random.randint(1, 10) / 1000.0)

    # Process video.
    with tracer.span(name='span1'):
        r1 = requests.get('http://localhost:8000/getdata1')
        # get_data1()
    with tracer.span(name='span2'):
        r2 = requests.get('http://localhost:8000/getdata2')
    with tracer.span(name='span3'):
        r3 = requests.get('http://localhost:8000/getdata3')

    # Record the processed video size.
    tag_value = tag_value_module.TagValue("mobile-ios9.3.5")
    tag_map = tag_map_module.TagMap()
    tag_map.insert(FRONTEND_KEY, tag_value)
    measure_map = stats_recorder.new_measurement_map()
    measure_map.measure_int_put(VIDEO_SIZE_MEASURE, 25 * MIB)
    measure_map.record(tag_map)

    # Get aggregated stats and print it to console.
    view_data = view_manager.get_view(VIDEO_SIZE_VIEW_NAME)
    pprint(vars(view_data))
    # temp pylint fix: change back to protected member method by adding underscore in front
    for k, val in view_data.tag_value_aggregation_data_map.items():
        pprint(k)
        pprint(vars(val))

    tracer.exporter.emit(tracer.current_span())
    tracer.exporter.export()


if __name__ == '__main__':
    main()
