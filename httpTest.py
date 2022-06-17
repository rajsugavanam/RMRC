from http.server import BaseHTTPRequestHandler, HTTPServer 

class handler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		print(self.rfile.read())
		self.wfile.write("hello")

def main():
	httpserver = HTTPServer(("localhost", 20000), handler)
	httpserver.serve_forever()
main()
