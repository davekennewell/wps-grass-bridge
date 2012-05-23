# -*- coding: utf-8 -*-
################################################################################
# Author:	Soeren Gebbert
#
# Copyright (C) 2010 Soeren Gebbert
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

import GlobalGrassSettings
import os.path
# Import the GrassModuleStarter
from gms.GrassModuleStarter import *

class ZOOGrassModuleStarter(GrassModuleStarter):
    """Start a grass module specified by ZOO-WPS server"""
    def __init__(self):
        GrassModuleStarter.__init__(self)

    ############################################################################
    def fromMaps(self, grassModule, inputs, outputs):

        self._grassModule = grassModule
        self._inputs = inputs
        self._outputs = outputs
        
        # Create the tmp working directory and initiate the logging functionality
        try:
            self._createTemporalDir(GlobalGrassSettings.WORKDIR)

            logfile = GlobalGrassSettings.LOGFILE
            module_stdout = GlobalGrassSettings.LOGFILE_MODULE_STDOUT
            module_stderr = GlobalGrassSettings.LOGFILE_MODULE_STDERR

            ModuleLogging.__init__(self, logfile, module_stdout, module_stderr)

            self.LogInfo(str(inputs))
            self.LogInfo(str(outputs))
        except:
            print "ERROR: Unable to start logging. break"
            raise
        try:
            # Setup a temporary GRASS location to get the module XML WPS process description
            self._setInputParameterInit()
            self._setUpGrassLocation(self.inputParameter.grassGisBase, self.inputParameter.grassAddonPath)

            try:
                # Parse the ZOO maps and create the GrassModuleStarter structures
                self._parseInputsAndOutputs()
                # Write the complex inputs into files
                self._createInputFiles()
                # Create the output file names
                self._createOutputFiles()
            except:
                raise
            # Create input and output maps
            self._createInputOutputMaps()
            # Import all data, run the module and export the data
            # Before import check if zipped shape files are present in input and
            # Extract them and update the input map
            self._checkForZippedShapeFiles()
            # Create the new location based on the first valid input and import all maps
            self._importData()
            # start the grass module one or multiple times, depending on the multiple import parameter
            self._startGrassModule()
            # now export the results
            self._exportOutput()
            # Attach the results to the outputs list
            self._attachOutputFiles()
            self.LogInfo(str(outputs))
        except:
            raise
        finally:
            # clean up
            self._removeTempData()
            self._closeLogfiles()

    ############################################################################
    def _setInputParameterInit(self):
        """Initiate the input parameter"""
        self.inputParameter = InputParameter(self.logfile)
        self.inputParameter.grassGisBase = GlobalGrassSettings.GRASS_GIS_BASE
        self.inputParameter.grassAddonPath = GlobalGrassSettings.GRASS_ADDON_PATH
        self.inputParameter.grassVersion = GlobalGrassSettings.GRASS_VERSION
        self.inputParameter.grassModule = self._grassModule

    ############################################################################
    def _createInputFiles(self):
        """ Generate input file names and write the content of the input map into files on hard disk """
        count = 0
        for input in self.inputParameter.complexDataList:
            filename = os.path.join(self.gisdbase, input.identifier + "_" + str(count))
            try:
                infile = open(filename, 'w')
                infile.write(self._inputs[input.identifier]["value"])
                infile.close()
            except:
                self.LogError("Unable to create input files")
                raise
            self._inputs[input.identifier]["value"] = filename
            input.pathToFile= filename
            self.LogInfo("Created input filename " + filename)
            count = count + 1
 
    ############################################################################
    def _createOutputFiles(self):
        """ Create the output file names which are used to identify the outputs """
        count = 0
        for output in self.inputParameter.complexOutputList:
            filename = os.path.join(self.gisdbase, output.identifier + "_" + str(count))
            output.pathToFile= filename
            self.LogInfo("Created output filename " + filename)
            count = count + 1
 
    ############################################################################
    def _attachOutputFiles(self):
        """Read into memory and Attach the computation result to the output map"""
        count = 0
        for output in self.inputParameter.complexOutputList:
            filename = output.pathToFile
            try:
                content = open(filename, 'r')
                self._outputs[output.identifier]["value"] = content.read()
            except:
                self.LogError("Unable to read output file")
                raise
            self.LogInfo("Attached output file " + filename)
            count = count + 1
        
    ############################################################################
    def _parseInputsAndOutputs(self):
        # Parse the inputs
	for key in self._inputs.keys():
            if self._inputs[key]["inRequest"].lower() == 'true':
                # Complex Data
                if self._inputs[key].has_key("mimeType") == True and self._inputs[key].has_key("value") == True and self._inputs[key]["value"] != 'NULL':
                    self.LogInfo("Attach complex data " + key)
                    input = ComplexData()
                    input.identifier = key
                    input.pathToFile = self._inputs[key]["value"]
                    input.mimeType = self._inputs[key]["mimeType"]
                    input.maxOccurs = self._inputs[key]["maxOccurs"]
                    if self._inputs[key].has_key("encoding"):
                        input.encoding = self._inputs[key]["encoding"]
                    if self._inputs[key].has_key("schema"):
                        input.schema = self._inputs[key]["schema"]
                    self.inputParameter.complexDataList.append(input)
                # Literal Data
                if self._inputs[key].has_key("DataType") == True and self._inputs[key].has_key("value") == True and self._inputs[key]["value"] != 'NULL':
                    self.LogInfo("Attach literal data " + key)
                    input = LiteralData()
                    input.identifier = key
                    input.value = self._inputs[key]["value"]
                    input.type = self._inputs[key]["DataType"]
                    self.inputParameter.literalDataList.append(input)
        # Only complex outputs are currently supported by grass
	for key in self._outputs.keys():
            if self._outputs[key]["inRequest"].lower() == 'true':
                # Complex Output
                if self._outputs[key].has_key("mimeType") == True:
                    self.LogInfo("Attach complex output " + key)
                    output = ComplexData()
                    output.identifier = key
                    output.mimeType = self._outputs[key]["mimeType"]
                    if self._outputs[key].has_key("encoding"):
                        output.encoding = self._outputs[key]["encoding"]
                    if self._outputs[key].has_key("schema"):
                        output.schema = self._outputs[key]["schema"]
                    self.inputParameter.complexOutputList.append(output)

