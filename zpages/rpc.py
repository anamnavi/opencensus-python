from flask import Flask, escape, request, render_template
from typing import NamedTuple
import datetime

app = Flask(__name__)


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


@app.route('/')
def showPage():
    directionDummy = "Sent"
    test_row = statSnapshot('apicall1()', False, 1, 2, 3, '2020-02-18 23:46:31.243168', '2020-02-18 23:46:31.243168', '2020-02-18 23:46:31.243168', 1.1, 1.2, 1.3, 2.1, 2.2, 2.3, 3.1, 3.2, 3.3, 4, 5, 6)
    # template_values = {'Direction': directionDummy}
    # path = os.path.join(os.path.dirname(__file__), 'index.html')
    # self.response.out.write(template.render(path, template_values))

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
