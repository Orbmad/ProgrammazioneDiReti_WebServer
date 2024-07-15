'''
Matricola: 0001080182
manuele.dambrosio@studio.unibo.it

Traccia 2: Web Server Semplice
'''

#!/bin/env python
import sys, signal
import http.server as hs
import socketserver as ss

#If not entered from the command line the default port is 8080.
if sys.argv[1:]:
  PORT = int(sys.argv[1])
else:
  PORT = 8080
HOST = 'localhost'
server_address = (HOST, PORT)

#ThreadingTCPServer can handle more than one request.
handler = hs.SimpleHTTPRequestHandler
server = ss.ThreadingTCPServer(server_address, handler)

#All threads are safely termineted on close.
server.daemon_threads = True
#Consent socket overwriting.
server.allow_reuse_address = True

#Stops execution when (CTRL + C) is pressed.
def exit_signal_handler(signal, frame):
    print( 'Exiting http server...')
    try:
      if( server ):
        server.server_close()
    finally:
      sys.exit(0)
exit_signal = signal.SIGINT
signal.signal(exit_signal, exit_signal_handler)

try:
  while True:
    print(f"Server http://{HOST}:{PORT} ready...")
    server.serve_forever()
except KeyboardInterrupt:
  pass

server.server_close