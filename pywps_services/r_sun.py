# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class r_sun(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'r.sun', title = 'Computes direct (beam), diffuse and reflected solar irradiation raster maps for given day, latitude, surface and atmospheric conditions. Solar parameters (e.g. sunrise, sunset times, declination, extraterrestrial irradiance, daylight length) are saved in the map history file. Alternatively, a local time can be specified to compute solar incidence angle and/or irradiance raster maps. The shadowing effect of the topography is optionally incorporated.', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'raster'}, {'type': 'simple', 'title': 'solar'}, {'type': 'simple', 'title': 'sun energy'}], abstract = 'http://grass.osgeo.org/grass70/manuals/html70_user/r.sun.html')

    # Literal and complex inputs
    self.addComplexInput(identifier = 'elevin', title = 'Name of the input elevation raster map [meters]', minOccurs = 1, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addComplexInput(identifier = 'aspin', title = 'Name of the input aspect map (terrain aspect or azimuth of the solar panel) [decimal degrees]', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = 'aspect', title = 'A single value of the orientation (aspect), 270 is south', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 270.0)
    self.addComplexInput(identifier = 'slopein', title = 'Name of the input slope raster map (terrain slope or solar panel inclination) [decimal degrees]', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = 'slope', title = 'A single value of inclination (slope)', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.0)
    self.addComplexInput(identifier = 'linkein', title = 'Name of the Linke atmospheric turbidity coefficient input raster map [-]', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = 'lin', title = 'A single value of the Linke atmospheric turbidity coefficient [-]', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 3.0)
    self.addComplexInput(identifier = 'albedo', title = 'Name of the ground albedo coefficient input raster map [-]', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = 'alb', title = 'A single value of the ground albedo coefficient [-]', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.2)
    self.addComplexInput(identifier = 'latin', title = 'Name of input raster map containing latitudes [decimal degrees]', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addComplexInput(identifier = 'longin', title = 'Name of input raster map containing longitudes [decimal degrees]', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addComplexInput(identifier = 'coefbh', title = 'Name of real-sky beam radiation coefficient (thick cloud) input raster map [0-1]', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addComplexInput(identifier = 'coefdh', title = 'Name of real-sky diffuse radiation coefficient (haze) input raster map [0-1]', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addComplexInput(identifier = 'horizon', title = 'The horizon information input map prefix', minOccurs = 0, maxOccurs = 1, formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'image/png'}, {'mimeType': 'image/gif'}, {'mimeType': 'image/jpeg'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])
    self.addLiteralInput(identifier = 'horizonstep', title = 'Angle step size for multidirectional horizon [degrees]', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'day', title = 'No. of day of the year (1-365)', minOccurs = 1, maxOccurs = 1, type = type(0), allowedValues = '*')
    self.addLiteralInput(identifier = 'step', title = 'Time step when computing all-day radiation sums [decimal hours]', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 0.5)
    self.addLiteralInput(identifier = 'declin', title = 'Declination value (overriding the internally computed value) [radians]', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'time', title = 'Local (solar) time (to be set for mode 1 only) [decimal hours]', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'dist', title = 'Sampling distance step coefficient (0.5-1.5)', minOccurs = 0, maxOccurs = 1, type = type(0.0), default = 1.0)
    self.addLiteralInput(identifier = 'numpartitions', title = 'Read the input files in this number of chunks', minOccurs = 0, maxOccurs = 1, type = type(0), default = 1)
    self.addLiteralInput(identifier = 'civiltime', title = 'Civil time zone value, if none, the time will be local solar time', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = '-s', title = 'Incorporate the shadowing effect of terrain', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = '-m', title = 'Use the low-memory version of the program', minOccurs = 0, maxOccurs = 1, type = type(True), default = False, allowedValues = [True, False])
    self.addLiteralInput(identifier = 'grass_resolution_ns', title = 'Resolution of the mapset in north-south direction in meters or degrees', abstract = 'This parameter defines the north-south resolution of the mapset in meter or degrees, which should be used to process the input and output raster data. To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_resolution_ew', title = 'Resolution of the mapset in east-west direction in meters or degrees', abstract = 'This parameter defines the east-west resolution of the mapset in meters or degrees, which should be used to process the input and output raster data.  To enable this setting, you need to specify north-south and east-west resolution.', minOccurs = 0, maxOccurs = 1, type = type(0.0), allowedValues = '*')
    self.addLiteralInput(identifier = 'grass_band_number', title = 'Band to select for processing (default is all bands)', abstract = 'This parameter defines band number of the input raster files which should be processed. As default all bands are processed and used as single and multiple inputs for raster modules.', minOccurs = 0, maxOccurs = 1, type = type(0), allowedValues = '*')

    # complex outputs
    self.addComplexOutput(identifier = 'incidout', title = 'Output incidence angle raster map (mode 1 only)', formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])

    self.addComplexOutput(identifier = 'beam_rad', title = 'Output beam irradiance [W.m-2] (mode 1) or irradiation raster map [Wh.m-2.day-1] (mode 2)', formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])

    self.addComplexOutput(identifier = 'insol_time', title = 'Output insolation time raster map [h] (mode 2 only)', formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])

    self.addComplexOutput(identifier = 'diff_rad', title = 'Output diffuse irradiance [W.m-2] (mode 1) or irradiation raster map [Wh.m-2.day-1] (mode 2)', formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])

    self.addComplexOutput(identifier = 'refl_rad', title = 'Output ground reflected irradiance [W.m-2] (mode 1) or irradiation raster map [Wh.m-2.day-1] (mode 2)', formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])

    self.addComplexOutput(identifier = 'glob_rad', title = 'Output global (total) irradiance/irradiation [W.m-2] (mode 1) or irradiance/irradiation raster map [Wh.m-2.day-1] (mode 2)', formats = [{'mimeType': 'image/tiff'}, {'mimeType': 'image/geotiff'}, {'mimeType': 'application/geotiff'}, {'mimeType': 'application/x-geotiff'}, {'mimeType': 'application/x-erdas-hfa'}, {'mimeType': 'application/netcdf'}, {'mimeType': 'application/x-netcdf'}])

  def execute(self):
    starter = PyWPSGrassModuleStarter()
    starter.fromPyWPS("r.sun", self.inputs, self.outputs, self.pywps)

if __name__ == "__main__":
  process = r_sun()
  process.execute()
