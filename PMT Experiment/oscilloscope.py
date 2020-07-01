#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Modified by taka (2010/04/20)


import re
import sys
import urllib





class Oscilloscope( object ):
    """
    Python module for Tektronix oscilloscope TDS3000B
    """





    def __init__( self, ip ):
        # Check the ip is correct or not.
        if re.match( "\d+\.\d+\.\d+\.\d+", ip ):
            self.IP = ip
        else:
            raise ValueError( str(ip) + ' is not correct IP address.\n Oscilloscope("1.1.1.1")' )


        #Constructed Mnemonics
        self.cursorPositionMnemonics = ( "POSITION1", "POSITION2" )
        self.measurementSpecifierMnemonics = ( "MEAS1", "MEAS2", "MEAS3", "MEAS4" )
        self.channelMnemonics = ( "CH1", "CH2", "CH3", "CH4" )
        self.referenceWaveformMnemonics = ( "REF1", "REF2", "REF3", "REF4" )
        self.mathMnemonics = ( "MATH", "MATH1" )
        self.waveformMnemonics = self.channelMnemonics + self.referenceWaveformMnemonics + self.mathMnemonics
        self.acquireModeMnemonics = ( "SAMPLE", "PEAKDETECT", "AVERAGE", "ENVELOPE" )


    # Argument Types
    def isNR1( self, value ):
        """
        If value is signed interger, it returns True. Otherwise it returns False.
        """
        value = str( value )
        return value.lstrip("-").isdigit()

    def isNR2( self, value ):
        """
        If value is floating point value without an exponent, it returns True. Otherwise it returns False.
        """
        value = str( vale )
        if self.isNR1( value ):
            return True
        value = value.lstrip("-").split(".")
        if not len( value )==2:
            return False
        for index in range(2):
            if not value[index].isdigit():
                return False
        return True


    def isNR3( self, value ):
        """
        If value is floating oint value with an exponent, it returns True. Otherwise it returns False.
        """
        value = str( value )
        if self.isNR1( value ):
            return True
        if self.isNR2( value ):
            return True
        
        # Divide the value to integer part and floating part
        value = value.lstrip("-").upper().split( "E", 1 )

        if not self.isNR2( value[0] ):
            return False
        if not self.isNR1( value[1] ):
            return False
        return True
        





    def sendQuery( self, query ):
        """
        This method sends query to oscilloscope.
        First argument "QUERY" should not to be url encoded.
        Return value is urlopen return value.
        """
        try:
            f = urllib.urlopen( "http://" + self.IP + "/?" + urllib.urlencode( query ) )
            return f
        except IOError:
            #self.sendQuery( query )
            print "http://" + self.IP + "/?" + urllib.urlencode( query )


    def sendCommand( self, command ):
        """
        This method send commands. The commands are defined by Tektronix programmer manual.
        First argument COMMAND should be string.
        """
        query = { "command": str( command ) }
        return self.sendQuery( query )



    def getImage( self, file ) :
        """
        Get oscilloscope display image file
        """
        url = "http://" + self.IP + "/Image.png"
        urllib.urlretrieve( url, file )




