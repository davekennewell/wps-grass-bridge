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
import WPS_1_0_0.OGC_WPS_1_0_0 as wps
import yaml

class GrassXMLtoYAML():
    """ Convert a Grass WPS XML file into a ZOO-WPS yaml config file"""
    def __init__(self):
        pass
        
    def setGrassXMLFileName(self,  filename):
        self.__grassXMLFileName = filename
        if not os.path.isfile(self.__grassXMLFileName):
            raise IOError("Unable to open xml file")
            
    def setZcfgFileName(self,  filename):
        self.__zcfgFileName = filename
        self.__output = open(self.__zcfgFileName,  'w')
    
    def __closeOutput(self):
        self.__output.close()
        
    def convert(self):
    
        self.__yam = {}
        """Start the conversion from WPS XML to ZOO-WPS yaml config file.
           Use nested dictionaries and arrays as data structure. """
        try:
            doc = wps.CreateFromDocument(file(self.__grassXMLFileName).read())
            
            zcfg = {} # dict for yaml output generation

	    zcfg['serviceProvider'] = "test_service"
	    zcfg['serviceType'] = "Python"
	    self.__yam["zcfg"] = zcfg
	    
            if len(doc.ProcessDescription) > 1:
                raise IOError("Only one Process is supported")
            
            for process in doc.ProcessDescription:
	        proc = {} # dict for yaml output generation

	        proc['processVersion'] = str(process.processVersion)
	        proc['storeSupported'] = bool(process.storeSupported)
	        proc['statusSupported'] = bool(process.statusSupported)
		proc["Identifier"] = str(process.Identifier.value())

                if process.Metadata != None:
                    metaData = []
                    for meta in process.Metadata:
                        content = {}
                        if meta.title != None:
                            content["title"] = str(meta.title)
                        if meta.about != None:
                            content["about"] = str(meta.about)
                        if meta.arcrole != None:
                            content["arcrole"] = str(meta.arcrole)
                        if meta.actuate != None:
                            content["actuate"] = str(meta.actuate)
                        if meta.href != None:
                            content["href"] = str(meta.href)
                        if meta.role != None:
                            content["role"] = str(meta.role)
                        if meta.type != None:
                            content["type"] = str(meta.type)
                        if meta.show != None:
                            content["show"] = str(meta.show)
                        metaData.append(content)
                    proc["Metadata"] = metaData


	        ita = self.__getTitleAbstract(process)
	        for key in ita.keys():
		    proc[key] = ita[key] 
	        proc["DataInputs"] = self.__getDataInputs(process)
	        proc["ProcessOutputs"] = self.__getProcessOutputs(process)
	        self.__yam["ProcessDescription"] = proc


	        
	    yaml.dump(self.__yam, self.__output, default_flow_style=False)
        except:
            raise
        finally:
            self.__closeOutput()
            
    def __getTitleAbstract(self, element):
        """Create the title and abstract for yaml zcfg file"""
        ita = {} # dict for yaml output generation
        if element.Title.value() != None:
            ita["Title"] = str(element.Title.value()).replace('\'', '')
        if element.Abstract != None:
            ita["Abstract"] = str(element.Abstract.value()).replace('\'', '')
            
        return ita
        
    def __getDataInputs(self,  process):
        """Create data inputs for yaml zcfg file"""
        dataInputs = [] # array for yaml output generation
        for data in process.DataInputs.Input:
            input = {} # dict for yaml output generation
            input["Identifier"] = str(data.Identifier.value())
            ita = self.__getTitleAbstract(data)
            for key in ita.keys():
                input[key] = ita[key] 
                
            input["minOccurs"] = int(data.minOccurs)
            input["maxOccurs"] = int(data.maxOccurs)
            
            if data.ComplexData != None:
                input["ComplexData"] = self.__getComplexData(data.ComplexData)
            if data.LiteralData != None:
                input["LiteralData"] = self.__getLiteralData(data.LiteralData)
                
            dataInputs.append(input)
            
        return dataInputs
  
    def __getProcessOutputs(self,  process):
        """Create process outputs for yaml zcfg file"""
        processOutputs = [] # array for yaml output generation
        for data in process.ProcessOutputs.Output:
            output = {} # dict for yaml output generation
            output["Identifier"] = str(data.Identifier.value())    
            ita = self.__getTitleAbstract(data)
            for key in ita.keys():
                output[key] = ita[key] 
                
            if data.ComplexOutput != None:
                output["ComplexOutput"] = self.__getComplexData(data.ComplexOutput)
            if data.LiteralOutput != None:
                output["LiteralOutput"] = self.__getLiteralData(data.LiteralOutput)
                            
            processOutputs.append(output)
            
        return processOutputs
        
    def __getComplexData(self,  element):
        """Create complex data for yaml zcfg file"""
        complexData = {} # dict for yaml output generation
        default = {} # dict for yaml output generation
        supported = [] # dict for yaml output generation

        if element.Default.Format.MimeType != None:
            default["MimeType"] = str(element.Default.Format.MimeType)
        if element.Default.Format.Encoding != None:
            default["Encoding"] = str(element.Default.Format.Encoding)
        if element.Default.Format.Schema != None:
            default["Schema"] = str(element.Default.Format.Schema)
        complexData["Default"] = default
        
        for format in element.Supported.Format:
          supformat = {}
	  if format.MimeType != None:
	      supformat["MimeType"] = str(format.MimeType)
	  if element.Default.Format.Encoding != None:
	      supformat["Encoding"] = str(format.Encoding)
	  if element.Default.Format.Schema != None:
	      supformat["Schema"] = str(format.Schema)
	  if supformat:
	      supported.append(supformat)
        complexData["Supported"] = supported
        
        return complexData
        
    def __getLiteralData(self,  element):
        """Write the literal data into the yaml zcfg file"""
        literalData = {} # dict for yaml output generation
        allowedValues = [] # array for yaml output generation
        if element.DataType != None:
            literalData["DataType"] = str(element.DataType.value())
        if element.AllowedValues != None:
            for value in element.AllowedValues.Value:
                try:
                    if literalData["DataType"] == "boolean":
                        if str(value.value()) == "true":
                            allowedValues.append(True)
                        if str(value.value()) == "false":
                            allowedValues.append(False)
                    elif literalData["DataType"] == "integer":
                        allowedValues.append(int(value.value()))
                    elif literalData["DataType"] == "float":
                        allowedValues.append(float(value.value()))
                    else:
                        allowedValues.append(str(value.value()))
                except:
                    allowedValues.append(str(value.value()))
            literalData["AllowdValues"] = allowedValues
        if element.DefaultValue != None:
            try:
                if literalData["DataType"] == "boolean":
                    if element.DefaultValue == "true":
                        literalData["DefaultValue"] = True
                    if element.DefaultValue == "false":
                        literalData["DefaultValue"] = False
                elif literalData["DataType"] == "integer":
                    literalData["DefaultValue"] = int(element.DefaultValue)
                elif literalData["DataType"] == "float":
                    literalData["DefaultValue"] = float(element.DefaultValue)
                else:
                    literalData["DefaultValue"] = str(element.DefaultValue)
            except:
                literalData["DefaultValue"] = str(element.DefaultValue)
        else:
            literalData["AnyValue"] = True

        if element.UOMs != None:
            UOMs = {} # dict for yaml output generation
            supported = [] # array for yaml output generation
            if element.UOMs.Default != None:
                UOMs["Default"] = str(element.UOMs.Default.UOM.value())
            if element.UOMs.Supported != None:
                for i in element.UOMs.Supported.UOM:
                    supported.append(str(i.value()))
                UOMs["Supported"] = supported
                literalData["UOMs"] = UOMs
            
        return literalData
        # Literal output and BBox are not implemented yet

def main():
    """The main function which will be called if the script is executed directly"""

    usage = "usage: %prog [-help,--help] --xmlfile inputfile.xml --zcfgfile output.txt]"
    description = "Use %prog to convert Grass 7.0 WPS XML process description files into ZOO-WPS server YAML config files."
    parser = OptionParser(usage=usage, description=description)
    parser.add_option("-x", "--xmlfile", dest="xmlfile", help="The path to the grass WPS input xml file", metavar="FILE")
    parser.add_option("-z", "--zcfgfile", dest="zcfgfile", help="Path to the new created yaml file", metavar="FILE")

    (options, args) = parser.parse_args()

    if options.xmlfile == None or options.zcfgfile == None:
        parser.print_help()
        parser.error("Booth file names must be provided")

    converter = GrassXMLtoYAML()
    converter.setGrassXMLFileName(options.xmlfile)
    converter.setZcfgFileName(options.zcfgfile)
    converter.convert()
    
    exit(0)

###############################################################################
if __name__ == "__main__":
    main()
