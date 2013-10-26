#!/usr/bin/python
import sys, time, os
from gpuInfo import gpuInfo
from boundedOffset import boundedOffset
from timer import timer

_ = os.popen("GPU-Z.exe -minimized")
sys.stdout = open("ClockMonitor.log", "a", 0)
sys.stderr = sys.stdout

print "\n--Startup -- " + time.ctime()
time.sleep(10) #Pause after startup

def getClock(gpu):
	clStr = str(gpu.sensors["GPU Core Clock"].value)
	val = float(clStr.split(":")[-1])
	return val
def setClock(spd):
	nvInspCmd = "nvidiaInspector.exe -setBaseClockOffset:0,0,135 -setMemoryClockOffset:0,0,500 -setGpuClock:0,2,%s -setMemoryClock:0,2,2600 -forcepstate:0,1"
	_ = os.popen(nvInspCmd % (str(int(spd))))
	print "Clock speed changed to " + str(spd) + "MHz"

def lowerClock():
	print "Throttling detected. Decreasing clock speed..."
	clockSpeed.decrement()
	setClock(clockSpeed.calculate())	

#(Base, incrementSize)
clockSpeed = boundedOffset( (800, 25), 8)
setClock(clockSpeed.calculate())

gpu = gpuInfo()
old = getClock(gpu)

clockSpeed = boundedOffset( (800, 25), 8)
clockTimer = timer(lowerClock, 2, 30)
timer = time.time()

while True:
	time.sleep(0.25)
	gpu.refresh()
	new = getClock(gpu)

	#falling edge
	if new < old:
		clockTimer.tick()
		timer = time.time()
		old = new

	#Time since last falling edge
	if time.time() - timer > 60*15:
		timer = time.time()
		print "Throttling not detected over interval, increasing clock speed..."
		clockSpeed.increment()
		setClock(clockSpeed.calculate())	
