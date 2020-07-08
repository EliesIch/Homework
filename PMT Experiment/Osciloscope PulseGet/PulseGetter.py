 #!/usr/bin/env python
# -*- coding: utf-8 -*-




"""
Usage

./pulseGetter dirname ipaddress cycle [channel, ]


"""




import oscilloscope
import time
import os
import sys


if not os.path.exists( sys.argv[1]):
    os.mkdir(sys.argv[1])

oscillo = oscilloscope.Oscilloscope( sys.argv[2] )    
cycle = int( sys.argv[3] )
channelList = sys.argv[4:len(sys.argv)]


for index in range(cycle):
    print str(index)

    oscillo.setAcquireStopAfter("sequence")
    oscillo.setAcquireState("run")

    while oscillo.getAcquireState().readline()=='1\n':
        pass
    
    for channel in channelList:
        oscillo.getWaveformFromWfmWithFormat( 'ch'+channel, 'internal', sys.argv[1] + '/' + str(index) + '_' + channel + '.isf')

