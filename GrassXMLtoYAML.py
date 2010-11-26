# -*- coding: utf-8 -*-
################################################################################
# Author:	Soeren Gebbert
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

from optparse import OptionParser
import os.path
import wpsXML.GrassXMLtoDict as wps
import yaml

class GrassXMLtoYAML(wps.GrassXMLtoDict):
    """ Convert a Grass WPS XML file into PyPWS process file"""
    def __init__(self):
        wps.GrassXMLtoDict.__init__(self)

    def setPythonFileName(self,  filename):
        self.__pythonFileName = filename
        self.__pythonFile = open(self.__pythonFileName,  'w')

    def convert(self):
        """Start the conversion from WPS XML to ZOO-WPS yaml config file.
           Use nested dictionaries and arrays as data structure. """
        try:
            self._parseXML()
            yaml.dump(self._content, self._output, default_flow_style=False)
            modulename = str(self._content["ProcessDescription"]["Identifier"])
            funcname =  str(self._content["ProcessDescription"]["Identifier"]).replace(".", "_")
            self._writePythonFile(self, modulename, funcname)
        except:
            raise
        finally:
            self._closeOutput()

    def _writePythonFile(self, modulename, funcname):
        """Write the service python file for the ZOO Kernel"""
        self.__pythonFile.write("import ZOOGrassModuleStarter as zoo\n")
        self.__pythonFile.write("def " + str(funcname) + "(m, inputs, outputs):\n")
        self.__pythonFile.write("    service = zoo.ZOOGrassModuleStarter()\n")
        self.__pythonFile.write("    service.fromMaps(\"" + str(modulename)+ "\", inputs, outputs)\n")
        self.__pythonFile.write("    return 1\n")
        self.__pythonFile.close()

def main():
    """The main function which will be called if the script is executed directly"""

    usage = "usage: %prog [-help,--help] --xmlfile inputfile.xml --zcfgfile output.txt]"
    description = "Use %prog to convert Grass 7.0 WPS XML process description files into ZOO-WPS server YAML config files."
    parser = OptionParser(usage=usage, description=description)
    parser.add_option("-x", "--xmlfile", dest="xmlfile", help="The path to the grass WPS input xml file", metavar="FILE")
    parser.add_option("-y", "--yamlfile", dest="yamlfile", help="Path to the new created yaml file", metavar="FILE")
    parser.add_option("-p", "--pythonfile", dest="pythonfile", help="Path to the new created python file", metavar="FILE")

    (options, args) = parser.parse_args()

    if options.xmlfile == None or options.yamlfile == None or options.pythonfile == None:
        parser.print_help()
        parser.error("Booth file names must be provided")

    converter = GrassXMLtoYAML()
    converter.setXMLFileName(options.xmlfile)
    converter.setOutputFileName(options.yamlfile)
    converter.setPythonFileName(options.pythonfile)
    converter.convert()
    
    exit(0)

###############################################################################
if __name__ == "__main__":
    main()
