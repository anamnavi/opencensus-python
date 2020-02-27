from flask import Flask, escape, request, render_template, jsonify
from flask_cors import CORS
from opencensus.trace.tracer import Tracer
from opencensus.trace.samplers import AlwaysOnSampler
from opencensus.stats import stats as stats_module

tracer = Tracer(sampler=AlwaysOnSampler())

stats = stats_module.stats
view_manager = stats.view_manager
stats_recorder = stats.stats_recorder



app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    names = {'name1': "Anam", 'name2': "Gaven", "name3": "Aasiyah"}
    return render_template("index.html", names=names)

@app.route('/getmethod1', methods=['GET'])
def getData1():
    name = "Anam Navied"
    test_data = {'name': name}
    return test_data

@app.route('/getmethod2', methods=['GET'])
def getData2():
    name = "Gaven Kerr"
    test_data = {'name': name}
    return test_data

@app.route('/getmethod3', methods=['GET'])
def getData3():
    name = "Aasiyah Feisal"
    test_data = {'name': name}
    return test_data

# Example for creating nested spans taken from opencensus-python wiki/documentation
# with tracer.span(name='span1'):
#     getData1()
# with tracer.span(name='span2'):
#     getData2()
# with tracer.span(name='span2'):
#     getData3()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)