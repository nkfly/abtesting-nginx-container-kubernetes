#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import sys

PORT_NUMBER = int(sys.argv[1])
MESSAGE = sys.argv[2]

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		self.wfile.write(MESSAGE)
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)

	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:	
	server.socket.close()