#ACQUISITION COMMANDS
    def getAcquireParameters( self ):
        """
        Get all the current acquisition parameters
        """
        return self.sendCommand( "ACQUIRE?" )



    def setAcquireMode( self, mode ):
        """
        Sets or queries the acquisition mode of the oscilloscope. This affects all live waveforms. This command is equivalent to setting Mode in the ACQUIRE menu.
        Waveforms are the displayed data point values taken from acquisition intervals. Each acquisition interval represents a time duration set by the horizontal scale (time per division). The oscilloscope sampling system always samples at the maximum rate, and so an acquisition interval may include more than one sample.
        The acquisition mode, which you set using this ACQuire:MODe command, determines how the final value of the acquisition interval is generated from the many data samples.
        """
        mode = str(mode).upper()
        if mode in acquireModeMnemonics:
            self.sendCommand( "ACQUIRE:MODE " + mode )
        else:
            print mode + " cannot be acquire mode."
            print acquireModeMnemonics,
            print " can be acquire mode."

    
    def getAcquireMode( self ):
        """
        Get acquire mode
        """
        return self.sendCommand( "ACQUIRE:MODE?" )


    def getAcquireNumacq( self ):
        """
        Indicates the number of acquisitions that have taken place since starting acquisition. This value is reset to zero when any Acquisition, Horizontal, or Vertical arguments that affect the waveform are modified. The maximum number of acquisitions that can be counted is 230–1. Counting stops when this number is reached. This is the same value that is displayed in the ACQUIRE menu.
        """
        return self.sendCommand( "ACQUIRE:NUMACQ?" )


    def setAcquireNumave( self, value ):
        """
        Sets the number of waveform acquisitions that make up an averaged waveform. This is equivalent to setting the Average count in the Acquisition Mode menu.
        """
        if not int(value) in ( 2,4,8,16,32,64,128,256,512 ):
            print str(value) + " cannot be the average number."
            print "Average number shoud be a powered of 2 and from 2 to 512."

        self.sendCommand( "ACQUIRE:NUMAVE " + str( int( value) ) )


    def getAcquireNumave( self ):
        """
        Sets the number of waveform acquisitions that make up an averaged waveform. This is equivalent to setting the Average count in the Acquisition Mode menu.
        """
        return self.sendCommand( "ACQUIRE:NUMAVE?" )


    def setAcquireNumenv( self, value ):
        """
        Sets the number of waveform acquisitions that make up an envelope waveform. This is equivalent to setting the Envelope count in the Acquisition Mode side menu.
        """
        if int( value ) in ( 2,4,8,16,32,64,128,256,512 ):
            self.sendCommand( "ACQUIRE:NUMENV " + str( int( value ) ) )
            return

        if str( value ).upper() in ( "0", "999999999", "INFINITE" ):
            self.sendCommand( "ACQUIRE:NUMENV 0" )
            return
            
        print str(value) + " cannot be the envelope number."
        print "Envelope number should be a powered of 2 and from 2 to 512, 0, 999999999, or INFINITE"

                          
    def getAcquireNumenv( self ):
        """
        Gets the number of waveform acquisitions that make up an envelope waveform. This is equivalent to setting the Envelope count in the Acquisition Mode side menu.
        """
        return self.sendCommand( "ACQUIRE:NUMENV?" )




    def setAcquireState( self, state ):
        """
        Sets or returns the acquisition state. This is the equivalent of pressing the front-panel RUN/STOP button. If ACQuire:STOPAfter is set to SEQuence, other signal events may also stop a waveform acquisition.
        """
        if str(state).upper() in ( "OFF", "STOP", "0" ):
            self.sendCommand( "ACQUIRE:STATE 0" )
            return
        
        if str(state).upper() in ( "ON", "RUN" ) or str(state).isdigit():
            self.sendCommand( "ACQUIRE:STATE 1" )
            return

        print str(state) + " cannot be the acquisition state. State should be integer, ON, RUN, OFF, or STOP"



    def getAcquireState( self ):
        """
        Get the current acquisition state.
        """
        return self.sendCommand( "ACQUIRE:STATE?" )



    def setAcquireStopAfter( self, stopafter ):
        """
        Tells the oscilloscope when to stop taking acquisitions.
        RUNSTop specifies that the run and stop state should be determined by the user pressing the front-panel RUN/STOP button.
        SEQuence specifies “single sequence” operation, where the oscilloscope stops after it has acquired enough waveforms to satisfy the conditions of the acquisi- tion mode. For example, if the acquisition mode is set to sample, and the horizontal scale is set to a speed that allows real-time operation, then the oscilloscope stops acquisition after digitizing a waveform from a single trigger event. However, if the acquisition mode is set to average 128 waveforms, then the oscilloscope stops acquiring data only after all 128 waveforms have been acquired. The ACQuire: STATE command and the front-panel RUN/STOP button will also stop acquisition when the oscilloscope is in single sequence mode.
        """
        if stopafter.upper() in ( "RUNSTOP", "SEQUENCE" ):
            self.sendCommand( "ACQURE:STOPAFTER " + stopafter )
        else:
            print str(stopafter) + " cannot be stop after mode."
            print "Stop after mode should be RUNSTOP or SEQUENCE"




