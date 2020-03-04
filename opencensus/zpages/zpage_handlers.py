
class ZPageHandlers:

#    Starts an {@code HttpServer} and registers all pages to it. When the JVM shuts down the server
#    is stopped.
   
#    <p>Users must call this function only once per process.

#    @param port the port used to bind the {@code HttpServer}.
#    @throws IllegalStateException if the server is already started.
#    @throws IOException if the server cannot bind to the requested address.
#    @since 0.6
    def start_http_server_and_register_all(self, port):
        print("start servers on" + port)