'''
This file registers/creates the RPC views and creates the html page
'''
class RPCHandler:

    RPCZ_URL = "/rpcz"
    SENT = "Sent"
    RECEIVED = "Received"
    SECONDS_PER_MINUTE = 60.0
    SECONDS_PER_HOUR = 3600.0
    NANOS_PER_SECOND = 1e9
    BYTES_PER_KB = 1024
    #private final ViewManager viewManager TODO add this variable
    RPC_STATS_TYPES = ["Count",
          "Avg latency (ms)",
          "Rate (rpc/s)",
          "Input (kb/s)",
          "Output (kb/s)",
          "Errors"]
    CLIENT_RPC_CUMULATIVE_VIEWS = [RPC_CLIENT_ERROR_COUNT_VIEW,
          RPC_CLIENT_ROUNDTRIP_LATENCY_VIEW,
          RPC_CLIENT_REQUEST_BYTES_VIEW,
          RPC_CLIENT_RESPONSE_BYTES_VIEW,
          RPC_CLIENT_STARTED_COUNT_CUMULATIVE_VIEW,
          // The last 5 views are not used yet.
          RPC_CLIENT_REQUEST_COUNT_VIEW,
          RPC_CLIENT_RESPONSE_COUNT_VIEW,
          RPC_CLIENT_UNCOMPRESSED_REQUEST_BYTES_VIEW,
          RPC_CLIENT_UNCOMPRESSED_RESPONSE_BYTES_VIEW,
          RPC_CLIENT_FINISHED_COUNT_CUMULATIVE_VIEW]

    SERVER_RPC_CUMULATIVE_VIEWS = [RPC_SERVER_ERROR_COUNT_VIEW,
          RPC_SERVER_SERVER_LATENCY_VIEW,
          RPC_SERVER_REQUEST_BYTES_VIEW,
          RPC_SERVER_RESPONSE_BYTES_VIEW,
          RPC_SERVER_STARTED_COUNT_CUMULATIVE_VIEW,
          // The last 5 views are not used yet.
          RPC_SERVER_REQUEST_COUNT_VIEW,
          RPC_SERVER_RESPONSE_COUNT_VIEW,
          RPC_SERVER_UNCOMPRESSED_REQUEST_BYTES_VIEW,
          RPC_SERVER_UNCOMPRESSED_RESPONSE_BYTES_VIEW,
          RPC_SERVER_FINISHED_COUNT_CUMULATIVE_VIEW]

    CLIENT_RPC_MINUTE_VIEWS = [RPC_CLIENT_ERROR_COUNT_MINUTE_VIEW,
          RPC_CLIENT_ROUNDTRIP_LATENCY_MINUTE_VIEW,
          RPC_CLIENT_REQUEST_BYTES_MINUTE_VIEW,
          RPC_CLIENT_RESPONSE_BYTES_MINUTE_VIEW,
          RPC_CLIENT_STARTED_COUNT_MINUTE_VIEW,
          // The last 5 views are not used yet.
          RPC_CLIENT_REQUEST_COUNT_MINUTE_VIEW,
          RPC_CLIENT_RESPONSE_COUNT_MINUTE_VIEW,
          RPC_CLIENT_UNCOMPRESSED_REQUEST_BYTES_MINUTE_VIEW,
          RPC_CLIENT_UNCOMPRESSED_RESPONSE_BYTES_MINUTE_VIEW,
          RPC_CLIENT_FINISHED_COUNT_MINUTE_VIEW]

    SERVER_RPC_MINUTE_VIEWS = [RPC_SERVER_ERROR_COUNT_MINUTE_VIEW,
          RPC_SERVER_SERVER_LATENCY_MINUTE_VIEW,
          RPC_SERVER_REQUEST_BYTES_MINUTE_VIEW,
          RPC_SERVER_RESPONSE_BYTES_MINUTE_VIEW,
          RPC_SERVER_STARTED_COUNT_MINUTE_VIEW,
          // The last 5 views are not used yet.
          RPC_SERVER_REQUEST_COUNT_MINUTE_VIEW,
          RPC_SERVER_RESPONSE_COUNT_MINUTE_VIEW,
          RPC_SERVER_UNCOMPRESSED_REQUEST_BYTES_MINUTE_VIEW,
          RPC_SERVER_UNCOMPRESSED_RESPONSE_BYTES_MINUTE_VIEW,
          RPC_SERVER_FINISHED_COUNT_MINUTE_VIEW]

    CLIENT_RPC_HOUR_VIEWS = [RPC_CLIENT_ERROR_COUNT_HOUR_VIEW,
          RPC_CLIENT_ROUNDTRIP_LATENCY_HOUR_VIEW,
          RPC_CLIENT_REQUEST_BYTES_HOUR_VIEW,
          RPC_CLIENT_RESPONSE_BYTES_HOUR_VIEW,
          RPC_CLIENT_STARTED_COUNT_HOUR_VIEW,
          // The last 5 views are not used yet.
          RPC_CLIENT_REQUEST_COUNT_HOUR_VIEW,
          RPC_CLIENT_RESPONSE_COUNT_HOUR_VIEW,
          RPC_CLIENT_UNCOMPRESSED_REQUEST_BYTES_HOUR_VIEW,
          RPC_CLIENT_UNCOMPRESSED_RESPONSE_BYTES_HOUR_VIEW,
          RPC_CLIENT_FINISHED_COUNT_HOUR_VIEW]

    SERVER_RPC_HOUR_VIEWS = [RPC_SERVER_ERROR_COUNT_HOUR_VIEW,
          RPC_SERVER_SERVER_LATENCY_HOUR_VIEW,
          RPC_SERVER_SERVER_ELAPSED_TIME_HOUR_VIEW,
          RPC_SERVER_REQUEST_BYTES_HOUR_VIEW,
          RPC_SERVER_RESPONSE_BYTES_HOUR_VIEW,
          RPC_SERVER_STARTED_COUNT_HOUR_VIEW,
          // The last 5 views are not used yet.
          RPC_SERVER_REQUEST_COUNT_HOUR_VIEW,
          RPC_SERVER_RESPONSE_COUNT_HOUR_VIEW,
          RPC_SERVER_UNCOMPRESSED_REQUEST_BYTES_HOUR_VIEW,
          RPC_SERVER_UNCOMPRESSED_RESPONSE_BYTES_HOUR_VIEW,
          RPC_SERVER_FINISHED_COUNT_HOUR_VIEW]

    def getUrlPath():
        return RPCZ_URL
    
    def emitStyle(PrintWriter out):
        out.write("<style>\n")
        out.write(Style.style)
        out.write("</style>\n")
    
    def emitHtml(Map<String, String> queryMap, OutputStream outputStream):
        return "to be done"
    
    def emitHtmlBody(PrintWriter out):
        return "to be done"

    def emitSummaryTable(PrintWriter out, Formatter formatter, boolean isReceived):
        return "to be done"

    def emitSummaryTableHeader(PrintWriter out, Formatter formatter):
        return "to be done"

    def emitSummaryTableRows(PrintWriter out, Formatter formatter, StatsSnapshot snapshot, String method):
        return "to be done"
    
    def getStatsSnapshots(boolean isReceived):
        return "to be done"

    def getStatsSnapshots(Map<String, StatsSnapshot> map, List<View> views):
        return "to be done"
    
    def getStats(StatsSnapshot snapshot, AggregationData data, View view, ViewData.AggregationWindowData windowData):
        return "to be done"

    def getDurationInSecs(ViewData.AggregationWindowData.CumulativeData cumulativeData):
        return "to be done"
    
    def toDoubleSeconds(Duration duration):
        return "to be done"

    def RpczZPageHandler create(ViewManager viewManager)
        return new RpczZPageHandler(viewManager)

    def RpczZPageHandler(ViewManager viewManager):
        this.viewManager = viewManager
        
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
import io.opencensus.stats.ViewManager