#ALIAS COMMANDS
#CALIBRATION AND DIAGNOSTIC COMMANDS
#CURSOR COMMANDS
#DISPLAY COMMANDS
#ETHERNET COMMANDS
#FILE SYSTEM COMMANDS
#FRONT PANEL COMMANDS
#HARD COPY COMMANDS
#HORIZONTAL COMMANDS
#MATH COMMANDS
#MEASUREMENT COMMANDS
    def setImmediateMeasurementSourceFrom( self, source ):
        sourceTuple = self.channelMnemonics + self.referenceWaveformMnemonics
        if str(source).upper() in sourceTuple:
            self.sendCommand( "MEASUREMENT:IMMED:SOURCE1 " + source )
        else:
            print source + " cannot be measurement source."
            print sourceTuple,
            print " can be measurement source."


    def setImmediateMeasurementType( self, type ):
        """
        Specifies the immediate measurement.
        """
        typeTuple = ( "AMPLITUDE", "AREA", "BURST", "CAREA", "CMEAN", "CRMS", "DELAY", "FALL", "FREQUENCY", "HIGH", "LOW", "MAXIMUM", "MEAN", "MINIMUM", "NDUTY", "NOVERSHOOT", "NWIDTH", "PDUTY", "PERIOD", "PHASE", "PK2PK", "POVERSHOOT", "PWIDTH", "RISE", "RMS" )
        if str(type).upper() in typeTuple:
            self.sendCommand( "MEASUREMENT:IMMED:TYPE " + type )
        else:
            print str(type) + " cannot be measurement type."
            print typeTuple,
            print " can be measurement type."


    def getImmediateMeasurementType( self ):
        """
        Return immediate measurement type.
        """
        return self.sendCommand( "MEASUREMENT:IMMED:TYPE?" )


    def getImmediateMeasurementValue( self ):
        """
        Immediately executes the immediate measurement specified by the MEASUrement:IMMed:TYPe command. The measurement is taken on the source specified by a MEASUrement:IMMed:SOURCE command.
        """
        return self.sendCommand( "MEASUREMENT:IMMED:VALUE?" )



#MISCELLANEOUS COMMANDS
#RS-232 COMMANDS
#SAVE AND RECALL COMMANDS
    """
    Save and Recall commands allow you to store and retrieve internal waveforms and settings. When you “save a setup,” you save the settings of the oscilloscope. When you then “recall a setup,” the oscilloscope restores itself to the state it was in when you originally saved that setting. 
    """
    def recallSetup( self, setup ):
        """
        Restores a stored or factory front-panel setup of the oscilloscope. This command is equivalent to selecting Recall Saved Setup or Recall Factory Setup in the SAVE/RECALL menu.
        SYNTAX : RECAll:SETUp { FACtory | <NR1> | <file path> }
        ARGUMENTS : FACtory selects the factory setup. Initializes instrument settings to factory defaults, excluding: GPIB, hard copy, RS232 parameters, file instrument setting parameters, calibration notification time, battery off time, backlight time-outs, and user’s language.
        <NR1> is a value in the range from 1 to 10 and specifies a setup storage location. 
        <file path> is the name of the file where the setup will be recalled from.
        <file path> is a quoted string that defines the file name and path. Input the file path using the form <drive>/<dir>/<filename>. <drive> and one or more <dir>s are optional. If you do not specify them, the oscilloscope will read the file from the current directory. <filename> stands for a filename of up to 8 characters followed by a period (“.”) and any 3-character extension. Do not use wild card characters.
        The current directory refers to the name of a directory as returned by the FILESystem:CWD command.
        """
        self.sendCommand( "RECALL:SETUP " + str(setup) )


    def setSaveWaveformFileFormat( self, format ):
        """
        Sets or queries the file format for saved waveforms. Only internal format files can be recalled into the oscilloscope.
        File format must be INTERNAL, SPREADSHEET and MATHCAD.
        """
        formatTuple = ( "INTERNAL", "SPREADSHEET", "MATHCAD" )
        if str(format).upper() in formatTuple:
            self.sendCommand( "SAVE:WAVEFORM:FILEFORMAT " + format )
        else:
            print str(format) + " is not file format."
            print "File format must be in " + str(formatTuple)


    def getSaveWaveformFileFormat( self ):
        """
        Gets the file format for saved waveforms.
        """
        return self.sendCommand( "SAVE:WAVEFORM:FILEFORMAT?" )




