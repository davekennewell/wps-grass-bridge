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
sys.path.append("..")
import WPS_1_0_0.OGC_WPS_1_0_0 as wps

class GrassXMLtoPyWPS():
    """ Convert a Grass WPS XML file into a ZOO-WPS yaml config file"""
    def __init__(self):
        pass
        
    def setGrassXMLFileName(self,  filename):
        self.__grassXMLFileName = filename
        if not os.path.isfile(self.__grassXMLFileName):
            raise IOError("Unable to open xml file")
            
    def setPyWPSFileName(self,  filename):
        self.__pyWPSFileName = filename
        self.__output = open(self.__pyWPSFileName,  'w')
    
    def __closeOutput(self):
        self.__output.close()
        
    def convert(self):
    
        self.__content = {}
        """Start the conversion from WPS XML to PyWPS Python service file.
           Use nested dictionaries and arrays as data structure. """
        try:
            doc = wps.CreateFromDocument(file(self.__grassXMLFileName).read())
	    
            if len(doc.ProcessDescription) > 1:
                raise IOError("Only one Process is supported")
            
            for process in doc.ProcessDescription:
	        proc = {} 

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
	        self.__content["ProcessDescription"] = proc
	        
	    self.__writePyWPSFile()
        except:
            raise
        finally:
            self.__closeOutput()
            
    def __writePyWPSFile(self):
        """Write the PyWPS python process file"""
        self.__output.write("# ################################################ #\n")
        self.__output.write("# This process was generated using GrassXMLtoPyWPS #\n")
        self.__output.write("# Author: Soeren Gebbert                           #\n")
        self.__output.write("# Mail: soerengebbert <at> googlemail <dot> com    #\n")
        self.__output.write("# ################################################ #\n\n")
        self.__output.write("from pywps.Process import WPSProcess\n\n")
        self.__output.write("class " + str(self.__content["ProcessDescription"]["Identifier"]).replace(".", "_") + "(WPSProcess):\n\n")
        self.__output.write("  def __init__(self):\n")
        self.__output.write("    WPSProcess.__init__(self, identifier = \'" + str(self.__content["ProcessDescription"]["Identifier"]) + "\', ")
        self.__output.write("title = \'" + str(self.__content["ProcessDescription"]["Title"]) + "\', ")
        self.__output.write("version = " + str(self.__content["ProcessDescription"]["processVersion"]) + ", ")
        self.__output.write("statusSupported = " + str(self.__content["ProcessDescription"]["statusSupported"]) + ", ")
        self.__output.write("storeSupported = " + str(self.__content["ProcessDescription"]["storeSupported"]) + ", ")
        self.__output.write("metadata = " + str(self.__content["ProcessDescription"]["Metadata"]) + ", ")
        self.__output.write("abstract = \'" + str(self.__content["ProcessDescription"]["Abstract"]) + "\')\n")
        
        
        self.__output.write("\n    # Literal and complex inputs\n")
        # Write the literal and complex inputs        
        for input in self.__content["ProcessDescription"]["DataInputs"]:
            if input.has_key("ComplexData"):
	        self.__output.write("    self.addComplexInput(")
	    elif input.has_key("LiteralData"):
	        self.__output.write("    self.addLiteralInput(")
	        
	    self.__output.write("identifier = \'" + input["Identifier"] + "\', ")
	    self.__output.write("title = \'" + input["Title"] + "\', ")
	    if input.has_key("Abstract"):
                self.__output.write("abstract = \'" + input["Abstract"] + "\', ")
            self.__output.write("minOccurs = " + str(input["minOccurs"]) + ", ")
            self.__output.write("maxOccurs = " + str(input["maxOccurs"]) + "") 
            
            if input.has_key("LiteralData"):
                if input["LiteralData"]["DataType"] == "float":
	            self.__output.write(", type = type(0.0)")
                if input["LiteralData"]["DataType"] == "integer":
	            self.__output.write(", type = type(0)")
                if input["LiteralData"]["DataType"] == "boolean":
	            self.__output.write(", type = type(True)")
                if input["LiteralData"]["DataType"] == "string":
	            self.__output.write(", type = type(\"string\")")
	        if input["LiteralData"].has_key("DefaultValue"):
                    if input["LiteralData"]["DataType"] == "string":
                        self.__output.write(", default = \"" + str(input["LiteralData"]["DefaultValue"]) + "\"")	 
                    else:
                        self.__output.write(", default = " + str(input["LiteralData"]["DefaultValue"]))	       
	        if input["LiteralData"].has_key("AllowedValues"):
	            self.__output.write(", allowedValues = \'" + str(input["LiteralData"]["AllowedValues"]) + "\'")
	        elif input["LiteralData"].has_key("AnyValue"):
	            self.__output.write(", allowedValues = \'*\'")
            if input.has_key("ComplexData"):
                self.__output.write(", formats = " + str(input["ComplexData"]["Supported"])) 
            self.__output.write(")\n")
            
        # For now only complex outputs are supported
        self.__output.write("\n    # complex outputs\n")
        for output in self.__content["ProcessDescription"]["ProcessOutputs"]:
            if output.has_key("ComplexOutput"):
	        self.__output.write("    self.addComplexOutput(")
	    self.__output.write("identifier = \'" + output["Identifier"] + "\', ")
	    self.__output.write("title = \'" + output["Title"] + "\'")
	    if output.has_key("Abstract"):
                self.__output.write(", abstract = \'" + output["Abstract"] + "\'")
            self.__output.write(", formats = " + str(output["ComplexOutput"]["Supported"]))
            self.__output.write(")\n")

        self.__output.write("\n\n  def execute(self):\n")
        self.__output.write("    pass\n\n\n")
            
        # For debug only
        self.__output.write("if __name__ == \"__main__\":\n")
        self.__output.write("  print \"Self test\"\n")
        self.__output.write("  p = " + str(self.__content["ProcessDescription"]["Identifier"]).replace(".", "_") + "()\n")
        self.__output.write("  p.execute()\n")
        self.__output.write("  for input in p.inputs:\n")
        self.__output.write("    print input\n")
        self.__output.write("  for output in p.outputs:\n")
        self.__output.write("    print output\n")
                        	
    def __getTitleAbstract(self, element):
        """Create the title and abstract for yaml zcfg file"""
        ita = {} 
        if element.Title.value() != None:
            ita["Title"] = str(element.Title.value()).replace('\'', '')
        if element.Abstract != None:
            ita["Abstract"] = str(element.Abstract.value()).replace('\'', '')
            
        return ita
        
    def __getDataInputs(self,  process):
        """Create data inputs for yaml zcfg file"""
        dataInputs = [] 
        for data in process.DataInputs.Input:
            input = {} 
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
        processOutputs = [] 
        for data in process.ProcessOutputs.Output:
            output = {} 
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
        complexData = {} 
        default = {}     
        supported = []   
        

        if element.Default.Format.MimeType != None:
            default["mimeType"] = str(element.Default.Format.MimeType)
        if element.Default.Format.Encoding != None:
            default["encoding"] = str(element.Default.Format.Encoding)
        if element.Default.Format.Schema != None:
            default["schema"] = str(element.Default.Format.Schema)
        complexData["Default"] = default
        
        for format in element.Supported.Format:
          supformat = {}
	  if format.MimeType != None:
	      supformat["mimeType"] = str(format.MimeType)
	  if element.Default.Format.Encoding != None:
	      supformat["encoding"] = str(format.Encoding)
	  if element.Default.Format.Schema != None:
	      supformat["schema"] = str(format.Schema)
	  if supformat:
	      supported.append(supformat)
        
        complexData["Supported"] = supported
        
        return complexData
        
    def __getLiteralData(self,  element):
        """Write the literal data into the yaml zcfg file"""
        literalData = {}   
        allowedValues = [] 
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
            UOMs = {}      
            supported = [] 
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
    description = "Use %prog to convert Grass 7.0 WPS XML process description files into Py-WPS server python process files."
    parser = OptionParser(usage=usage, description=description)
    parser.add_option("-x", "--xmlfile", dest="xmlfile", help="The path to the grass WPS input xml file", metavar="FILE")
    parser.add_option("-p", "--pythonfile", dest="pythonfile", help="Path to the new created PyWPS python process file", metavar="FILE")

    (options, args) = parser.parse_args()

    if options.xmlfile == None or options.pythonfile == None:
        parser.print_help()
        parser.error("Booth file names must be provided")

    converter = GrassXMLtoPyWPS()
    converter.setGrassXMLFileName(options.xmlfile)
    converter.setPyWPSFileName(options.pythonfile)
    converter.convert()
    
    exit(0)

###############################################################################
if __name__ == "__main__":
    main()
