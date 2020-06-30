#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vxi11
#import matplotlib.pyplot as plt
import time
import subprocess
import sys
import struct
import os

instr = vxi11.Instrument( "172.28.126.231" )
instr.timeout = 60*1000
print( instr.ask( "*IDN?" ) )
print( instr.ask( "Time?" ) )
print( instr.ask( "WFMOutpre?" ) )

settingFileName = sys.argv[1] + "_setting.txt"
sfile = open( settingFileName, "w" )


# oscilloscope setting
instr.write( "data:source ch1" )
instr.write( "WFMOutpre:BYT_Nr 1" )
instr.write( "wfmoutpre:xunit s" )
instr.write( "wfmoutpre:yunit V" )


# horizontal axis setting check
xIncr = instr.ask( "wfmoutpre:xincr?" )
print "xIncr : ", xIncr
sfile.write( str(xIncr) + "\n" )



xLength = instr.ask( "HORizontal:ACQLENGTH?" )
instr.write( "data:stop " + str(xLength) )
print( "xLength : ", xLength )
print( instr.ask( "data:start?" ) )
print( instr.ask( "data:stop?" ) )
sfile.write( str(xLength) + "\n" )



# vertical axis setting check
yMult = []
yOff  = []
for ch in range( 1, 3):
    instr.write( "data:source ch" + str(ch) )
    yMult.append( instr.ask( "wfmoutpre:ymult?" ) )
    yOff.append( instr.ask( "wfmoutpre:yOff?" ) )
print "yMult : ", yMult
print "yOff: ", yOff
sfile.write( str(yMult[0]) + "\t" + str(yMult[1]) + "\n" )
sfile.write( str(yOff[0])  + "\t" + str(yOff[1])  + "\n" )


# save setting detail
instr.write( "header on" )
for ch in range( 1, 3):
    instr.write( "data:source ch" + str(ch) )
    print( instr.ask( "WFMOUTPRE:WFID?" ) )
    sfile.write( instr.ask( "WFMOUTPRE:WFID?" ) + "\n" )



instr.write( "data:source ch1" )
print( instr.ask( "Data?" )  )
sfile.write( instr.ask( "Data?" ) + "\n" )
print( instr.ask( "wfmoutpre?" ) )
sfile.write( instr.ask( "wfmoutpre?" ) + "\n" )
print( instr.ask( "horizontal?" ) )
sfile.write( instr.ask( "horizontal?" ) + "\n" )
print( instr.ask( "ch1?" ) )
sfile.write( instr.ask( "ch1?" ) + "\n" )
print( instr.ask( "ch2?" ) )
sfile.write( instr.ask( "ch2?" ) + "\n" )
print( instr.ask( "wfmoutpre:yoff?" ) )
instr.write( "header off" )

sfile.close()



# loop start
instr.write( "ACQuire:STOPAfter Sequence" )


plotObj = 0
for i in range( int(sys.argv[2]) ):
    #instr.write( "acquire:state RUN" )

    print i
    while not instr.ask( "acquire:state?" ) == '0':
        print "*",
        time.sleep(0.01)

    instr.write( "curve?" )
    d = instr.read_raw()

    ofileName = sys.argv[1] + "_" + str(i).zfill(5) + ".dat"
    ofile = open( ofileName, "wb" )
    ofile.write( d )
    ofile.close()

    instr.write( "acquire:state RUN" )


instr.write( "ACQuire:STOPAfter RUNStop" )
instr.write( "acquire:state RUN" )