#STATUS AND ERROR COMMANDS
#TRIGGER COMMANDS
#VERTICAL COMMANDS
    def setOffsetOfChannel( self, channel, offset ):
        """
        Sets or queries the offset, typically in volts, that is subtracted from the specified input channel before it is acquired. The greater the offset, the lower on the display the waveform appears. This is equivalent to setting Offset in the Vertical menu.
        """
        if str(channel).upper() in self.channelMnemonics:
            self.sendCommand( channel + ":OFFSET " + str(float(offset)) )
        else:
            print str(channel) + " is not channel"
            print "Channel must be in " + str(self.channelMnemonics)


    def getOffsetOfChannel( self, channel ):
        """
        Gets the offset value, typically in volts.
        """
        if str(channel).upper() in self.channelMnemonics:
            return self.sendCommand( channel + ":OFFSET?" )
        else:
            print str(channel) + " is not channel."
            print "Channel must be in " + str(self.channelMnemonics)


    def selectWaveform( self, wfm, frag="ON" ):
        """
        Turns the specified waveform ON or OFF. Turning a waveform ON makes it the selected waveform. 
        OFF or 0 turns off the display of the specified waveform. ON or 1 turns on the display of the specified waveform. The waveform also becomes the selected waveform.
        """
        #wfmTuple = self.channelMnemonics + self.mathTuple + self.referenceWaveformMnemonics
        #if str(wfm).upper() in wfmTuple:
        if str(wfm).upper() in self.waveformMnemonics:
            if str(frag).upper()=="ON" or str(frag)=="1":
                self.sendCommand( "SELECT:" + str(wfm) + " " + str(frag) )
            elif str(frag).upper()=="OFF" or str(frag)=="0":
                self.sendCommand( "SELECT:" + str(wfm) + " " + str(frag) )
        else:
            print str(wfm) + " is not wave form."
            #print "Wave form must be in " + str(wfmTuple)
            print "Wave form must be in " + str(self.waveformMnemonics)
            

    def isSelectWaveform( self, wfm ):
        """
        Returns 1 or 0 indicating that the specified waveform is being desplayed.
        """
        wfmTuple = self.channelMnemonics + self.mathTuple + self.referenceWaveformMnemonics
        if str(wfm).upper() in wfmTuple:
            return self.sendCommand( "SELECT:" + str(wfm) + "?" )
        else:
            print str(wfm) + " is not wave form."
            print "Wave form must be in " + str(wfmTuple)
            




#WAVEFORM COMMANDS






#My methods
    def getImmediateMeasurementValueOfTypeFromSource( self, type, source ):
        """
        Immediately executes the immediate measurement specifiied by the two arguments.
        """
        self.setImmediateMeasurementSourceFrom( source )
        self.setImmediateMeasurementType( type )
        return self.getImmediateMeasurementValue()


    def getWaveform( self, filename ):
        """
        Gets waveform data and save to filename
        """
        urllib.urlretrieve( "http://" + self.IP + "/?" + urllib.urlencode( { "wfmsend": "GET" } ), str(filename) )


    
    def getWaveformFromWfmWithFormat( self, wfm, format, filename ):
        """
        Gets waveform data and save to filename.
        Waveform is specified by wfm, and file format must be specified.
        """
        self.selectWaveform( str(wfm) )
        self.setSaveWaveformFileFormat( str(format) )
        self.getWaveform( str(filename) )




if __name__ == "__main__":
    print "This is oscilloscope module."
    oscillo = Oscilloscope( "202.13.215.109" )
    print "Oscilloscope IP is " + oscillo.IP

    import time
    oscillo.setAcquireStopAfter( "SEQUENCE" )
    
