from flask import Flask, escape, request, render_template
from typing import NamedTuple
import sys
from opencensus.stats import view as view_module
from opencensus.stats import view_manager as view_manager_module
import datetime


app = Flask(__name__)

manager = view_manager_module.ViewManager()

print(sys.path)

class statSnapshot(NamedTuple):
    method: str
    received: bool
    countMinute: int
    countHour: int
    countTotal: int
    avgLatencyMinute: datetime.datetime
    avgLatencyHour: datetime.datetime
    avgLatencyTotal: datetime.datetime
    rpcRateMinute: float
    rpcRateHour: float
    rpcRateTotal: float
    inputRateMinute: float
    inputRateHour: float
    inputRateTotal: float
    outputRateMinute: float
    outputRateHour: float
    outputRateTotal: float
    errorsMinute: int
    errorsHour: int
    errorsTotal: int


class statGroup(NamedTuple):
    direction: str
    snapshots: list # of type statSnapshot, can't specify explicitly but will only consist of this


class statPage(NamedTuple):
    statgroups: list # of type statGroup, can't specify explicitly but will only consist of this

def getStatsSnapshots(map, views) :
    for view in views :
      view_data = manager.get_view(manager,view.name)
      if view_data is None:
        continue
      for key in view_data.tag_value_aggregation_data_map(view_data).keys():
        method = "" if key is None else key.asString()
        snapshot = statSnapshot(map.get(method))
        if (snapshot is None) :
          snapshot = statSnapshot()
          map.put(method, snapshot)

        #TODO getStats(snapshot, entry.getValue(), view, view_data.getWindowData());


@app.route('/')
def showPage():
    directionDummy = "Sent"
    test_row = statSnapshot('apicall1()', False, 1, 2, 3, '2020-02-18 23:46:31.243168', '2020-02-18 23:46:31.243168', '2020-02-18 23:46:31.243168', 1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 3.1, 3.2, 3.3, 4, 5, 6)


    return render_template("index.html", Direction=directionDummy,
                           method=test_row.method,
                           countMinute=test_row.countMinute,
                           countHour=test_row.countHour,
                           countTotal=test_row.countTotal,
                           avgLatencyMinute=test_row.avgLatencyMinute,
                           avgLatencyHour=test_row.avgLatencyHour,
                           avgLatencyTotal=test_row.avgLatencyTotal,
                           rpcRateMinute=test_row.rpcRateMinute,
                           rpcRateHour=test_row.rpcRateHour,
                           rpcRateTotal=test_row.rpcRateTotal,
                           inputRateMinute=test_row.inputRateMinute,
                           inputRateHour=test_row.inputRateHour,
                           inputRateTotal=test_row.inputRateTotal,
                           outputRateMinute=test_row.outputRateMinute,
                           outputRateHour=test_row.outputRateHour,
                           outputRateTotal=test_row.outputRateTotal,
                           errorsMinute=test_row.errorsMinute,
                           errorsHour=test_row.errorsHour,
                           errorsTotal=test_row.errorsTotal)

if __name__ == '__main__':
    app.run(debug=True)
