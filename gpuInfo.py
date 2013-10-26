#!/usr/bin/python

from ctypes import *
from gpuzstruct import gpuzMemory
import msvcrt, os

#Based off of a Shared Memory Example written by Srijit Kumar Bhadra
#   http://coding.derkeiler.com/Archive/Python/comp.lang.python/2005-03/3007.html
#Reference implementation: 
#   http://bluesplat-tech.blogspot.com/2009/09/gpu-z-reader-cause-i-can.html
#   C-sharp. Quite helpful, though I never actually built the source/installed VS

mappedFileName = c_char_p("GPUZShMem")
FILE_MAP_READ = 0x04

class datum():
    def __init__(self, name, value, unit=None, digits=None):
        self.name = name
        self.value = value
        self.unit = unit
        self.digits = digits
    def __repr__(self):
        return "DATUM " + str(self.name) + ":" + str(self.value)
    def __str__(self):
        return "DATUM " + str(self.name) + ":" + str(self.value)

class gpuInfo():
    def __init__(self):
        self.refresh()

    def refresh(self):
        self.data, self.sensors = {}, {}
        hMapObject = windll.kernel32.OpenFileMappingA(FILE_MAP_READ, 0, mappedFileName)
        if (hMapObject == 0):
            self._error_()

        mapPointer = windll.kernel32.MapViewOfFile(hMapObject, FILE_MAP_READ, 0, 0, sizeof(gpuzMemory))

        if (mapPointer == 0):
            self._error_()

        else:
            gpuz = cast(mapPointer, POINTER(gpuzMemory)).contents

        for rec in gpuz.sensors:
            if rec.name != u'':
                self.sensors[rec.name] = datum(rec.name, rec.value, \
                                                rec.unit, rec.digits)

        for rec in gpuz.data:
            if rec.key != u'':
                self.data[rec.key] = datum(rec.key, rec.value)

        windll.kernel32.UnmapViewOfFile(mapPointer)
        windll.kernel32.CloseHandle(hMapObject)

    def _error_(self):
        print "\nPlease make sure GPU-Z is running.\n"
        raise WinError()
