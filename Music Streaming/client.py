import pyaudio
import wave
import sys
import time
from socket import *

if __name__ == "__main__":
	
	# Set up connection
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.bind( ('129.161.51.126', 4200) )
	clientSocket.listen(1)

	# Set up audio streamer
	p = pyaudio.PyAudio()
	stream = p.open(format=8,
	                channels=2,
	                rate=44100,
	                output=True)

	# Start main loop
	while 1:
		# Make connection
		connectionSocket, addr = clientSocket.accept()
		print 'Connection Made'
		data = connectionSocket.recv(int(4096))

		# Get music data
		while len(data) > 0:
			stream.write(data)
			data = connectionSocket.recv(int(4096))

		# Close the connection
		connectionSocket.close()
		print 'Connection Closed'

	# Close the stream
	stream.stop_stream()
	stream.close()
	p.terminate()