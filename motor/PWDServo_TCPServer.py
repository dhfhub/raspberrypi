#for python3
#sudo python3 -B PWDServo_TCPServer.py

import socketserver
import signal
import time
import socket
import PWDServo

#HOST = '127.0.0.1'
HOST = '192.168.0.10'
PORT = 11000

servo1 = PWDServo.PWDServo(18)
servo1.goHome()


class Handler(socketserver.StreamRequestHandler):
	def handle(self):
		global PORT #call global variable
		global servo1
		
		while True:
			#in python3, must send by byte
			data = self.request.recv(1024)
			strdata = data.decode('utf-8')
			
			#print("recieve="+data)
			if len(data) == 0:
				break
			
			cleandata= strdata.replace("\n","");
			cleandata = cleandata.replace("\r","");
			cleandata = cleandata.replace("\r\n","");
			if len(cleandata) != 0:
				if cleandata.find("M")!=-1:
					commands = cleandata.split("M")
					#print(commands)
					for command in commands:
						if(len(command)!=0):
							#command = commands.split(" ")
							print("move to "+command)
							servo1.moveTo(int(command))
				else:
					print("unknown command:"+cleandata)
				
			#print(strdata)
			
			#self.request.send(strdata.encode('utf-8'))
			
			##self.request.send(data)
		self.request.close()
		print("disconnect")

###main

server = socketserver.TCPServer(('', PORT), Handler)
print("listening : %s" % (server.socket.getsockname(),))

try:
	server.serve_forever()
except KeyboardInterrupt:
	print("catch interrupt")
finally:
	# clean up
	print("clean up")
	server.shutdown()
    


