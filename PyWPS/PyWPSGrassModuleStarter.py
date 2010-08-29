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



# !!!!! EDIT THIS SECTION !!!!!
# Some default variables. Override them to your needs.
WORKDIR="/tmp"
OUTPUTDIR="/tmp"
LOGFILE="logfile.txt"
LOGFILE_MODULE_STDOUT="logfile_module_stdout.txt"
LOGFILE_MODULE_STDERR="logfile_module_sterr.txt"
GRASS_GIS_BASE="/home/soeren/src/grass7.0/grass_trunk/dist.i686-pc-linux-gnu"
GRASS_ADDON_PATH="/home/soeren/src/vtkGRASSBridge/vtk-grass-bridge/WPS/Testing/Python/GrassAddons"
GRASS_VERSION="7.0.svn"
# !!!!! END EDIT SECTION !!!!!


import os.path
# Import the GrassModuleStarter
from GrassModuleStarter import *
# Import the WPS bindings
import WPS_1_0_0.OGC_WPS_1_0_0 as wps

class PyWPSGrassModuleStarter(GrassModuleStarter):
    """Start a grass module specified by ZOO-WPS server"""
    def __init__(self):
        GrassModuleStarter.__init__(self)

    ############################################################################
    def fromMaps(self, grassModule, inputs, outputs):

        self._grassModule = grassModule
        self._inputs = {}
        # Transfer the input values. The metadata is read separately from generated GRASS WPS XML files
	for key in inputs.keys():
            self._inputs[key] = inputs[key]["value"]

        self._outputs = outputs
        
        # Create the tmp working directory and initiate the logging functionality
        try:
            self._createTemporalDir(WORKDIR)

            logfile = os.path.join("/tmp", LOGFILE)
            module_stdout = os.path.join("/tmp", LOGFILE_MODULE_STDOUT)
            module_stderr = os.path.join("/tmp", LOGFILE_MODULE_STDERR)

#            logfile = os.path.join(self.gisdbase, LOGFILE)
#            module_stdout = os.path.join(self.gisdbase, LOGFILE_MODULE_STDOUT)
#            module_stderr = os.path.join(self.gisdbase, LOGFILE_MODULE_STDERR)
#            logfile = LOGFILE
#            module_stdout = LOGFILE_MODULE_STDOUT
#            module_stderr = LOGFILE_MODULE_STDERR

            ModuleLogging.__init__(self, logfile, module_stdout, module_stderr)

            #self.LogInfo(str(inputs))
            #self.LogInfo(str(outputs))
        except:
            print "ERROR: Unable to start logging. break"
            raise
        try:
            # Setup a temporary GRASS location to get the module XML WPS process description
            self._setInputParameterInit()
            self._setUpGrassLocation(self.inputParameter.grassGisBase, self.inputParameter.grassAddonPath)

            # Catch the XML process description of the input module
            inputlist = [self._createGrassModulePath(), "--wps-process-description"]
            error_code, stdout_buff, stderr_buff = self._runProcess(inputlist)
            #
            try:
                # Read the XML into a PyXB generated class hierarchy
                self._doc = wps.CreateFromDocument(stdout_buff)
                # Create the inner data structure for GrassModuleStarter
                self._parseXML()
                # Write the complex inputs into files
                self._createInputFiles()
                # Create the output file names
                self._createOutputFiles()

                # Check and attach the literal data
                for key in self._inputs.keys():
                    for ldata in self.inputParameter.literalDataList:
                        if ldata.identifier == key:
                            ldata.value = self._inputs[key]
            except:
                raise
            # Create input and output maps
            self._createMaps()
            # Import/link the data, run the module and export the data
            self._importRunExport()
            # Attach the results to the outputs list
            self._attachOutputFiles()
            # self.LogInfo(str(self._inputs))
            # self.LogInfo(str(outputs))
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
        self.inputParameter.grassGisBase = GRASS_GIS_BASE
        self.inputParameter.grassAddonPath = GRASS_ADDON_PATH
        self.inputParameter.grassVersion = GRASS_VERSION
        self.inputParameter.grassModule = self._grassModule

    ############################################################################
    def _createInputFiles(self):
        """Generate input file names and write the content of the input map into files on hard disk"""
        count = 0
        for input in self.inputParameter.complexDataList:
            filename = os.path.join(self.gisdbase, input.identifier + "_" + str(count))
            try:
                infile = open(filename, 'w')
                infile.write(self._inputs[input.identifier])
                infile.close()
            except:
                self.LogError("Unable to create input files")
                raise
            self._inputs[input.identifier] = filename
            input.pathToFile= filename
            self.LogInfo("Created input filename " + filename)
            count = count + 1
 
    ############################################################################
    def _createOutputFiles(self):
        """Create the output file names which are used to identify the outputs"""
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
    def _parseXML(self):
        """Parse the PyXB XML structure and fill the internal data structure with content"""
        try:
            if len(self._doc.ProcessDescription) > 1:
                raise IOError("Only one Process is supported")
            
            for process in self._doc.ProcessDescription:
	        self._getDataInputs(process)
	        self._getProcessOutputs(process)
        except:
            raise

    ############################################################################
    def _getDataInputs(self,  process):
        """Create data inputs"""
        for data in process.DataInputs.Input:
            input= None
            
            if data.ComplexData != None:
                input = self._getComplexData(data.ComplexData)
                if input:
                    input.maxOccurs = int(data.maxOccurs)
                    input.identifier = str(data.Identifier.value())
                    self.inputParameter.complexDataList.append(input)
                    #print "Added input", input.identifier
            if data.LiteralData != None:
                input= self._getLiteralData(data.LiteralData)
                if input:
                    input.maxOccurs = int(data.maxOccurs)
                    input.identifier = str(data.Identifier.value())
                    self.inputParameter.literalDataList.append(input)
                    #print "Added input", input.identifier

    ############################################################################
    def _getProcessOutputs(self,  process):
        """Create process outputs"""
        for data in process.ProcessOutputs.Output:
            output = None
                
            if data.ComplexOutput != None:
                output = self._getComplexData(data.ComplexOutput)
                output.identifier = str(data.Identifier.value())
                self.inputParameter.complexOutputList.append(output)
                #print "Added output", output.identifier

    ############################################################################
    def _getComplexData(self,  element):
        """Create complex data"""
        data = ComplexData()
       
        if element.Default.Format.MimeType != None:
            data.mimeType = str(element.Default.Format.MimeType)
        if element.Default.Format.Encoding != None:
            data.encoding = str(element.Default.Format.Encoding)
        if element.Default.Format.Schema != None:
            data.schema = str(element.Default.Format.Schema)

        return data

    ############################################################################
    def _getLiteralData(self,  element):
        """The literal data"""
        data = LiteralData()

        if element.DataType != None:
            data.type = str(element.DataType.value())

        return data

