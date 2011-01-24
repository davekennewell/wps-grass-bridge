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
import wpsXML.GrassXMLtoDict as wps

class GrassXMLtoPyWPS(wps.GrassXMLtoDict):
    """ Convert a Grass WPS XML file into PyPWS process file"""
    def __init__(self):
        wps.GrassXMLtoDict.__init__(self)
        
    def convert(self):
        try:
            self._parseXML()

            """Write the PyWPS python process file"""
            self._output.write("# ################################################ #\n")
            self._output.write("# This process was generated using GrassXMLtoPyWPS #\n")
            self._output.write("# Author: Soeren Gebbert                           #\n")
            self._output.write("# Mail: soerengebbert <at> googlemail <dot> com    #\n")
            self._output.write("# ################################################ #\n\n")
            self._output.write("from pywps.Process import WPSProcess\n\n")
            self._output.write("from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter\n\n")
            self._output.write("class " + str(self._content["ProcessDescription"]["Identifier"]).replace(".", "_") + "(WPSProcess):\n\n")
            self._output.write("  def __init__(self):\n")
            self._output.write("    WPSProcess.__init__(self, identifier = \'" + str(self._content["ProcessDescription"]["Identifier"]) + "\', ")
            self._output.write("title = \'" + str(self._content["ProcessDescription"]["Title"]).replace("<", "&#60;").replace(">", "&#62;").strip() + "\', ")
            self._output.write("version = " + str(self._content["ProcessDescription"]["processVersion"]) + ", ")
            self._output.write("statusSupported = " + str(self._content["ProcessDescription"]["statusSupported"]) + ", ")
            self._output.write("storeSupported = " + str(self._content["ProcessDescription"]["storeSupported"]) + ", ")
            self._output.write("metadata = " + str(self._content["ProcessDescription"]["Metadata"]) + ", ")
            self._output.write("abstract = \'" + str(self._content["ProcessDescription"]["Abstract"]).replace("<", "&#60;").replace(">", "&#62;").strip() + "\')\n")


            self._output.write("\n    # Literal and complex inputs\n")
            # Write the literal and complex inputs
            for input in self._content["ProcessDescription"]["DataInputs"]:
                if input.has_key("ComplexData"):
                    self._output.write("    self.addComplexInput(")
                elif input.has_key("LiteralData"):
                    self._output.write("    self.addLiteralInput(")

                self._output.write("identifier = \'" + input["Identifier"] + "\', ")
                self._output.write("title = \'" + input["Title"].replace("<", "&#60;").replace(">", "&#62;").strip() + "\', ")
                if input.has_key("Abstract"):
                    self._output.write("abstract = \'" + input["Abstract"].replace("<", "&#60;").replace(">", "&#62;").strip() + "\', ")
                self._output.write("minOccurs = " + str(input["minOccurs"]) + ", ")
                self._output.write("maxOccurs = " + str(input["maxOccurs"]) + "")

                if input.has_key("LiteralData"):
                    if input["LiteralData"]["DataType"] == "float":
                        self._output.write(", type = type(0.0)")
                    if input["LiteralData"]["DataType"] == "integer":
                        self._output.write(", type = type(0)")
                    if input["LiteralData"]["DataType"] == "boolean":
                        self._output.write(", type = type(True)")
                    if input["LiteralData"]["DataType"] == "string":
                        self._output.write(", type = type(\"string\")")
                    if input["LiteralData"].has_key("DefaultValue"):
                        if input["LiteralData"]["DataType"] == "string":
                            self._output.write(", default = \"" + str(input["LiteralData"]["DefaultValue"]) + "\"")
                        else:
                            self._output.write(", default = " + str(input["LiteralData"]["DefaultValue"]))
                    if input["LiteralData"].has_key("AllowedValues"):
                        self._output.write(", allowedValues = " + str(input["LiteralData"]["AllowedValues"]))
                    elif input["LiteralData"].has_key("AnyValue"):
                        self._output.write(", allowedValues = \'*\'")
                if input.has_key("ComplexData"):
                    self._output.write(", formats = " + str(input["ComplexData"]["Supported"]))
                self._output.write(")\n")

            # For now only complex outputs are supported
            self._output.write("\n    # complex outputs\n")
            for output in self._content["ProcessDescription"]["ProcessOutputs"]:
                if output.has_key("ComplexOutput"):
                    self._output.write("    self.addComplexOutput(")
                self._output.write("identifier = \'" + output["Identifier"] + "\', ")
                self._output.write("title = \'" + output["Title"].replace("<", "&#60;").replace(">", "&#62;").strip() + "\'")
                if output.has_key("Abstract"):
                    self._output.write(", abstract = \'" + output["Abstract"].replace("<", "&#60;").replace(">", "&#62;").strip() + "\'")
                self._output.write(", formats = " + str(output["ComplexOutput"]["Supported"]))
                self._output.write(")\n\n")

            self._output.write("  def execute(self):\n")
            self._output.write("    starter = PyWPSGrassModuleStarter()\n")
            self._output.write("    starter.fromPyWPS(\"" + self._content["ProcessDescription"]["Identifier"] +  "\", self.inputs, self.outputs, self.pywps)\n\n")

            self._output.write("if __name__ == \"__main__\":\n")
            self._output.write("  process = " + str(self._content["ProcessDescription"]["Identifier"]).replace(".", "_") + "()\n")
            self._output.write("  process.execute()\n")
        except:
            raise
        finally:
            self._closeOutput()

    def _getComplexData(self,  element):
        """This virtual method from GrassXMLToDict must be override, because
        PyWPs uses lower cases for default and supported formats"""
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

def main():
    """The main function which will be called if the script is executed directly"""

    usage = "usage: %prog [-help,--help] --xmlfile module.xml --pythonfile module.py]"
    description = "Use %prog to convert Grass 7.0 WPS XML process description files into Py-WPS server python process files."
    parser = OptionParser(usage=usage, description=description)
    parser.add_option("-x", "--xmlfile", dest="xmlfile", help="The path to the grass WPS input xml file", metavar="FILE")
    parser.add_option("-p", "--pythonfile", dest="pythonfile", help="Path to the new created PyWPS python process file", metavar="FILE")

    (options, args) = parser.parse_args()

    if options.xmlfile == None or options.pythonfile == None:
        parser.print_help()
        parser.error("Booth file names must be provided")

    converter = GrassXMLtoPyWPS()
    converter.setXMLFileName(options.xmlfile)
    converter.setOutputFileName(options.pythonfile)
    converter.convert()
    
    exit(0)

###############################################################################
if __name__ == "__main__":
    main()
