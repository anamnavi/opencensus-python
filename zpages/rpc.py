"""
rpc.py is for collecting rpc data from an application, processing it,
and displaying it on a RPC zpage.

Uses stats, tracer, view_manager objects from opencensus framework
"""
from flask import Flask, escape, request, render_template
from typing import NamedTuple
import sys
from opencensus.stats import view as view_module
from opencensus.stats import view_manager as view_manager_module
import datetime


app = Flask(__name__)

manager = view_manager_module.ViewManager()

print(sys.path)


class stat_snapshot(NamedTuple):
    """
    stores and represents the essential rpc data needed for a row displayed on the rpc zpage
    """
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


class stat_group(NamedTuple):
    """
    stores and represents the row data (stat_snapshot) as well as which table this would fall under
    on the rpc zpage tables


    """
    direction: str
    snapshots: list # of type statSnapshot, can't specify explicitly but will only consist of this


class stat_page(NamedTuple):
    statgroups: list # of type statGroup, can't specify explicitly but will only consist of this


def get_stats_snapshots(map, views):
    for view in views :
        view_data = manager.get_view(manager,view.name)
        if view_data is None:
            continue
        for entry in view_data.tag_value_aggregation_data_map():
            tag_values = entry # Entry<List</*@Nullable*/ TagValue>, AggregationData> entry
        #     if len(tag_values):
        #
        #
        # old
        # for key in view_data.tag_value_aggregation_data_map(view_data).keys():
        #     method = "" if key is None else key.asString()
        #     snapshot = stat_snapshot(map.get(method))
        #     if (snapshot is None) :
        #         snapshot = stat_snapshot()
        #         map.put(method, snapshot)

        #TODO getStats(snapshot, entry.getValue(), view, view_data.getWindowData());


@app.route('/', methods=['GET'])
def main():
    direction_dummy = "Sent"
    test_row = stat_snapshot(method='api_call1()',
                             received=False,
                             countMinute=1,
                             countHour=2,
                             countTotal=3,
                             avgLatencyMinute='2020-02-18 23:46:31.243168',
                             avgLatencyHour='2020-02-18 23:46:31.243168',
                             avgLatencyTotal='2020-02-18 23:46:31.243168',
                             rpcRateMinute=1.1,
                             rpcRateHour=1.2,
                             rpcRateTotal=1.3,
                             inputRateMinute=2.1,
                             inputRateHour=2.2,
                             inputRateTotal=2.3,
                             outputRateMinute=3.1,
                             outputRateHour=3.2,
                             outputRateTotal=3.3,
                             errorsMinute=4,
                             errorsHour=5,
                             errorsTotal=6)
    return render_template("index.html", Direction=direction_dummy, obj=test_row)


if __name__ == '__main__':
    app.run(debug=True)
