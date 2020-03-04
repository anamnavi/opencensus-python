from zpage_handler import ZPageHandler
from opencensus.stats.view_manager import ViewManager
import io

from RpcViewConstants import RPC_CLIENT_ERROR_COUNT_HOUR_VIEW
from RpcViewConstants import RPC_CLIENT_ERROR_COUNT_MINUTE_VIEW
from RpcViewConstants import RPC_CLIENT_ERROR_COUNT_VIEW
from RpcViewConstants import RPC_CLIENT_FINISHED_COUNT_CUMULATIVE_VIEW
from RpcViewConstants import RPC_CLIENT_FINISHED_COUNT_HOUR_VIEW
from RpcViewConstants import RPC_CLIENT_FINISHED_COUNT_MINUTE_VIEW
from RpcViewConstants import RPC_CLIENT_REQUEST_BYTES_HOUR_VIEW
from RpcViewConstants import RPC_CLIENT_REQUEST_BYTES_MINUTE_VIEW
from RpcViewConstants import RPC_CLIENT_REQUEST_BYTES_VIEW
from RpcViewConstants import RPC_CLIENT_REQUEST_COUNT_HOUR_VIEW
from RpcViewConstants import RPC_CLIENT_REQUEST_COUNT_MINUTE_VIEW
from RpcViewConstants import RPC_CLIENT_REQUEST_COUNT_VIEW
from RpcViewConstants import RPC_CLIENT_RESPONSE_BYTES_HOUR_VIEW
from RpcViewConstants import RPC_CLIENT_RESPONSE_BYTES_MINUTE_VIEW
from RpcViewConstants import RPC_CLIENT_RESPONSE_BYTES_VIEW
from RpcViewConstants import RPC_CLIENT_RESPONSE_COUNT_HOUR_VIEW
from RpcViewConstants import RPC_CLIENT_RESPONSE_COUNT_MINUTE_VIEW
from RpcViewConstants import RPC_CLIENT_RESPONSE_COUNT_VIEW
from RpcViewConstants import RPC_CLIENT_ROUNDTRIP_LATENCY_HOUR_VIEW
from RpcViewConstants import RPC_CLIENT_ROUNDTRIP_LATENCY_MINUTE_VIEW
from RpcViewConstants import RPC_CLIENT_ROUNDTRIP_LATENCY_VIEW
from RpcViewConstants import RPC_CLIENT_STARTED_COUNT_CUMULATIVE_VIEW
from RpcViewConstants import RPC_CLIENT_STARTED_COUNT_HOUR_VIEW
from RpcViewConstants import RPC_CLIENT_STARTED_COUNT_MINUTE_VIEW
from RpcViewConstants import RPC_CLIENT_UNCOMPRESSED_REQUEST_BYTES_HOUR_VIEW
from RpcViewConstants import RPC_CLIENT_UNCOMPRESSED_REQUEST_BYTES_MINUTE_VIEW
from RpcViewConstants import RPC_CLIENT_UNCOMPRESSED_REQUEST_BYTES_VIEW
from RpcViewConstants import RPC_CLIENT_UNCOMPRESSED_RESPONSE_BYTES_HOUR_VIEW
from RpcViewConstants import RPC_CLIENT_UNCOMPRESSED_RESPONSE_BYTES_MINUTE_VIEW
from RpcViewConstants import RPC_CLIENT_UNCOMPRESSED_RESPONSE_BYTES_VIEW
from RpcViewConstants import RPC_SERVER_ERROR_COUNT_HOUR_VIEW
from RpcViewConstants import RPC_SERVER_ERROR_COUNT_MINUTE_VIEW
from RpcViewConstants import RPC_SERVER_ERROR_COUNT_VIEW
from RpcViewConstants import RPC_SERVER_FINISHED_COUNT_CUMULATIVE_VIEW
from RpcViewConstants import RPC_SERVER_FINISHED_COUNT_HOUR_VIEW
from RpcViewConstants import RPC_SERVER_FINISHED_COUNT_MINUTE_VIEW
from RpcViewConstants import RPC_SERVER_REQUEST_BYTES_HOUR_VIEW
from RpcViewConstants import RPC_SERVER_REQUEST_BYTES_MINUTE_VIEW
from RpcViewConstants import RPC_SERVER_REQUEST_BYTES_VIEW
from RpcViewConstants import RPC_SERVER_REQUEST_COUNT_HOUR_VIEW
from RpcViewConstants import RPC_SERVER_REQUEST_COUNT_MINUTE_VIEW
from RpcViewConstants import RPC_SERVER_REQUEST_COUNT_VIEW
from RpcViewConstants import RPC_SERVER_RESPONSE_BYTES_HOUR_VIEW
from RpcViewConstants import RPC_SERVER_RESPONSE_BYTES_MINUTE_VIEW
from RpcViewConstants import RPC_SERVER_RESPONSE_BYTES_VIEW
from RpcViewConstants import RPC_SERVER_RESPONSE_COUNT_HOUR_VIEW
from RpcViewConstants import RPC_SERVER_RESPONSE_COUNT_MINUTE_VIEW
from RpcViewConstants import RPC_SERVER_RESPONSE_COUNT_VIEW
from RpcViewConstants import RPC_SERVER_SERVER_ELAPSED_TIME_HOUR_VIEW
from RpcViewConstants import RPC_SERVER_SERVER_LATENCY_HOUR_VIEW
from RpcViewConstants import RPC_SERVER_SERVER_LATENCY_MINUTE_VIEW
from RpcViewConstants import RPC_SERVER_SERVER_LATENCY_VIEW
from RpcViewConstants import RPC_SERVER_STARTED_COUNT_CUMULATIVE_VIEW
from RpcViewConstants import RPC_SERVER_STARTED_COUNT_HOUR_VIEW
from RpcViewConstants import RPC_SERVER_STARTED_COUNT_MINUTE_VIEW
from RpcViewConstants import RPC_SERVER_UNCOMPRESSED_REQUEST_BYTES_HOUR_VIEW
from RpcViewConstants import RPC_SERVER_UNCOMPRESSED_REQUEST_BYTES_MINUTE_VIEW
from RpcViewConstants import RPC_SERVER_UNCOMPRESSED_REQUEST_BYTES_VIEW
from RpcViewConstants import RPC_SERVER_UNCOMPRESSED_RESPONSE_BYTES_HOUR_VIEW
from RpcViewConstants import RPC_SERVER_UNCOMPRESSED_RESPONSE_BYTES_MINUTE_VIEW
from RpcViewConstants import RPC_SERVER_UNCOMPRESSED_RESPONSE_BYTES_VIEW

