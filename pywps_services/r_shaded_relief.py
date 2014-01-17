# ################################################ #
# This process was generated using GrassXMLtoPyWPS #
# Author: Soeren Gebbert                           #
# Mail: soerengebbert <at> googlemail <dot> com    #
# ################################################ #

from pywps.Process import WPSProcess

from PyWPSGrassModuleStarter import PyWPSGrassModuleStarter

class r_shaded_relief(WPSProcess):

  def __init__(self):
    WPSProcess.__init__(self, identifier = 'r.shaded.relief', title = 'No title available', version = 1, statusSupported = True, storeSupported = True, metadata = [{'type': 'simple', 'title': 'raster'}, {'type': 'simple', 'title': 'elevation'}, {'type': 'simple', 'title': 'terrain'}], 