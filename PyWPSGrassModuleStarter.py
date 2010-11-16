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
import tempfile
from types import *
# Import the GrassModuleStarter
from gms.GrassModuleStarter import *
# Impot the PyWPS stuff.. Mask the name to avoid conflicts with the GrassModuleStarter
from pywps.Process.InAndOutputs import LiteralInput as PyWPSLiteralInput
from pywps.Process.InAndOutputs import ComplexInput as PyWPSComplexInput
from pywps.Process.InAndOutputs import ComplexOutput as PyWPSComplexOutput

class PyWPSGrassModuleStarter(GrassModuleStarter):
    """Start a grass module specified by PyWPS server"""
    def __init__(self):
        GrassModuleStarter.__init__(self)

    ############################################################################
    def fromPyWPS(self, grassModule, inputs, outputs):

        self._grassModule = grassModule
        self._inputs = inputs
        self._outputs = outputs
        
        # Initiate the logging mechanism and the logfiles
        ModuleLogging.__init__(self, GlobalGrassSettings.LOGFILE, GlobalGrassSettings.LOGFILE_MODULE_STDOUT, GlobalGrassSettings.LOGFILE_MODULE_STDERR)

        # Parse the input parameter of the text file
        self.inputParameter = InputParameter(self.logfile)
        # Initiate the input parameter for the GrassModuleStarter
        self._setInputParameterInit()
        # Parse the PyWPS input and output data
        self._parsePyWPSInputsOutputs()
        
        try:
            self._createInputOutputMaps()
            self._createOutputFiles()
            try:
                # Temporal directory must be created at the beginning
                self._createTemporalDir(self.inputParameter.workDir)
                self._setUpGrassLocation(self.inputParameter.grassGisBase, self.inputParameter.grassAddonPath)
                # Import all data, run the module and export the data
                # Before import check if zipped shape files are present in input and
                # Extract them and update the input map
                self._checkForZippedShapeFiles()
                # Create the new location based on the first valid input and import all maps
                self._importData()
                # start the grass module 
                self._startGrassModule()
                # now export the results
                self._exportOutput()
                # Pass outputs
                self._passOutputs()
            except:
                raise
            finally:
                self._removeTempData()
        except:
            raise
        finally:
            self._closeLogfiles()
            
    ############################################################################
    def _parsePyWPSInputsOutputs(self):
        
        for input in self._inputs:
            if isinstance(self._inputs[input], PyWPSLiteralInput):
                data = LiteralData()
                data.identifier = self._inputs[input].identifier
                data.value = self._inputs[input].getValue()
                #check for double, integer, boolean, string
                if self._inputs[input].dataType is IntType:
                    data.type = "integer"
                elif self._inputs[input].dataType is FloatType:
                    data.type = "double"
                elif self._inputs[input].dataType is StringType:
                    data.type = "string"
                elif self._inputs[input].dataType is BooleanType:
                    data.type = "boolean"
                    if data.value == False:
                        data.value = "False"
                    elif data.type == True:
                        data.value = "True"
                    else:
                        data.value = "False"
                else:
                    data.type = "string"
                self.inputParameter.literalDataList.append(data)
                self.LogInfo("Added literal input " + data.identifier)
            elif isinstance(self._inputs[input], PyWPSComplexInput):
                data = ComplexData()
                data.identifier = self._inputs[input].identifier
                data.pathToFile = self._inputs[input].getValue()
                data.maxOccurs = self._inputs[input].maxOccurs
                data.mimeType = self._inputs[input].format["mimeType"]
                data.schema = self._inputs[input].format["schema"]
                data.encoding = self._inputs[input].format["encoding"]
                self.inputParameter.complexDataList.append(data)
                self.LogInfo("Added complex input " + data.identifier)
        
        for output in self._outputs:
            if isinstance(self._outputs[output], PyWPSComplexOutput):
                data = ComplexOutput()
                data.identifier = self._outputs[output].identifier
                data.mimeType = self._outputs[output].format["mimeType"]
                data.schema = self._outputs[output].format["schema"]
                data.encoding = self._outputs[output].format["encoding"]
                self.inputParameter.complexOutputList.append(data)
                self.LogInfo("Added complex output " + data.identifier)


    ############################################################################
    def _setInputParameterInit(self):
        """Initiate the input parameter"""
        self.inputParameter = InputParameter(self.logfile)
        self.inputParameter.grassGisBase = GlobalGrassSettings.GRASS_GIS_BASE
        self.inputParameter.grassAddonPath = GlobalGrassSettings.GRASS_ADDON_PATH
        self.inputParameter.grassVersion = GlobalGrassSettings.GRASS_VERSION
        self.inputParameter.workDir = GlobalGrassSettings.WORKDIR
        self.inputParameter.grassModule = self._grassModule
 
    ############################################################################
    def _createOutputFiles(self):
        """Create the output file names which are used to identify the outputs"""
        count = 0
        for output in self.inputParameter.complexOutputList:
            filename = tempfile.mktemp(prefix=output.identifier + "_" + str(count),dir=GlobalGrassSettings.OUTPUTDIR)
            output.pathToFile= filename
            self.LogInfo("Created output filename " + filename)
            count = count + 1
            

    ############################################################################
    def _passOutputs(self):
        for output in self.inputParameter.complexOutputList:
            filename = output.pathToFile
            try:
                self._outputs[output.identifier].setValue(filename)
            except:
                self.LogError("Unable to attach output file")
                raise
            self.LogInfo("Attached output file " + filename)    
    