class RpczZPageHandler():

    my_view_manager = ViewManager()

    RPCZ_URL = "/rpcz"
    SENT = "Sent"
    RECEIVED = "Received"
    SECONDS_PER_MINUTE = 60.0
    SECONDS_PER_HOUR = 3600.0
    NANOS_PER_SECOND = 1e9
    BYTES_PER_KB = 1024

    RPC_STATS_TYPES = ("Count", "Avg latency (ms)", "Rate (rpc/s)", "Input (kb/s)", "Output (kb/s)", "Errors")

    CLIENT_RPC_CUMULATIVE_VIEWS = (
        RPC_CLIENT_ERROR_COUNT_VIEW,
        RPC_CLIENT_ROUNDTRIP_LATENCY_VIEW,
        RPC_CLIENT_REQUEST_BYTES_VIEW,
        RPC_CLIENT_RESPONSE_BYTES_VIEW,
        RPC_CLIENT_STARTED_COUNT_CUMULATIVE_VIEW,
        RPC_CLIENT_REQUEST_COUNT_VIEW,
        RPC_CLIENT_RESPONSE_COUNT_VIEW,
        RPC_CLIENT_UNCOMPRESSED_REQUEST_BYTES_VIEW,
        RPC_CLIENT_UNCOMPRESSED_RESPONSE_BYTES_VIEW,
        RPC_CLIENT_FINISHED_COUNT_CUMULATIVE_VIEW
    )

    SERVER_RPC_CUMULATIVE_VIEWS = (
        RPC_SERVER_ERROR_COUNT_VIEW,
        RPC_SERVER_SERVER_LATENCY_VIEW,
        RPC_SERVER_REQUEST_BYTES_VIEW,
        RPC_SERVER_RESPONSE_BYTES_VIEW,
        RPC_SERVER_STARTED_COUNT_CUMULATIVE_VIEW,
        # The last 5 views are not used yet.
        RPC_SERVER_REQUEST_COUNT_VIEW,
        RPC_SERVER_RESPONSE_COUNT_VIEW,
        RPC_SERVER_UNCOMPRESSED_REQUEST_BYTES_VIEW,
        RPC_SERVER_UNCOMPRESSED_RESPONSE_BYTES_VIEW,
        RPC_SERVER_FINISHED_COUNT_CUMULATIVE_VIEW
    )

    CLIENT_RPC_MINUTE_VIEWS = (
        RPC_CLIENT_ERROR_COUNT_MINUTE_VIEW,
        RPC_CLIENT_ROUNDTRIP_LATENCY_MINUTE_VIEW,
        RPC_CLIENT_REQUEST_BYTES_MINUTE_VIEW,
        RPC_CLIENT_RESPONSE_BYTES_MINUTE_VIEW,
        RPC_CLIENT_STARTED_COUNT_MINUTE_VIEW,
        # The last 5 views are not used yet.
        RPC_CLIENT_REQUEST_COUNT_MINUTE_VIEW,
        RPC_CLIENT_RESPONSE_COUNT_MINUTE_VIEW,
        RPC_CLIENT_UNCOMPRESSED_REQUEST_BYTES_MINUTE_VIEW,
        RPC_CLIENT_UNCOMPRESSED_RESPONSE_BYTES_MINUTE_VIEW,
        RPC_CLIENT_FINISHED_COUNT_MINUTE_VIEW
    )

    SERVER_RPC_MINUTE_VIEWS = (
        RPC_SERVER_ERROR_COUNT_MINUTE_VIEW,
        RPC_SERVER_SERVER_LATENCY_MINUTE_VIEW,
        RPC_SERVER_REQUEST_BYTES_MINUTE_VIEW,
        RPC_SERVER_RESPONSE_BYTES_MINUTE_VIEW,
        RPC_SERVER_STARTED_COUNT_MINUTE_VIEW,
        # The last 5 views are not used yet.
        RPC_SERVER_REQUEST_COUNT_MINUTE_VIEW,
        RPC_SERVER_RESPONSE_COUNT_MINUTE_VIEW,
        RPC_SERVER_UNCOMPRESSED_REQUEST_BYTES_MINUTE_VIEW,
        RPC_SERVER_UNCOMPRESSED_RESPONSE_BYTES_MINUTE_VIEW,
        RPC_SERVER_FINISHED_COUNT_MINUTE_VIEW
    )

    CLIENT_RPC_HOUR_VIEWS = (
        RPC_CLIENT_ERROR_COUNT_HOUR_VIEW,
        RPC_CLIENT_ROUNDTRIP_LATENCY_HOUR_VIEW,
        RPC_CLIENT_REQUEST_BYTES_HOUR_VIEW,
        RPC_CLIENT_RESPONSE_BYTES_HOUR_VIEW,
        RPC_CLIENT_STARTED_COUNT_HOUR_VIEW,
        # The last 5 views are not used yet.
        RPC_CLIENT_REQUEST_COUNT_HOUR_VIEW,
        RPC_CLIENT_RESPONSE_COUNT_HOUR_VIEW,
        RPC_CLIENT_UNCOMPRESSED_REQUEST_BYTES_HOUR_VIEW,
        RPC_CLIENT_UNCOMPRESSED_RESPONSE_BYTES_HOUR_VIEW,
        RPC_CLIENT_FINISHED_COUNT_HOUR_VIEW
    )

    SERVER_RPC_HOUR_VIEWS = (
        RPC_SERVER_ERROR_COUNT_HOUR_VIEW,
        RPC_SERVER_SERVER_LATENCY_HOUR_VIEW,
        RPC_SERVER_SERVER_ELAPSED_TIME_HOUR_VIEW,
        RPC_SERVER_REQUEST_BYTES_HOUR_VIEW,
        RPC_SERVER_RESPONSE_BYTES_HOUR_VIEW,
        RPC_SERVER_STARTED_COUNT_HOUR_VIEW,
        # The last 5 views are not used yet.
        RPC_SERVER_REQUEST_COUNT_HOUR_VIEW,
        RPC_SERVER_RESPONSE_COUNT_HOUR_VIEW,
        RPC_SERVER_UNCOMPRESSED_REQUEST_BYTES_HOUR_VIEW,
        RPC_SERVER_UNCOMPRESSED_RESPONSE_BYTES_HOUR_VIEW,
        RPC_SERVER_FINISHED_COUNT_HOUR_VIEW
    )

    def get_url_path(self):
        return self.RPCZ_URL

    # Here we will need to do HTML writing
    def emitStyle(self, out): 
        print("TODO")
        # out.write("<style>\n")
        # out.write(Style.style)
        # out.write("</style>\n")

    def emitHtml(self, dict, out):
        print("TODO")
