import requests
from opencensus.trace.tracer import Tracer
from opencensus.trace.samplers import AlwaysOnSampler
from opencensus.stats import stats as stats_module

tracer = Tracer(sampler=AlwaysOnSampler())

stats = stats_module.stats
view_manager = stats.view_manager
stats_recorder = stats.stats_recorder

with tracer.span(name='span1'):
    r1 = requests.get('http://localhost:8000/getmethod1')
    print("Call to method 1: ", r1.status_code, ", " + r1.text)
with tracer.span(name='span2'):
    r2 = requests.get('http://localhost:8000/getmethod2')
    print("Call to method 2: ", r2.status_code, ", " + r2.text)
with tracer.span(name='span3'):
    r3 = requests.get('http://localhost:8000/getmethod3')
    print("Call to method 3: ", r3.status_code, ", " + r3.text)
    print(r3.json()['name'])