################################################################################
def main():
    """This is a simple test script to evaluate the PyWPS - GrassModuleStarter 
    wrapper. """
    
    # Create a complex input for v.voronoi
    identifier = "input"
    title = "Name of input vector map"
    minOccurs = 1
    maxOccurs = 1
    format = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}]
    
    input = PyWPSComplexInput(identifier=identifier, minOccurs=minOccurs, maxOccurs=maxOccurs, title=title,formats=format)
    
    # The data is an GML file
    data = '<?xml version=\'1.0\' encoding="UTF-8" ?>\n<wfs:FeatureCollection\n   xmlns:ms="http://mapserver.gis.umn.edu/mapserver"\n   xmlns:gml="http://www.opengis.net/gml"\n   xmlns:wfs="http://www.opengis.net/wfs"\n   xmlns:ogc="http://www.opengis.net/ogc"\n   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n   xsi:schemaLocation="http://mapserver.gis.umn.edu/mapserver http://carto.languedoc-roussillon.ecologie.gouv.fr/final/mapjax/webservices//wfs/diren_general/?SERVICE=WFS&amp;VERSION=1.1.0&amp;REQUEST=DescribeFeatureType&amp;TYPENAME=Znieff1&amp;OUTPUTFORMAT=text/xml; subtype=gml/3.1.1  http://www.opengis.net/wfs http://schemas.opengis.net/wfs/1.1.0/wfs.xsd">\n      <gml:boundedBy>\n      \t<gml:Envelope srsName="EPSG:27572">\n      \t\t<gml:lowerCorner>549421.218052 1703199.993069</gml:lowerCorner>\n      \t\t<gml:upperCorner>801405.118492 1990265.823167</gml:upperCorner>\n      \t</gml:Envelope>\n      </gml:boundedBy>\n    <gml:featureMember>\n      <ms:Znieff1 gml:id="Znieff1.11">\n        <gml:boundedBy>\n        \t<gml:Envelope srsName="EPSG:27572">\n        \t\t<gml:lowerCorner>609360.619377 1818923.090409</gml:lowerCorner>\n        \t\t<gml:upperCorner>610176.568795 1821136.189945</gml:upperCorner>\n        \t</gml:Envelope>\n        </gml:boundedBy>\n        <ms:msGeometry>\n          <gml:Polygon srsName="EPSG:27572">\n            <gml:exterior>\n              <gml:LinearRing>\n                <gml:posList srsDimension="2">609953.620527 1821125.764306 609965.191840 1821108.579188 609962.785923 1821078.562515 609926.353472 1820970.067135 609934.373194 1820864.206806 610055.012725 1820718.018733 610123.294928 1820567.706231 610176.568795 1820321.844472 610050.773729 1820223.087325 609975.159208 1820044.247527 609905.158493 1819973.788542 609899.659255 1819809.269676 609805.943077 1819640.511814 609724.141913 1819393.962650 609689.198840 1819211.456694 609673.961368 1818923.090409 609578.182975 1818958.377185 609490.997142 1819035.939352 609490.768007 1819106.054635 609437.494140 1819307.349654 609360.619377 1819403.930019 609387.199027 1819438.529391 609475.186833 1819455.485374 609546.447790 1819476.222083 609631.571409 1819562.033108 609717.153299 1819805.947220 609820.951413 1819995.212656 609932.310980 1820195.820271 609936.549976 1820385.887679 609869.298879 1820597.264635 609799.985569 1820691.439083 609692.635863 1820749.639350 609638.560024 1820859.165838 609621.374906 1820979.003396 609699.968180 1821106.860676 609768.823221 1821123.816660 609845.239714 1821127.826521 609918.219183 1821136.189945 609953.620527 1821125.764306 609953.620527 1821125.764306 </gml:posList>\n              </gml:LinearRing>\n            </gml:exterior>\n          </gml:Polygon>\n        </ms:msGeometry>\n        <ms:toponyme>Ar\xc3\xaate rocheuse de Fount-Ferrouzo</ms:toponyme>\n        <ms:id>4085-0010</ms:id>\n        <ms:surface_sig_ha>46.5860506579831</ms:surface_sig_ha>\n      </ms:Znieff1>\n    </gml:featureMember>\n</wfs:FeatureCollection>\n\n'

    # Set the value
    input.storeData(data)
    
    inputs= {}
    inputs[identifier] = input
    
    # Create the complex output for v.voronoi
    identifier = "output"
    title = "Name of output vector map"
    format = [{'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/2.1.2/feature.xsd', 'encoding': 'UTF-8'}]
    
    output = PyWPSComplexOutput(identifier=identifier, title=title,formats=format)
    
    outputs = {}
    outputs[identifier] = output

    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.voronoi", inputs, outputs)
    
    print outputs[identifier].value
    
    exit(0)

###############################################################################
if __name__ == "__main__":
    main()