#     PrintWriter out =
#         new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream, Charsets.UTF_8)));
#     out.write("<!DOCTYPE html>\n");
#     out.write("<html lang=\"en\"><head>\n");
#     out.write("<meta charset=\"utf-8\">\n");
#     out.write("<title>RpcZ</title>\n");
#     out.write("<link rel=\"shortcut icon\" href=\"https://opencensus.io/images/favicon.ico\"/>\n");
#     out.write(
#         "<link href=\"https://fonts.googleapis.com/css?family=Open+Sans:300\""
#             + "rel=\"stylesheet\">\n");
#     out.write(
#         "<link href=\"https://fonts.googleapis.com/css?family=Roboto\"" + "rel=\"stylesheet\">\n");
#     emitStyle(out);
#     out.write("</head>\n");
#     out.write("<body>\n");
#     try {
#       emitHtmlBody(out);
#     } catch (Throwable t) {
#       out.write("Errors while generate the HTML page " + t);
#     }
#     out.write("</body>\n");
#     out.write("</html>\n");
#     out.close();
#   }

#   private void emitHtmlBody(PrintWriter out) {
#     Formatter formatter = new Formatter(out, Locale.US);
#     out.write(
#         "<p class=\"header\">"
#             + "<img class=\"oc\" src=\"https://opencensus.io/img/logo-sm.svg\" />"
#             + "Open<span>Census</span></p>");
#     out.write("<h1>RPC Stats</h1>");
#     out.write("<p></p>");
#     emitSummaryTable(out, formatter, /* isReceived= */ false);
#     emitSummaryTable(out, formatter, /* isReceived= */ true);
#   }

