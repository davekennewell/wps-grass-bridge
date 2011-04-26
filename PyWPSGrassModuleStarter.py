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

from gms.ErrorHandler import GMSError
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
    def fromPyWPS(self, grassModule, inputs, outputs, pywps):
       
        self._grassModule = grassModule
        self._inputs = inputs
        self._outputs = outputs
        self._pywps = pywps
        
        # Initiate the logging mechanism and the logfiles
        ModuleLogging.__init__(self, GlobalGrassSettings.LOGFILE, GlobalGrassSettings.LOGFILE_MODULE_STDOUT, GlobalGrassSettings.LOGFILE_MODULE_STDERR)

        # Parse the input parameter of the text file
        self.inputParameter = InputParameter(self.logfile)
        # Initiate the input parameter for the GrassModuleStarter
        self._setInputParameterInit()
        
        # Some debug stuff
        # self.LogInfo(str(self._pywps.inputs))

        # Parse the PyWPS input and output data
        self._parsePyWPSInputsAndOutputs()
        
        try:
            self._createOutputFiles()
            self._createInputOutputMaps()
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
    def _parsePyWPSInputsAndOutputs(self):
        
        # Double for loop to identify requested inputs
        for datainput in self._pywps.inputs["datainputs"]: # list
            for input in self._inputs: # dict
                # Identify requested inputs
                if self._inputs[input].identifier != datainput["identifier"]:
                    continue
                else:
                    message = "Add requested input with identifier \"" + datainput["identifier"] + "\""
                    self.LogInfo(message)
                    
                # Check for literal inputs
                if isinstance(self._inputs[input], PyWPSLiteralInput):
                    # Attach only when not empty
                    if self._inputs[input].getValue() != None:
                        data = LiteralData()
                        data.identifier = self._inputs[input].identifier

                        # Store the value
                        data.value = str(self._inputs[input].getValue())

                        # In case an array is attached, store the values as comma 
                        # separated list
                        if type(self._inputs[input].getValue()) == type([]):
                            data.value = ""
                            count = 0
                            size = len(self._inputs[input].getValue())
                            for i in self._inputs[input].getValue():
                                data.value += str(i)
                                if count > 0 and count < size - 1:
                                    data.value += ","
                                count += 1

                        #check for double, integer, boolean, string
                        if self._inputs[input].dataType is IntType:
                            data.type = "integer"
                        elif self._inputs[input].dataType is FloatType:
                            data.type = "double"
                        elif self._inputs[input].dataType is StringType:
                            data.type = "string"
                        elif self._inputs[input].dataType is BooleanType:
                            # Override the stored value
                            data.type = "boolean"
                            if self._inputs[input].getValue() == False:
                                data.value = "False"
                            elif self._inputs[input].getValue() == True:
                                data.value = "True"
                            else:
                                data.value = "False"
                        else:
                            data.type = "string"

                        self.inputParameter.literalDataList.append(data)
                        self.LogInfo("Added literal input " + data.identifier + " with value " + str(data.value) + " of type " + str(type(data.value)))

                # Check for complex data
                
                elif isinstance(self._inputs[input], PyWPSComplexInput):
                    if  self._inputs[input].getValue() != None:
                        # Check for multiple complex inputs
                        if type(self._inputs[input].getValue()) == type([]):
                            for path in self._inputs[input].getValue():
                                data = ComplexData()
                                data.identifier = self._inputs[input].identifier
                                data.pathToFile = path
                                data.maxOccurs = self._inputs[input].maxOccurs
                                # Check for mime types
                                try:
                                    data.mimeType = self._inputs[input].format["mimetype"]
                                except:
                                    try:
                                        data.mimeType = self._inputs[input].format["mimeType"]
                                    except:
                                        log = "Missing mimeType in input " + str(input)
                                        self.LogError(log)
                                        raise GMSError(log)
                                try:
                                    # schema and encoding are not mandatory
                                    if self._inputs[input].format.has_key("schema"):
                                        data.schema = self._inputs[input].format["schema"]
                                    else:
                                        self.LogWarning("Missing schema")
                                    if self._inputs[input].format.has_key("encoding"):
                                        data.encoding = self._inputs[input].format["encoding"]
                                    else:
                                        self.LogWarning("Missing schema")
                                except:
                                    pass
                                
                                self.inputParameter.complexDataList.append(data)
                                self.LogInfo("Added complex input " + data.identifier + " with file path " + data.pathToFile)
                              
                        # Single complex input
                        else:
                            
                            data = ComplexData()
                            data.identifier = self._inputs[input].identifier
                            data.pathToFile =  self._inputs[input].getValue()
                            data.maxOccurs = self._inputs[input].maxOccurs
                            # Check for mime types                        
                            try:
                                data.mimeType = self._inputs[input].format["mimetype"]
                            except:
                                try:
                                    data.mimeType = self._inputs[input].format["mimeType"]
                                except:
                                    log = "Missing mimetype in input " + str(input)
                                    self.LogError(log)
                                    raise GMSError(log)
                            try:
                                # schema and encoding are not mandatory 
                                if self._inputs[input].format.has_key("schema"):
                                    data.schema = self._inputs[input].format["schema"]
                                else:
                                    self.LogWarning("Missing schema")
                                if self._inputs[input].format.has_key("encoding"):
                                    data.encoding = self._inputs[input].format["encoding"]
                                else:
                                    self.LogWarning("Missing schema")
                            except:
                                pass
                            self.inputParameter.complexDataList.append(data)
                            self.LogInfo("Added complex input " + data.identifier + " with file path " + data.pathToFile)

        # Attach all requested outputs
        # jmdj: A responsedocument with outputs is not mandatory in WPS requests.
        # If no ouputs are present we will assume the default mimeTypes and structure from the process it self
        try:
            outputList = self._pywps.inputs["responseform"]["responsedocument"]["outputs"]
            # may happen that responsedocument has some content inside
            if outputList == []:
                raise
            
            # if no exception raise then continue to loop:
            for output in outputList:
                data = ComplexOutput()
                data.identifier = output["identifier"]
                try:
                    data.mimeType = output["mimetype"]
                except:
                    log = "Missing mimeType in output " + str(output)
                    self.LogError(log)
                    raise GMSError(log)
                try:
                    # schema and encoding are not mandatory
                    data.schema = output["schema"]
                    data.encoding = output["encoding"]
                except:
                    self.LogWarning("Missing schema and encoding")
                    pass
              
                self.inputParameter.complexOutputList.append(data)
                self.LogInfo("Added complex output " + data.identifier + " of format " + data.mimeType)
             
        except:
             # Making outputs to have the same attributes as self._pywps.inputs
             outputList=self._outputs.values()
             # Making outputs to have the same attributes as self._pywps.inputs
             # for output in outputList:
             for output in outputList:
                data = ComplexOutput()
                data.identifier = output.identifier
                try:
                    data.mimeType = output.format["mimetype"]
                except:
                    log = "Missing mimeType in output from process" + str(output)
                    self.LogError(log)
                    raise GMSError(log)
                try:
                # schema and encoding are not mandatory
                # self_outputs.values() contains a "schema" key with None, false positive.
                    if type(output.format["schema"]) is not NoneType:
                        data.schema = output.format["schema"]
                        data.encoding = output.format["encoding"]
                except:
                    self.LogWarning("Missing schema and encoding from process")
                    pass
                self.inputParameter.complexOutputList.append(data)
                self.LogInfo("Added complex output " + data.identifier + " of format " + data.mimeType)
            
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
            filename = tempfile.mkstemp(prefix=output.identifier + "_" + str(count),dir=GlobalGrassSettings.OUTPUTDIR)
            output.pathToFile= filename[1]
            # No need to let the file open
            os.close(filename[0])
            self.LogInfo("Created output filename " + filename[1])
            count = count + 1

    ############################################################################
    def _passOutputs(self):
        for output in self.inputParameter.complexOutputList:
            filename = str(output.pathToFile)
            
            try:
                self._outputs[output.identifier].setValue(filename)
            except:
                self.LogError("Unable to attach output file")
                raise
            self.LogInfo("Attached output file " + filename)  

