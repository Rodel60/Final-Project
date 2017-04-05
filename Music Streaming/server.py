import pyaudio
import wave
import sys
import time
from socket import *

if __name__ == "__main__":
	
	# Define data chunk size
	CHUNK = 1024

	# Set up the connection
	sock = socket(AF_INET, SOCK_STREAM)
	sock.connect(('10.20.21.43', 4200))

	# Set up the wav file
	wf = wave.open('all_i_do_is_win.wav', 'rb')

	# Read data from wav file
	data = wf.readframes(CHUNK)

	# Stream data
	while len(data) > 0:
		sock.send( data )
		data = wf.readframes(CHUNK)

	socket.close()