#   private void emitSummaryTable(PrintWriter out, Formatter formatter, boolean isReceived) {
#     formatter.format(
#         "<h2><table class=\"title\"><tr align=left><td><font size=+2>"
#             + "%s</font></td></tr></table></h2>",
#         (isReceived ? RECEIVED : SENT));
#     formatter.format("<table frame=box cellspacing=0 cellpadding=2>");
#     emitSummaryTableHeader(out, formatter);
#     Map<String, StatsSnapshot> snapshots = getStatsSnapshots(isReceived);
#     for (Entry<String, StatsSnapshot> entry : snapshots.entrySet()) {
#       emitSummaryTableRows(out, formatter, entry.getValue(), entry.getKey());
#     }
#     out.write("</table>");
#     out.write("<br />");
#   }


ZPageHandler.register(RpczZPageHandler)


# import datetime
# import sys
# from flask import Flask, escape, request, render_template
# from typing import NamedTuple, List
# from opencensus.stats import view as view_module
# from opencensus.stats import view_manager as view_manager_module



# app = Flask(__name__)

# manager = view_manager_module.ViewManager()

# print(sys.path)


# class stat_snapshot(NamedTuple):
#     """
#     stores and represents the essential rpc data needed for a row displayed on the rpc zpage
#     """
#     method: str
#     received: bool
#     countMinute: int
#     countHour: int
#     countTotal: int
#     avgLatencyMinute: datetime.datetime
#     avgLatencyHour: datetime.datetime
#     avgLatencyTotal: datetime.datetime
#     rpcRateMinute: float
#     rpcRateHour: float
#     rpcRateTotal: float
#     inputRateMinute: float
#     inputRateHour: float
#     inputRateTotal: float
#     outputRateMinute: float
#     outputRateHour: float
#     outputRateTotal: float
#     errorsMinute: int
#     errorsHour: int
#     errorsTotal: int


