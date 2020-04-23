import io
from datetime import time, datetime
from typing import NamedTuple

from opencensus.stats.view_manager import ViewManager

from style import Style
from zpage_handler import ZPageHandler

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

    manager = ViewManager()

    RPCZ_URL = "/rpcz"
    SENT = "Sent"
    RECEIVED = "Received"
    SECONDS_PER_MINUTE = 60.0
    SECONDS_PER_HOUR = 3600.0
    NANOS_PER_SECOND = 1e9
    BYTES_PER_KB = 1024

    RPC_STATS_TYPES = ("Count", \
        "Avg latency (ms)", \
        "Rate (rpc/s)", \
        "Input (kb/s)", \
        "Output (kb/s)", \
        "Errors")

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
    def emit_style(self, out):
        print("TODO")
        out.write("<style>\n")
        out.write(Style.style)
        out.write("</style>\n")

    def emit_html(self, out):
        out = io.StringIO()
        out.write("<!DOCTYPE html>\n")
        out.write("<html lang=\"en\"><head>\n")
        out.write("<meta charset=\"utf-8\">\n")
        out.write("<title>RpcZ</title>\n")
        out.write("<link rel=\"shortcut icon\" \
            href=\"https://opencensus.io/images/favicon.ico\"/>\n")
        out.write("<link \
            href=\"https://fonts.googleapis.com/css?family=Open+Sans:300\"rel=\"stylesheet\">\n")
        out.write("<link \
            href=\"https://fonts.googleapis.com/css?family=Roboto\"" + "rel=\"stylesheet\">\n")
        self.emit_style(out)
        out.write("</head>\n")
        out.write("<body>\n")
        try:
            emit_html_body(self, out)
        except:
            out.write("Errors while generate the HTML page ")
        out.write("</body>\n")
        out.write("</html>\n")
        out.close()

    def emit_html_body(self, out):
        out.write("<p class=\"header\"><img class=\"oc\" \
            src=\"https://opencensus.io/img/logo-sm.svg\" />Open<span>Census</span></p>")
        out.write("<h1>RPC Stats</h1>")
        out.write("<p></p>")
        self.emit_summary_table(out, False)
        self.emit_summary_table(out, True)

    def emit_summary_table(self, out, is_received):
        format_str = "<h2><table class=\"title\"><tr align=left><td><font size=+2> \
            {}</font></td></tr></table></h2>"
        format_str.format(self.RECEIVED if is_received else self.SENT)
        out.write(format_str)
        format_str = "<table frame=box cellspacing=0 cellpadding=2>"
        out.write(format_str)
        self.emit_summary_table_header(out)
        snapshots = self.get_stats_snapshots(is_received)
        for entry in snapshots: #check what snapshot returns
            self.emit_summary_table_rows(out, snapshots[entry], entry) #check what entry contrains
        out.write("</table>")
        out.write("<br />")

    def emit_summary_table_header(self, out):
        #First line.
        out.write("<tr bgcolor=#A94442>")
        out.write("<th></th><td></td>")
        for rpc_stats_type in self.RPC_STATS_TYPES:
            formatter = "<th class=\"borderLB\" colspan=3>{}</th>"
            to_print = formatter.format(rpc_stats_type)
            out.write(to_print)
        out.write("</tr>")

        #Second line.
        out.write("<tr bgcolor=#A94442>")
        out.write("<th align=left>Method</th>\n")
        out.write("<td bgcolor=#A94442>&nbsp;&nbsp;&nbsp;&nbsp;</td>")
        for index in range(0, len(self.RPC_STATS_TYPES)):
            out.write("<th class=\"borderLB\" align=center>Min.</th>\n")
            out.write("<th class=\"borderLB\" align=center>Hr.</th>\n")
            out.write("<th class=\"borderLB\" align=center>Tot.</th>")

    def emit_summary_table_rows(self, out, snapshot, method):
        out.write("<tr>")
        to_print = "<td><b>{}</b></td>"
        out.write(to_print.format(method))
        out.write("<td></td>")
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.countLastMinute))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.countLastHour))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.countTotal))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.avgLatencyLastMinute))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.avgLatencyLastHour))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.avgLatencyTotal))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.rpcRateLastMinute))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.rpcRateLastHour))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.rpcRateTotal))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.inputRateLastMinute))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.inputRateLastHour))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.inputRateTotal))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.outputRateLastMinute))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.outputRateLastHour))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.outputRateTotal))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.errorsLastMinute))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.errorsLastHour))
        to_print = "<td class=\"borderLC\">{}</td>"
        out.write(to_print.format(snapshot.errorsTotal))
        out.write("</tr>")

    def get_stats_snapshots(self, is_received):
        stats_map = dict() # Sorted by method name.
        if is_received:
            self.get_snapshots(stats_map, self.SERVER_RPC_CUMULATIVE_VIEWS)
            self.get_snapshots(stats_map, self.SERVER_RPC_MINUTE_VIEWS)
            self.get_snapshots(stats_map, self.SERVER_RPC_HOUR_VIEWS)
        else:
            self.get_snapshots(stats_map, self.CLIENT_RPC_CUMULATIVE_VIEWS)
            self.get_snapshots(stats_map, self.CLIENT_RPC_MINUTE_VIEWS)
            self.get_snapshots(stats_map, self.CLIENT_RPC_HOUR_VIEWS)
        return stats_map

    def get_snapshots(self, data_map, views):
        for view in views:
            view_data = self.manager.get_view(view.name)
            if view_data is None:
                continue
            for entry in view_data.tag_value_aggregation_data_map().entrySet:
                #confused about what type of object tag_value_aggregation_data_map returns
                tag_values = entry #
                if len(tag_values) == 1:
                    tag_value = tag_values[0]
                else:
                    tag_value = tag_values[1]
                method = "" if tag_value is None else tag_value
                snapshot = StatSnapshot(data_map.get(method))
                if snapshot is None:
                    snapshot = StatSnapshot()
                    data_map.put(method, snapshot)
                self.get_stats(snapshot, entry.get_value(), view, view_data.get_window_data())

    # Gets RPC stats by its view definition, and set it to stats snapshot.
    def get_stats(self, snapshot, data, view, window_data):
        if view == RPC_CLIENT_ROUNDTRIP_LATENCY_VIEW or view == RPC_SERVER_SERVER_LATENCY_VIEW:
            snapshot.avg_latency_total = data.mean_data()
        elif view == RPC_CLIENT_ROUNDTRIP_LATENCY_MINUTE_VIEW \
            or view == RPC_SERVER_SERVER_LATENCY_MINUTE_VIEW:
            snapshot.avg_latency_minute = data.mean_data()
        elif view == RPC_CLIENT_ROUNDTRIP_LATENCY_HOUR_VIEW \
            or view == RPC_SERVER_SERVER_LATENCY_HOUR_VIEW:
            snapshot.avgLatencyLastHour = data.mean_data()
        elif view == RPC_CLIENT_ERROR_COUNT_VIEW or view == RPC_SERVER_ERROR_COUNT_VIEW:
            snapshot.errors_total = data.count_data()
        elif view == RPC_CLIENT_ERROR_COUNT_MINUTE_VIEW \
            or view == RPC_SERVER_ERROR_COUNT_MINUTE_VIEW:
            snapshot.errors_minute = data.count_data()
        elif view == RPC_CLIENT_ERROR_COUNT_HOUR_VIEW or view == RPC_SERVER_ERROR_COUNT_HOUR_VIEW:
            snapshot.errors_hour = data.count_data()
        elif view == RPC_CLIENT_REQUEST_BYTES_VIEW or view == RPC_SERVER_REQUEST_BYTES_VIEW:
            snapshot.input_rate_total = data.count_data() \
                                        * data.mean_data() \
                                        / self.BYTES_PER_KB \
                                        / self.get_duration_in_secs(window_data)
        elif view == RPC_CLIENT_REQUEST_BYTES_MINUTE_VIEW \
            or view == RPC_SERVER_REQUEST_BYTES_MINUTE_VIEW:
            snapshot.input_rate_minute = data.mean_data() * data.count_data() \
                / self.BYTES_PER_KB / self.SECONDS_PER_MINUTE
        elif view == RPC_CLIENT_REQUEST_BYTES_HOUR_VIEW \
            or view == RPC_SERVER_REQUEST_BYTES_HOUR_VIEW:
            snapshot.input_rate_hour = data.mean_data() * data.count_data() \
                / self.BYTES_PER_KB / self.SECONDS_PER_HOUR
        elif view == RPC_CLIENT_RESPONSE_BYTES_VIEW \
            or view == RPC_SERVER_RESPONSE_BYTES_VIEW:
            snapshot.output_rate_total = data.count_data() \
                    * data.mean_data() \
                    / self.BYTES_PER_KB \
                    / self.get_duration_in_secs(window_data)
        elif view == RPC_CLIENT_RESPONSE_BYTES_MINUTE_VIEW \
            or view == RPC_SERVER_RESPONSE_BYTES_MINUTE_VIEW:
            snapshot.output_rateminute = data.mean_data() * data.count_data() \
                / self.BYTES_PER_KB / self.SECONDS_PER_MINUTE
        elif view == RPC_CLIENT_RESPONSE_BYTES_HOUR_VIEW \
            or view == RPC_SERVER_RESPONSE_BYTES_HOUR_VIEW:
            snapshot.output_rate_hour = data.mean_data() * data.count_data() \
                / self.BYTES_PER_KB / self.SECONDS_PER_HOUR
        elif view == RPC_CLIENT_STARTED_COUNT_MINUTE_VIEW \
            or view == RPC_SERVER_STARTED_COUNT_MINUTE_VIEW:
            snapshot.count_minute = data.count_data()
            snapshot.rpc_rate_minute = snapshot.count_minute / self.SECONDS_PER_MINUTE
        elif view == RPC_CLIENT_STARTED_COUNT_HOUR_VIEW \
            or view == RPC_SERVER_STARTED_COUNT_HOUR_VIEW:
            snapshot.count_hour = data.count_data()
            snapshot.rpc_rate_hour = snapshot.count_hour / self.SECONDS_PER_HOUR
        elif view == RPC_CLIENT_STARTED_COUNT_CUMULATIVE_VIEW \
            or view == RPC_SERVER_STARTED_COUNT_CUMULATIVE_VIEW:
            snapshot.count_total = data.count_data()
            snapshot.rpc_rate_total = snapshot.count_total \
                / self.get_duration_in_secs(window_data)

    # Calculates the duration of the given CumulativeData in seconds.
    def get_duration_in_secs(self, cumulative_data):
        d1 = datetime.strptime(cumulative_data.end_time, "%Y-%m-%d %H:%M:%S.%f")
        d2 = datetime.strptime(cumulative_data.start_time, "%Y-%m-%d %H:%M:%S.%f")
        self.to_double_seconds(d1-d2)

    def to_double_seconds(self, cumulative_data):
        time.mktime(cumulative_data.timetuple())

    def create(self, manager):
        return self.__init__(manager)

    def __init__(self, manager):
        self.manager = manager
        ZPageHandler.register(RpczZPageHandler)


class StatSnapshot(NamedTuple):
    """
    stores and represents the essential rpc data needed for a row displayed on the rpc zpage
    """
    method: str
    received: bool
    count_minute: int
    count_hour: int
    count_total: int
    avg_latency_minute: datetime.datetime
    avg_latency_hour: datetime.datetime
    avg_latency_total: datetime.datetime
    rpc_rate_minute: float
    rpc_rate_hour: float
    rpc_rate_total: float
    input_rate_minute: float
    input_rate_hour: float
    input_rate_total: float
    output_rate_minute: float
    output_rate_hour: float
    output_rate_total: float
    errors_minute: int
    errors_hour: int
    errors_total: int


# class stat_group(NamedTuple):
#     """
#     stores and represents the row data (stat_snapshot) as
# well as which table this would fall under
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
#     :param statgroups: list of stat groups (received and sent) that
# together make up a page of stat data
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
