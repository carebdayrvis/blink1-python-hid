import hid
import time

class Blink:

	def __init__(self):
		self.h = hid.device()
		self.h.open(0x27b8, 0x01ed)

	def off(self):
		"""Turn blink(1) off.""" 
		action = ord('D')
		self.h.write([0x01, action, 0, 0, 0, 0, 0, 0])

	def on(self, red, green, blue):
		"""Turn blink(1) on and set to a given color.""" 
		action = ord('n')
		self.h.write([0x01, action, red, green, blue, 0, 0, 0])

	def fade(self, red, green, blue, fadeMillis, led):
		"""Fade blink(1) to a given color over fadeMillis milliseconds.""" 
		action = ord('c')
		fadeMillis = fadeMillis / 10
		th = (fadeMillis & 0xff00) >> 8
		tl = fadeMillis & 0x00ff
		self.h.write([0x01, action, red, green, blue, th, tl, led])
		
	def setLine(self, red, green, blue, fadeMillis, position):
		"""Set color line at position for fadeMillis duration."""
		action = ord('P')
		fadeMillis = fadeMillis / 10
		th = (fadeMillis & 0xff00) >> 8
		tl = fadeMillis & 0x00ff
		self.h.write([0x01, action, red, green, blue, th, tl, position])

	def saveLines(self):
		"""Save pattern to blink(1)"""
		self.h.write([0x01, 0x57, 0, 0, 0, 0, 0, 0])

	def playLines(self, position, count):
		"""Play pattern, ending at position."""
		self.h.write([0x01, 0x70, 1, 0, position, count, 0, 0])
		