################################################################################
def main():
    # Simple test case
    inputs = {'input': {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.0/polygon.xsd', 'xlink:href': 'http://carto.languedoc-roussillon.ecologie.gouv.fr/webservices/wfs/diren_general/?VERSION=1.1.0&service=WFS&request=GetFeature&typename=Znieff1&maxfeatures=1', 'value': '<?xml version=\'1.0\' encoding="UTF-8" ?>\n<wfs:FeatureCollection\n   xmlns:ms="http://mapserver.gis.umn.edu/mapserver"\n   xmlns:gml="http://www.opengis.net/gml"\n   xmlns:wfs="http://www.opengis.net/wfs"\n   xmlns:ogc="http://www.opengis.net/ogc"\n   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n   xsi:schemaLocation="http://mapserver.gis.umn.edu/mapserver http://carto.languedoc-roussillon.ecologie.gouv.fr/final/mapjax/webservices//wfs/diren_general/?SERVICE=WFS&amp;VERSION=1.1.0&amp;REQUEST=DescribeFeatureType&amp;TYPENAME=Znieff1&amp;OUTPUTFORMAT=text/xml; subtype=gml/3.1.1  http://www.opengis.net/wfs http://schemas.opengis.net/wfs/1.1.0/wfs.xsd">\n      <gml:boundedBy>\n      \t<gml:Envelope srsName="EPSG:27572">\n      \t\t<gml:lowerCorner>549421.218052 1703199.993069</gml:lowerCorner>\n      \t\t<gml:upperCorner>801405.118492 1990265.823167</gml:upperCorner>\n      \t</gml:Envelope>\n      </gml:boundedBy>\n    <gml:featureMember>\n      <ms:Znieff1 gml:id="Znieff1.11">\n        <gml:boundedBy>\n        \t<gml:Envelope srsName="EPSG:27572">\n        \t\t<gml:lowerCorner>609360.619377 1818923.090409</gml:lowerCorner>\n        \t\t<gml:upperCorner>610176.568795 1821136.189945</gml:upperCorner>\n        \t</gml:Envelope>\n        </gml:boundedBy>\n        <ms:msGeometry>\n          <gml:Polygon srsName="EPSG:27572">\n            <gml:exterior>\n              <gml:LinearRing>\n                <gml:posList srsDimension="2">609953.620527 1821125.764306 609965.191840 1821108.579188 609962.785923 1821078.562515 609926.353472 1820970.067135 609934.373194 1820864.206806 610055.012725 1820718.018733 610123.294928 1820567.706231 610176.568795 1820321.844472 610050.773729 1820223.087325 609975.159208 1820044.247527 609905.158493 1819973.788542 609899.659255 1819809.269676 609805.943077 1819640.511814 609724.141913 1819393.962650 609689.198840 1819211.456694 609673.961368 1818923.090409 609578.182975 1818958.377185 609490.997142 1819035.939352 609490.768007 1819106.054635 609437.494140 1819307.349654 609360.619377 1819403.930019 609387.199027 1819438.529391 609475.186833 1819455.485374 609546.447790 1819476.222083 609631.571409 1819562.033108 609717.153299 1819805.947220 609820.951413 1819995.212656 609932.310980 1820195.820271 609936.549976 1820385.887679 609869.298879 1820597.264635 609799.985569 1820691.439083 609692.635863 1820749.639350 609638.560024 1820859.165838 609621.374906 1820979.003396 609699.968180 1821106.860676 609768.823221 1821123.816660 609845.239714 1821127.826521 609918.219183 1821136.189945 609953.620527 1821125.764306 609953.620527 1821125.764306 </gml:posList>\n              </gml:LinearRing>\n            </gml:exterior>\n          </gml:Polygon>\n        </ms:msGeometry>\n        <ms:toponyme>Ar\xc3\xaate rocheuse de Fount-Ferrouzo</ms:toponyme>\n        <ms:id>4085-0010</ms:id>\n        <ms:surface_sig_ha>46.5860506579831</ms:surface_sig_ha>\n      </ms:Znieff1>\n    </gml:featureMember>\n</wfs:FeatureCollection>\n\n', 'encoding': 'UTF-8'}, '-t': {'DataType': 'boolean', 'value': 'false'}, '-l': {'DataType': 'boolean', 'value': 'false'}}
    outputs = {'output': {'mimeType': 'text/xml', 'schema': 'http://schemas.opengis.net/gml/3.1.0/polygon.xsd', 'value': 'NULL', 'encoding': 'UTF-8'}}
    starter = PyWPSGrassModuleStarter()
    starter.fromMaps("v.voronoi", inputs, outputs)
    
    exit(0)

###############################################################################
if __name__ == "__main__":
    main()
