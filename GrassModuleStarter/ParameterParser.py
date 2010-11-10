################################################################################
# Author:	Soeren Gebbert
#               Parts of this code are from the great pyWPS from Jachym Cepicky:
#               http://pywps.wald.intevation.org/
#
# Copyright (C) 2009 Soeren Gebbert
#               mail to: soerengebbert <at> googlemail <dot> com
#
# License:
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

import os
import os.path
from ProcessLogging import *

class ComplexData():
    """This class saves the complex in- and output data
    of a wps execution request"""
    ############################################################################
    def __init__(self, fileobj=None):
        self.identifier = ""
        self.maxOccurs= ""
        self.pathToFile = ""
        self.mimeType = ""
        self.schema = ""
        self.encoding = ""
        if isinstance(fileobj, file):
            self.__file = fileobj
            self.__parseFile()

    ############################################################################
    def __parseFile(self):
        for i in range(6):
            string = self.__file.readline()
            if string == "":
                return
            splitstring = string.split('=')
            if len(splitstring) > 1:
                if splitstring[0].upper().find("IDENTIFIER") != -1:
                    self.identifier = splitstring[1].rstrip()
                    #print self.identifier
                if splitstring[0].upper().find("MAXOCCURS") != -1:
                    self.maxOccurs = splitstring[1].rstrip()
                    #print self.maxOccurs
                if splitstring[0].upper().find("PATHTOFILE") != -1:
                    self.pathToFile = splitstring[1].rstrip()
                    #print self.pathToFile
                if splitstring[0].upper().find("MIMETYPE") != -1:
                    self.mimeType = splitstring[1].rstrip()
                    #print self.mimeType
                if splitstring[0].upper().find("ENCODING") != -1:
                    self.encoding = splitstring[1].rstrip()
                    #print self.encoding
                if splitstring[0].upper().find("SCHEMA") != -1:
                    self.schema = splitstring[1].rstrip()
                    #print self.schema

###############################################################################
###############################################################################
###############################################################################
    
class ComplexOutput(ComplexData):
    """The same as ComplexData, but used for name convenience"""
    pass

###############################################################################
###############################################################################
###############################################################################

class LiteralData():
    """This class saves the literal in- and output data
    of a wps execution request"""
    ############################################################################
    def __init__(self, fileobj=None):
        self.identifier = ""
        self.value = ""
        self.type = "" #double, integer, boolean, string
        if isinstance(fileobj, file):
            self.__file = fileobj
            self.__parseFile()

    ############################################################################
    def __parseFile(self):
        for i in range(3):
            string = self.__file.readline()
            if string == "":
                return
            splitstring = string.split('=')
            if len(splitstring) > 1:
                if splitstring[0].upper().find("IDENTIFIER") != -1:
                    self.identifier = splitstring[1].rstrip()
                    #print self.identifier
                if splitstring[0].upper().find("VALUE") != -1:
                    self.value = splitstring[1].rstrip()
                    #print self.value
                if splitstring[0].upper().find("TYPE") != -1:
                    self.type = splitstring[1].rstrip()
                    #print self.type

###############################################################################
###############################################################################
###############################################################################

class InputParameter(ProcessLogging):
    """This class parses and stores the key-value input parameter of
    a wps execusion request"""
    ############################################################################
    def __init__(self, logfile):

        ProcessLogging.__init__(self, logfile)
        
        self.workDir = None
        self.grassGisBase = ""
        self.grassAddonPath = ""
        self.grassVersion = ""
        self.grassModule = ""
        self.complexDataList = []
        self.complexOutputList = []
        self.literalDataList = []
        self.location = ""
        self.linkInput = "TRUE"
        self.ignoreProjection = "FALSE"
        self.useXYLocation = "FALSE"
        self.__fileName = ""

    ############################################################################
    def parseFile(self, filename):
        """Parse the key-value pairs and call the appropriate subroutines and
        classes"""
        self.__filename = filename

        if os.path.isfile(filename) == False:
            self.LogError("Unable to open input file " + str(filename))
            raise IOError

        self.__file = open(filename, 'r')

        while True:
            string = self.__file.readline()
            if string == "":
                break

            if string.upper().find("[SYSTEM]") != -1:
                #print string.upper()
                self.__parseSystem()

            if string.upper().find("[GRASS]") != -1:
                #print string.upper()
                self.__parseGrass()

            if string.upper().find("[COMPLEXDATA]") != -1:
                #print string.upper()
                self.complexDataList.append(ComplexData(self.__file))

            if string.upper().find("[COMPLEXOUTPUT]") != -1:
                #print string.upper()
                self.complexOutputList.append(ComplexOutput(self.__file))

            if string.upper().find("[LITERALDATA]") != -1:
                #print string.upper()
                self.literalDataList.append(LiteralData(self.__file))

    ############################################################################
    def __parseSystem(self):
        """Parse and store the sytem relevant variables"""
        for i in range(2):
            string = self.__file.readline()
            if string == "":
                return
            splitstring = string.split('=')
            if len(splitstring) > 1:
                if splitstring[0].upper().find("WORKDIR") != -1:
                    self.workDir = splitstring[1].rstrip()
                    #print self.workDir
                if splitstring[0].upper().find("OUTPUTDIR") != -1:
                    self.outputDir = splitstring[1].rstrip()
                    #print self.outputDir


    ############################################################################
    def __parseGrass(self):
        """Parse and store the grass relevant variables"""
        for i in range(8):
            string = self.__file.readline()
            if string == "":
                return
            splitstring = string.split('=')
            if len(splitstring) > 1:
                if splitstring[0].upper().find("GISBASE") != -1:
                    self.grassGisBase = splitstring[1].rstrip()
                    #print self.grassGisBase
                if splitstring[0].upper().find("GRASS_ADDON_PATH") != -1:
                    self.grassAddonPath = splitstring[1].rstrip()
                    #print self.grassAddonPath
                if splitstring[0].upper().find("GRASS_VERSION") != -1:
                    self.grassVersion = splitstring[1].rstrip()
                    #print self.grassVersion
                if splitstring[0].upper().find("MODULE") != -1:
                    self.grassModule = splitstring[1].rstrip()
                    #print self.grassModule
                if splitstring[0].upper().find("LOCATION") != -1:
                    self.location = splitstring[1].rstrip()
                    #print self.location
                if splitstring[0].upper().find("LINKINPUT") != -1:
                    self.linkInput = splitstring[1].rstrip()
                    #print self.linkInput
                if splitstring[0].upper().find("IGNOREPROJECTION") != -1:
                    self.ignoreProjection = splitstring[1].rstrip()
                    #print self.ignoreProjection
                if splitstring[0].upper().find("USRXYLOCATION") != -1:
                    self.useXYLocation = splitstring[1].rstrip()
                    #print self.useXYLocation
