#!/usr/bin/python

import time

#Keeps a set of items up to binWidth items long, making sure the range
#stays between max and max-binCapacity
class timeBin():
	def __init__(self, binWidth, binCapacity):
		self.readings = []
		self.numReadings = binWidth
		self.readingRange = binCapacity

	def addPt(self, pt):
		self.readings.append(pt)
		rng = lambda x: max(x) - min(x)
		while len(self.readings) > self.numReadings or rng(self.readings) > self.readingRange:
			self.trim()

	def saturated(self):
		if len(self.readings) == self.numReadings:
			return True
		return False

	def trim(self):
		self.readings.remove(min(self.readings))
	
	def reset(self):
		self.readings = []

class timer():
	handler = lambda: None
	timeRange = None
	#Call handler if <numOccurrences> events happen within <timeSpan> second of eachother
	def __init__(self, handler, numOccurrences = 2, timeSpan = 10):
		self.handler = handler
		self.timeRange = timeBin(numOccurrences, timeSpan)

	def tick(self):
		self.timeRange.addPt(time.time())
		if self.timeRange.saturated():
			self.handler()
	
	def reset(self):
		self.timeRange.reset()
		

#a = timeBin(4, 10)
def myHandler():
	print "Alert"

test = timer(myHandler, 2, 5)
t = test.tick
