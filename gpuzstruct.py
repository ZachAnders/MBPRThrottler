from ctypes import *

recordCount = 128 #Record Count

#Gpu info
class infoRecord(Structure):
	_pack_ = 1
	_fields_ = [("key", c_wchar*256), \
				("value", c_wchar*256)]

#Gpu Sensor stats
class sensorRecord(Structure):
	_pack_ = 1
	_fields_ = [("name", c_wchar*256), \
				("unit", c_wchar*8), \
				("digits", c_uint32), \
				("value", c_double)]
				
class gpuzMemory(Structure):
	_pack_ = 1
	_fields_ = [("version", c_uint32), \
				("busy", c_long), \
				("lastUpdate", c_uint32), \
				("data", infoRecord*128), \
				("sensors", sensorRecord*128)]