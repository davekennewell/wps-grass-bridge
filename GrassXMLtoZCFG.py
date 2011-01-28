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
import sys
import os
import os.path
import wpsXML.WPS_1_0_0.OGC_WPS_1_0_0 as wps

class GrassXMLtoZcfg():
    """ Convert a Grass WPS XML file into a ZOO-WPS config file (zcfg)"""
    def __init__(self):
        pass
        
    def setGrassXMLFileName(self,  filename):
        self.__grassXMLFileName = filename
        if not os.path.isfile(self.__grassXMLFileName):
            raise IOError("Unable to open xml file")
            
    def setZcfgFileName(self,  filename):
        self.__zcfgFileName = filename
        self.__output = open(self.__zcfgFileName,  'w')

    def setPythonFileName(self,  filename):
        self.__pythonFileName = filename
        self.__pythonFile = open(self.__pythonFileName,  'w')

    def __writePythonFile(self, modulename, funcname):
        """Write the service python file for the ZOO Kernel"""
        self.__pythonFile.write("#####################################################\n")
        self.__pythonFile.write("# This service was generated using wps-grass-bridge #\n")
        self.__pythonFile.write("#####################################################\n")
        self.__pythonFile.write("import ZOOGrassModuleStarter as zoo\n")
        self.__pythonFile.write("def " + str(funcname) + "(m, inputs, outputs):\n")
        self.__pythonFile.write("    service = zoo.ZOOGrassModuleStarter()\n")
        self.__pythonFile.write("    service.fromMaps(\"" + str(modulename)+ "\", inputs, outputs)\n")
        self.__pythonFile.write("    return 3\n")
        self.__pythonFile.close()

    def __closeOutput(self):
        self.__output.close()
        
    def convert(self):
        """Start the conversion from WPS XML to ZOO-WPS config file zcfg"""
        try:
            doc = wps.CreateFromDocument(file(self.__grassXMLFileName).read())
            
            if len(doc.ProcessDescription) > 1:
                raise IOError("Only one Process is supported")
            
            for i in doc.ProcessDescription:
                self.__writeIdentTitleAbstract(i)
                self.__output.write("processVersion = 2\n")
                self.__output.write("storeSupported = true \n")
                self.__output.write("statusSupported = true\n")
                self.__output.write("serviceProvider = " + str(i.Identifier.value()).replace(".", "_") + "\n")
                self.__output.write("serviceType = Python\n")
                self.__writeDataInputs(i)
                self.__writeProcessOutputs(i)

                self.__writePythonFile(str(i.Identifier.value()), str(i.Identifier.value()).replace(".", "_"))
        except:
            raise
        finally:
            self.__closeOutput()
            
    def __writeDataInputs(self,  process):
        """Write all data inputs into the zcfg file"""
        self.__output.write("<DataInputs>\n")
        for i in process.DataInputs.Input:
            self.__writeIdentTitleAbstract(i,  "  ")
            self.__output.write("  minOccurs = " + str(i.minOccurs) + "\n")
            self.__output.write("  maxOccurs = " + str(i.maxOccurs) + "\n")
            if i.ComplexData != None:
                self.__writeComplexData(i.ComplexData)
            if i.LiteralData != None:
                self.__writeLiteralData(i.LiteralData)
        self.__output.write("</DataInputs>\n")
  
    def __writeProcessOutputs(self,  process):
        """Write all process outputs into the zcfg file"""
        for i in process.ProcessOutputs.Output:
            self.__output.write("<DataOutputs>\n")
            self.__writeIdentTitleAbstract(i,  "  ")
            if i.ComplexOutput != None:
                self.__writeComplexData(i.ComplexOutput)
            if i.LiteralOutput != None:
                self.__writeLiteralData(i.LiteralOutput)
            self.__output.write("</DataOutputs>\n")
           
    def __writeIdentTitleAbstract(self,  element,  indent=""):
        """Write identifier, title,and abstract """
        if element.Identifier != None:
            self.__output.write(indent + "[" + str(element.Identifier.value()).replace(".", "_").replace('\'', '') + "]\n")
        if element.Title.value() != None:
            self.__output.write(indent + "Title = " + str(element.Title.value()).replace("\n"," ").replace("\t",  " ").replace("=",  "::").replace('\'', '').replace('(', '').replace(')', '').replace('<', '').replace('>', '').replace('[', '').replace(']', '') + "\n")
        else:
            self.__output.write(indent + "Title =\n")
        if element.Abstract != None:
            self.__output.write(indent + "Abstract = " + str(element.Abstract.value()).replace("\n"," ").replace("\t",  " ").replace("=",  "::").replace('\'', '').replace('(', '').replace(')', '').replace('<', '').replace('>', '').replace('[', '').replace(']', '')  + "\n")
        else:
            self.__output.write(indent + "Abstract =\n")
    
    def __writeComplexData(self,  element):
        """Write the complex data into the zcfg file"""
        self.__output.write("  <ComplexData>\n")
        self.__output.write("    <Default>\n")
        if element.Default.Format.MimeType != None:
            self.__output.write("      mimeType = " + str(element.Default.Format.MimeType) + "\n")
        if element.Default.Format.Encoding != None:
            self.__output.write("      encoding = " + str(element.Default.Format.Encoding) + "\n")
        if element.Default.Format.Schema != None:
            self.__output.write("      schema = " + str(element.Default.Format.Schema) + "\n")
        self.__output.write("    </Default>\n")
        for i in element.Supported.Format:
            self.__output.write("    <Supported>\n")
            if i.MimeType != None:
                self.__output.write("      mimeType = " + str(i.MimeType) + "\n")
            if i.Encoding != None:
                self.__output.write("      encoding = " + str(i.Encoding) + "\n")
            if i.Schema != None:
                self.__output.write("      schema = " + str(i.Schema) + "\n")
            self.__output.write("    </Supported>\n")
        self.__output.write("  </ComplexData>\n")
        
    def __writeLiteralData(self,  element):
        """Write the literal data into the zcfg file"""
        self.__output.write("  <LiteralData>\n")
        if element.DataType != None:
            self.__output.write("    DataType   = " + str(element.DataType.value()) + "\n")
        # Allowed values are not supported for now
        #if element.AllowedValues != None:
        #    for i in element.AllowedValues.Value:
        #        self.__output.write("str(i.value()),")
        #    self.__output.write("\n")
        self.__output.write("    <Default>\n")
        if element.DefaultValue != None:
            self.__output.write("      value = " + str(element.DefaultValue) + "\n")
        self.__output.write("    </Default>\n")
        self.__output.write("  </LiteralData>\n")

def main():
    """The main function which will be called if the script is executed directly"""

    usage = "usage: %prog [-help,--help] --xmlfile inputfile.xml --zcfgfile output.txt]"
    description = "Use %prog to convert Grass 7.0 WPS XML process description files into ZOO-WPS server config files."
    parser = OptionParser(usage=usage, description=description)
    parser.add_option("-x", "--xmlfile", dest="xmlfile", help="The path to the grass WPS input xml file", metavar="FILE")
    parser.add_option("-z", "--zcfgfile", dest="zcfgfile", help="Path to the new created zcfg file", metavar="FILE")
    parser.add_option("-p", "--pythonfile", dest="pythonfile", help="Path to the new created python file", metavar="FILE")

    (options, args) = parser.parse_args()

    if options.xmlfile == None or options.zcfgfile == None or options.pythonfile == None:
        parser.print_help()
        parser.error("All file names must be provided")

    converter = GrassXMLtoZcfg()
    converter.setGrassXMLFileName(options.xmlfile)
    converter.setZcfgFileName(options.zcfgfile)
    converter.setPythonFileName(options.pythonfile)
    converter.convert()
    
    exit(0)

###############################################################################
if __name__ == "__main__":
    main()
