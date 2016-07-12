import numpy as np
from threading import Thread

class PlayerBase(Thread):
	level = .5
	client = None
	data = None
	output = None
	position = 0
	channels = 2
	
				
	def process(self, frames):
		if self.data is None:
			return
			
		(data_frames, data_channels) = self.data.shape

		if self.position >= data_frames:
			return
			
		pos = self.position
		new_pos = pos + frames
		length = frames if new_pos < data_frames else data_frames - pos			
		output = self.output

		for channel in range(self.channels):
			data_channel = channel
			
			if data_channel >= data_channels:
				if data_channels == 1:
					data_channel = 0
				else:
					break
					
			output[:length] = self.data[pos:new_pos, data_channel] * self.level
			self.client.outports[channel].get_buffer()[:] = output
			
		self.position = new_pos