################################################################################
# Code for testing #############################################################
################################################################################

# We emulate the PyWPS inputs dict structure for testing
class pywps_inputs:
    def __init__(self):
        self.inputs = {'responseform': {'rawdataoutput': {}, 'responsedocument': {'lineage': False, 'status': False, 'storeexecuteresponse': True, 'outputs': [{'mimetype': u'text/xml', 'encoding': '', 'asreference': True, 'identifier': u'output', 'uom': '', 'schema': u'http://schemas.opengis.net/gml/2.1.2/feature.xsd'}]}}, 'service': 'wps', 'language': 'en-CA', 'request': 'execute', 'version': u'1.0.0', 'datainputs': [{'mimetype': u'text/xml', 'encoding': '', 'value': u'<ogr:FeatureCollection xmlns:gml="http://www.opengis.net/gml" xmlns:ogr="http://ogr.maptools.org/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://schemas.opengis.net/gml/3.1.1/base/ gml.xsd"><gml:boundedBy><gml:Box><gml:coord><gml:X>631431.2732342008</gml:X><gml:Y>217051.3475836431</gml:Y></gml:coord><gml:coord><gml:X>643603.8568773235</gml:X><gml:Y>225781.1802973978</gml:Y></gml:coord></gml:Box></gml:boundedBy><gml:featureMember><ogr:qt_temp fid="F0"><ogr:geometryProperty><gml:Point><gml:coordinates>631571.793680297443643,225728.485130111512262</gml:coordinates></gml:Point></ogr:geometryProperty><ogr:height>10</ogr:height></ogr:qt_temp></gml:featureMember><gml:featureMember><ogr:qt_temp fid="F1"><ogr:geometryProperty><gml:Point><gml:coordinates>635752.276951672858559,225113.708178438653704</gml:coordinates></gml:Point></ogr:geometryProperty><ogr:height>20</ogr:height></ogr:qt_temp></gml:featureMember><gml:featureMember><ogr:qt_temp fid="F2"><ogr:geometryProperty><gml:Point><gml:coordinates>640898.838289962848648,225781.180297397775576</gml:coordinates></gml:Point></ogr:geometryProperty><ogr:height>40</ogr:height></ogr:qt_temp></gml:featureMember><gml:featureMember><ogr:qt_temp fid="F3"><ogr:geometryProperty><gml:Point><gml:coordinates>643603.856877323472872,221319.65613382900483</gml:coordinates></gml:Point></ogr:geometryProperty><ogr:height>60</ogr:height></ogr:qt_temp></gml:featureMember><gml:featureMember><ogr:qt_temp fid="F4"><ogr:geometryProperty><gml:Point><gml:coordinates>640038.1505576208001,217999.860594795551151</gml:coordinates></gml:Point></ogr:geometryProperty><ogr:height>50</ogr:height></ogr:qt_temp></gml:featureMember><gml:featureMember><ogr:qt_temp fid="F5"><ogr:geometryProperty><gml:Point><gml:coordinates>633047.258364312234335,217051.347583643131657</gml:coordinates></gml:Point></ogr:geometryProperty><ogr:height>40</ogr:height></ogr:qt_temp></gml:featureMember><gml:featureMember><ogr:qt_temp fid="F6"><ogr:geometryProperty><gml:Point><gml:coordinates>635471.236059479531832,220599.488847583648749</gml:coordinates></gml:Point></ogr:geometryProperty><ogr:height>25</ogr:height></ogr:qt_temp></gml:featureMember><gml:featureMember><ogr:qt_temp fid="F7"><ogr:geometryProperty><gml:Point><gml:coordinates>631431.27323420078028,222443.819702602224424</gml:coordinates></gml:Point></ogr:geometryProperty><ogr:height>20</ogr:height></ogr:qt_temp></gml:featureMember></ogr:FeatureCollection>', 'identifier': u'input', 'type': 'ComplexValue', 'schema': u'http://schemas.opengis.net/gml/2.1.2/feature.xsd'}, {'dataType': '', 'identifier': u'-t', 'value': False, 'uom': ''}, {'dataType': '', 'identifier': u'-l', 'value': False, 'uom': ''}], 'identifier': [u'v.voronoi']}


################################################################################
# Main function to start the v.voronoi test
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
    # The PyWPS request dict structure
    requests = pywps_inputs()
    # The first input
    data = requests.inputs["datainputs"][0]["value"]
    input.setMimeType(requests.inputs["datainputs"][0])
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

    # Start the GRASS process
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("v.voronoi", inputs, outputs, requests)
    
    print "Generated GML output is located here: ", outputs[identifier].value
    
    exit(0)

###############################################################################
if __name__ == "__main__":
    main()
