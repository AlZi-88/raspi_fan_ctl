from bsw_config import bsw_config

class fan:
	def __init__(self, fan_pin = 27):
		self.fan_pin = fan_pin
		self.bsw = bsw_config.BSW(self.fan_pin)
		self.status = 'Not Purgeing'
	def purge(self):
		self.bsw.set_channel(self.fan_pin)
		self.status = 'Purgeing'
	def stop_purgeing(self):
		self.bsw.reset_channel(self.fan_pin)
		self.status = 'Not Purgeing'
	def get_status(self):
		return self.status
	def __del__(self):
		del self.bsw