################################################################################
def main():
    # Simple test case
    inputs = {'input': {'maxOccurs': '1', 'minOccurs': '0', 'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.0/polygon.xsd', 'xlink:href': 'http://carto.languedoc-roussillon.ecologie.gouv.fr/webservices/wfs/diren_general/?VERSION=1.1.0&service=WFS&request=GetFeature&typename=Znieff1&maxfeatures=1', 'value': '<?xml version=\'1.0\' encoding="UTF-8" ?>\n<wfs:FeatureCollection\n   xmlns:ms="http://mapserver.gis.umn.edu/mapserver"\n   xmlns:gml="http://www.opengis.net/gml"\n   xmlns:wfs="http://www.opengis.net/wfs"\n   xmlns:ogc="http://www.opengis.net/ogc"\n   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n   xsi:schemaLocation="http://mapserver.gis.umn.edu/mapserver http://carto.languedoc-roussillon.ecologie.gouv.fr/final/mapjax/webservices//wfs/diren_general/?SERVICE=WFS&amp;VERSION=1.1.0&amp;REQUEST=DescribeFeatureType&amp;TYPENAME=Znieff1&amp;OUTPUTFORMAT=text/xml; subtype=gml/3.1.1  http://www.opengis.net/wfs http://schemas.opengis.net/wfs/1.1.0/wfs.xsd">\n      <gml:boundedBy>\n      \t<gml:Envelope srsName="EPSG:27572">\n      \t\t<gml:lowerCorner>549421.218052 1703199.993069</gml:lowerCorner>\n      \t\t<gml:upperCorner>801405.118492 1990265.823167</gml:upperCorner>\n      \t</gml:Envelope>\n      </gml:boundedBy>\n    <gml:featureMember>\n      <ms:Znieff1 gml:id="Znieff1.11">\n        <gml:boundedBy>\n        \t<gml:Envelope srsName="EPSG:27572">\n        \t\t<gml:lowerCorner>609360.619377 1818923.090409</gml:lowerCorner>\n        \t\t<gml:upperCorner>610176.568795 1821136.189945</gml:upperCorner>\n        \t</gml:Envelope>\n        </gml:boundedBy>\n        <ms:msGeometry>\n          <gml:Polygon srsName="EPSG:27572">\n            <gml:exterior>\n              <gml:LinearRing>\n                <gml:posList srsDimension="2">609953.620527 1821125.764306 609965.191840 1821108.579188 609962.785923 1821078.562515 609926.353472 1820970.067135 609934.373194 1820864.206806 610055.012725 1820718.018733 610123.294928 1820567.706231 610176.568795 1820321.844472 610050.773729 1820223.087325 609975.159208 1820044.247527 609905.158493 1819973.788542 609899.659255 1819809.269676 609805.943077 1819640.511814 609724.141913 1819393.962650 609689.198840 1819211.456694 609673.961368 1818923.090409 609578.182975 1818958.377185 609490.997142 1819035.939352 609490.768007 1819106.054635 609437.494140 1819307.349654 609360.619377 1819403.930019 609387.199027 1819438.529391 609475.186833 1819455.485374 609546.447790 1819476.222083 609631.571409 1819562.033108 609717.153299 1819805.947220 609820.951413 1819995.212656 609932.310980 1820195.820271 609936.549976 1820385.887679 609869.298879 1820597.264635 609799.985569 1820691.439083 609692.635863 1820749.639350 609638.560024 1820859.165838 609621.374906 1820979.003396 609699.968180 1821106.860676 609768.823221 1821123.816660 609845.239714 1821127.826521 609918.219183 1821136.189945 609953.620527 1821125.764306 609953.620527 1821125.764306 </gml:posList>\n              </gml:LinearRing>\n            </gml:exterior>\n          </gml:Polygon>\n        </ms:msGeometry>\n        <ms:toponyme>Ar\xc3\xaate rocheuse de Fount-Ferrouzo</ms:toponyme>\n        <ms:id>4085-0010</ms:id>\n        <ms:surface_sig_ha>46.5860506579831</ms:surface_sig_ha>\n      </ms:Znieff1>\n    </gml:featureMember>\n</wfs:FeatureCollection>\n\n', 'encoding': 'UTF-8'}, '-t': {'maxOccurs': '1', 'minOccurs': '0', 'DataType': 'boolean', 'value': 'false'}, '-l': {'maxOccurs': '1', 'minOccurs': '0', 'DataType': 'boolean', 'value': 'false'}}
    outputs = {'output': {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.0/polygon.xsd', 'value': 'NULL', 'encoding': 'UTF-8'}}
    
    starter = ZOOGrassModuleStarter()
    starter.fromMaps("v.voronoi", inputs, outputs)
    
    print str(outputs['output']['value'])
        
    exit(0)

###############################################################################
if __name__ == "__main__":
    main()
