import http.server
import random
import time
from prometheus_client import start_http_server
from prometheus_client import Gauge
from prometheus_client import Histogram

INPROGRESS = Gauge('hello_worlds_inprogress',
                   'Number of Hello Worlds in progress')
LAST = Gauge('hello_worlds_last_time_seconds',
             'The last time a Hello world as served')

LATENCY = Histogram('hello_world_latency_seconds',
                    'Time for a request Hello World')

class MyHandler(http.server.BaseHTTPRequestHandler):
  @LATENCY.time()
  def do_GET(self):
    INPROGRESS.inc()
    self.send_response(200)
    self.end_headers()
    self.wfile.write(b"Hello World")
    LAST.set(time.time())
    INPROGRESS.dec()

if __name__ == "__main__":
   start_http_server(8000)
   server = http.server.HTTPServer(('0.0.0.0', 8001), MyHandler)
   server.serve_forever()