# class stat_group(NamedTuple):
#     """
#     stores and represents the row data (stat_snapshot) as well as which table this would fall under
#     on the rpc zpage tables

#     :type direction string
#     :param direction: if the rpc is sent or received

#     :type list of class:`~opencensus.zpages.rpc.stat_snapshot`
#     :param snapshots: list of stat_snapshot objects for that specific direction

#     """
#     direction: str
#     snapshots: List[stat_snapshot]


# class stat_page(NamedTuple):
#     """
#     stores and represents all rpc data across different groups and rows of data

#     :type list of class: `~opencensus.zpages.rpc.stat_group`
#     :param statgroups: list of stat groups (received and sent) that together make up a page of stat data
#     """
#     statgroups: List[stat_group]


# def get_stats_snapshots(map, views):
#     """
#     processes the ingested stats data and prints it out

#     : type map: `~opencensus.zpages.rpc.stat_snapshot` todo replace
#     : param map: todo

#     : type views: todo
#     : param view: todo
#     """
#     for view in views :
#         view_data = manager.get_view(manager,view.name)
#         if view_data is None:
#             continue
#         for entry in view_data.tag_value_aggregation_data_map():
#             tag_values = entry # Entry<List</*@Nullable*/ TagValue>, AggregationData> entry
#         #     if len(tag_values):
#         #
#         #
#         # old
#         # for key in view_data.tag_value_aggregation_data_map(view_data).keys():
#         #     method = "" if key is None else key.asString()
#         #     snapshot = stat_snapshot(map.get(method))
#         #     if (snapshot is None) :
#         #         snapshot = stat_snapshot()
#         #         map.put(method, snapshot)

#         # getStats(snapshot, entry.getValue(), view, view_data.getWindowData())


# @app.route('/', methods=['GET'])
# def main():
#     direction_dummy = "Sent"
#     test_row = stat_snapshot(method='api_call1()',
#                              received=False,
#                              countMinute=1,
#                              countHour=2,
#                              countTotal=3,
#                              avgLatencyMinute='2020-02-18 23:46:31.243168',
#                              avgLatencyHour='2020-02-18 23:46:31.243168',
#                              avgLatencyTotal='2020-02-18 23:46:31.243168',
#                              rpcRateMinute=1.1,
#                              rpcRateHour=1.2,
#                              rpcRateTotal=1.3,
#                              inputRateMinute=2.1,
#                              inputRateHour=2.2,
#                              inputRateTotal=2.3,
#                              outputRateMinute=3.1,
#                              outputRateHour=3.2,
#                              outputRateTotal=3.3,
#                              errorsMinute=4,
#                              errorsHour=5,
#                              errorsTotal=6)
#     return render_template("index.html", Direction=direction_dummy, obj=test_row)


# if __name__ == '__main__':
#     app.run(debug=True)
