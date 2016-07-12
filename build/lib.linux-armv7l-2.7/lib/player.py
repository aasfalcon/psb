import jack
import numpy as np
from time import sleep
from soundfile import SoundFile
from scikits.samplerate import resample

import pyximport
pyximport.install()
from pyx.process import PlayerBase

class Player(PlayerBase):
	stopping = False
	filename = ''
	
	
	def __init__(self, client_name = 'psb'):
		super(Player, self).__init__()
		self.client = jack.Client(client_name)
		
		for channel in range(self.channels): 
			self.client.outports.register('out_{0}'.format(channel))

		self.client.set_process_callback(self.process)
		self.client.activate()
		self.output = np.zeros(self.client.blocksize, np.float32)
				
		
	def connect(self, inputs):
		for channel in range(self.channels): 
			self.client.connect( \
				'{0}:out_{1}'.format(self.client.name, channel), \
				inputs[channel])
		
		
	def read_sample(self, filename, max = 60 * 44100):
		wav = SoundFile(filename)
		data = wav.read(max, dtype = np.float32)
				
		# fix rate
		jack_rate = float(self.client.samplerate)
		file_rate = float(wav.samplerate)
		
		if (jack_rate != file_rate):
			data = resample(data, jack_rate / file_rate, 'sinc_best')
	
		silence = np.zeros((self.client.blocksize, wav.channels), np.float32)
		data = data.reshape(-1, wav.channels)
		data = np.append(data, silence, axis=0)
		return data
		
	
	def run(self):		
		while not self.stopping:
			if self.filename:
				self.data = self.read_sample(self.filename)
				self.filename = ''
				self.position = 0
			else:
				sleep(.01)
			
		self.client.deactivate()

		
	def join(self):
		self.stopping = True
		super(Player, self).join()
								
		    
	def play(self, filename):
		self.filename = filename
				
		
	def stop(self):
		self.data = None
				
