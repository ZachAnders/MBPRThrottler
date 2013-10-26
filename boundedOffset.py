#!/usr/bin/python

class boundedOffset():
	def __init__(self, base, maxIncr, startMax=True):
		self.base = base
		self.maxIncr = maxIncr

		if startMax:
			self.incr = maxIncr
		else:
			self.incr = 0

	def decrement(self):
		self.incr -= 1
		if self.incr < 0:
			self.incr = 0
	
	def increment(self):
		self.incr += 1
		if self.incr > self.maxIncr:
			self.incr = self.maxIncr
	
	def calculate(self):
		return self.base[0] + self.base[1] * self.incr
