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
from ProcessLogging import ProcessLogging

class GrassEnvironment(ProcessLogging):
    """This class saves and sets grass environment variables"""

    ############################################################################
    def __init__(self, logfile):

        ProcessLogging.__init__(self, logfile)
        self.env = {"GISBASE":"", "GISRC":"", "LD_LIBRARY_PATH":"",\
        "GRASS_ADDON_PATH":"", "GRASS_VERSION":"", "PYTHONPATH":""}

    ############################################################################
    def getEnvVariables(self):
        for key in self.env:
            try:
                self.env[key] = os.getenv(key, self.env[key])
            except:
                self.LogError("Error setting grass environmental variables")
                raise

    ############################################################################
    def setEnvVariables(self):
        for key in self.env:
            try:
                value = self.env[key]
                origValue = os.getenv(key)
                if origValue:
                    value  += ":"+origValue
                os.putenv(key,value)
                os.environ[key] = value
                self.LogInfo(key + "=" + value)
            except:
                self.LogError("Error setting grass environmental variables")
                raise

###############################################################################
###############################################################################
###############################################################################

class GrassGisRC(ProcessLogging):
    """This class takes care of the correct creation of the gisrc file"""
    ############################################################################
    def __init__(self, logfile):

        ProcessLogging.__init__(self, logfile)
        self.locationName = GRASS_LOCATION_NAME
        self.mapset = GRASS_MAPSET_NAME
        self.gisdbase = ""
        self.__gisrcFile = ""

    ############################################################################
    def __init__(self, gisdbase, locationName, mapset, logfile):
        ProcessLogging.__init__(self, logfile)
        self.locationName = locationName
        self.mapset = mapset
        self.gisdbase = gisdbase
        self.__gisrcFile = ""
        self.__tmpDir = ""

    ############################################################################
    def rewriteFile(self):
        if self.__gisrcFile != "":
            self.__writeFile()
        else:
            self.LogError("Error re-writing the gisrc file")
            raise IOError

    ############################################################################
    def writeFile(self, tempdir):
        if os.path.isdir(tempdir):
            try:
               self.__gisrcFile = os.path.join(tempdir, "gisrc")
               self.__writeFile()
            except:
                self.LogError("Error writing the gisrc file")
                raise

    ############################################################################
    def printFile(self):
        try:
            gisrc = open(self.__gisrcFile, 'r')
            self.LogInfo(str(gisrc.read()))
            gisrc.close()
        except:
            self.LogError("Error printing the gisrc file")
            raise
        
    ############################################################################
    def __writeFile(self):
        try:
            gisrc = open(self.__gisrcFile, 'w')
            gisrc.write("LOCATION_NAME: %s\n" % self.locationName)
            gisrc.write("MAPSET: %s\n" % self.mapset)
            gisrc.write("DIGITIZER: none\n")
            gisrc.write("GISDBASE: %s\n" % self.gisdbase)
            gisrc.write("OVERWRITE: 1\n")
            gisrc.write("DEBUG: 0\n")
            gisrc.write("GRASS_GUI: text")
            gisrc.close()
            gisrc = open(self.__gisrcFile, 'r')
            self.LogInfo(gisrc.read())
            gisrc.close()
        except:
            self.LogError("Error writing the gisrc file")
            raise

    ############################################################################
    def getFileName(self):
        return self.__gisrcFile

###############################################################################
###############################################################################
###############################################################################

class GrassWindFile(ProcessLogging):
    """This class takes care of thr correct creation of grass WIND and
    DEFAULT_WIND files using a dummy region"""
    ############################################################################
    def __init__(self, gisdbase, location, mapset, logfile):

        ProcessLogging.__init__(self, logfile)
        """ Create the WIND and if needed the DEFAULT_WIND file """
        self.__windFile = ""
        self.__windname = "WIND"

        if mapset == "PERMANENT":
            #If PERMANENT is used as mapset, the DEFAULT_WIND file will be created too
            self.__windFile = os.path.join(gisdbase, location, mapset, "DEFAULT_WIND" )
            self.__write()

        self.__windFile = os.path.join(gisdbase, location, mapset, "WIND")
        self.__write()

    ############################################################################
    def __write(self):
        try:
            wind =open(self.__windFile,'w')
            wind.write("""proj:       0\n""")
            wind.write("""zone:       0\n""")
            wind.write("""north:      100\n""")
            wind.write("""south:      0\n""")
            wind.write("""east:       100\n""")
            wind.write("""west:       0\n""")
            wind.write("""cols:       100\n""")
            wind.write("""rows:       100\n""")
            wind.write("""e-w resol:  1\n""")
            wind.write("""n-s resol:  1\n""")
            wind.close()
        except:
            self.LogError("Error writing the WIND file")
            raise

    ############################################################################
    def getFileName(self):
        return self.__windFile

