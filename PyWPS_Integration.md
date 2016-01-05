# Installation and usage of wps-grass-bridge with PyWPS and GRASS GIS 7

# Introduction #

The wps-grass-bridge is designed to make the integration of GRASS GIS 7 in WPS server as easy as possible. Especially for PyWPS a generic approach has been implemented to attach most of the existing and future raster and vector processing modules to PyWPS out of the box.

It is only tested on OpenSuse Linux 11.1 and 11.2 on 32Bit and 64Bit. Other operating systems are currently not supported.

Informations what kind of GRASS GIS modules are supported are available here: http://code.google.com/p/wps-grass-bridge/wiki/GRASS_GIS_module_support

# Installation #

The wps-grass-bridge depends on GRASS GIS 7 trunk, PyWPS trunk and PyXB 1.1.2.
Please use always the latest svn versions of PyWPS and GRASS GIS 7, booth projects are under active development.

## Overview ##

The general principle is

  1. Install GRASS GIS trunk version 7 and PyWPS trunk via svn
  1. Install PyXB, which is needed to generate the PyWPS processes
  1. Download the wps-grass-bridge via svn
  1. Modify the GlobalGrassSettings.py script and test the PyWPSGrassModuleStarter.py
  1. Create the XML process description for each GRASS GIS module which should be attached
  1. Based on the XML files generate the PyWPS processes with GrassXMLtoPyWPS.py
  1. Put the wps-grass-bridge and the generated processes into a PyWPS process directory

### GRASS GIS 7 trunk installation ###

The wps-grass-bridge is based on the latest GRASS GIS 7 version, which is available as svn download. Download GRASS GIS 7 via svn into your development folder:
```
svn checkout https://svn.osgeo.org/grass/grass/trunk grass_trunk
```

Follow these compilation instruction:
http://grass.osgeo.org/wiki/Compile_and_Install

Only compilation is needed. GRASS GIS 7 must not be installed, it will run perfectly after compilation from the dist directory.

### PyWPS trunk installation ###

PyWPS ships a very nice documentation, which describes detailed how to install, configure and use PyWPS. The documentation is available here:
http://pywps.wald.intevation.org/documentation/index.html

### PyXB 1.1.2 Installation ###

To generate PyWPS processes PyXB 1.1.2 is needed to parse the GRASS GIS XML WPS process description files.

Download PyXB version 1.1.2 here: http://sourceforge.net/projects/pyxb/

To install PyXB follow the install instructions located here:
http://pyxb.sourceforge.net/overview_how.html
Make sure PyXB is located in your PYTHONPATH after installation.

### wps-grass-bridge installation ###

The wps-grass-bridge can only be downloaded via svn. Building or installation is not supported/needed. To download the wps-grass-bridge please use [revision 82](https://code.google.com/p/wps-grass-bridge/source/detail?r=82), switch into your development directory and type:

```
svn checkout http://wps-grass-bridge.googlecode.com/svn/trunk/ wps-grass-bridge-read-only -r82
```

The wps-grass-bridge including tests and test data will be downloaded.

# How to generate and use GRASS GIS processes #

All python scripts you need are located in wps-grass-bridge-read-only directory. The PyWPSGrassModuleStarter.py implements the connection between PyWPS and GRASS GIS. It is derived from GrassModuleStarter which is located in the gms directory.

To run the PyWPSGrassModuleStarter.py you need to modify the GlobalGrassSetting.py file. The following mostly self explaining variables must be set correctly:

```
WORKDIR="/tmp"
OUTPUTDIR="/tmp"
LOGFILE="/tmp/logfile.txt"
LOGFILE_MODULE_STDOUT="/tmp/logfile_module_stdout.txt"
LOGFILE_MODULE_STDERR="/tmp/logfile_module_sterr.txt"
GRASS_GIS_BASE="/home/soeren/src/grass7.0/grass_trunk/dist.x86_64-unknown-linux-gnu"
GRASS_ADDON_PATH="gms/Testing/Python/GrassAddons"
GRASS_VERSION="7.0.svn"
```

Make sure the log files are accessible by your web server. The WORKDIR is used to create the temporally GRASS GIS locations, based on the first complex raster or vector input. All results are stored as files in the OUTPUTDIR.

The PyWPSGrassModuleStarter includes a test which is automatically started if you execute the script in the command line. To start the PyWPSGrassModuleStarter make sure PyWPS is in your PYTHONPATH and all GRASS GIS relevant variables are set in GlobalGrassSetting.py, then type:
```
python PyWPSGrassModuleStarter.py
```

This will start the test by executing v.voronoi. When successfully finished the path to a generated GML file is printed to stdout.

## XML process description generation ##

You can create valid XML process descriptions in any valid GRASS GIS location. Start grass7 and switch to the GRASS GIS shell. To generate the XML process description for r.univar just type:
```
r.univar --wps-process-description > /tmp/r.univar.xml
```

## PyWPS process generation ##

Based on the class GrassModuleStarter, which hides all the GRASS GIS overhead, a class named PyWPSGrassModuleStarter has been implemented which is used by all automatically generated PyPWS processes.
To generate PyPWS processes the GrassXMLtoPyWPS.py script was implemented. Before you can use this script, make sure PyXB version 1.1.2 is in your PYTHONPATH.

Run the generator with the generated XML process description:
```
python GrassXMLtoPyWPS.py -x /tmp/r.univar.xml -p r_univar.py
```

To generate many processes at once be sure you are in a valid grass 7 session and in the wps-grass-bridge-read-only directory. Then execute the following commands:
```
cd gms/Testing/Python/XML
sh create_xml.sh
cd -
sh create_pywps_processes.sh 
```

Now a lot processes should be created in the pywps\_services directory as well as an init.py file. In the init.py file the last comma must be removed.

## Attaching the processes ##

Put the content of wps-grass-bridge-read-only and all generated processes you need into a PyWPS process directory. Add all processes to your init.py file in your process directory and make sure a pywps.cfg is present and correctly configured.

Use a wrapper script in your cgi-bin directory to set the process path and PyWPS PYTHONPATH like:

```
#!/usr/bin/sh

export PYTHONPATH="/home/soeren/src/pywps-trunk/trunk/":$PYTHONPATH
export PYWPS_CFG=/home/soeren/src/pywps-trunk/trunk/pywps/etc/pywps.cfg
export PYWPS_PROCESSES=/home/soeren/src/wps-grass-bridge

python /home/soeren/src/pywps-trunk/trunk/wps.py
```

## WPS clients ##

To use a WPS service you will need a client. There are several clients (mostly web clients) available in the internet (PyWPS, 52North, ZOO WPS, ...). There is also a very nice WPS plugin for QGIS implemented from Horts Düster. The plugin is available here: http://pyqgis.org/repo/contributed

# Result #

<a href='http://www.youtube.com/watch?feature=player_embedded&v=zCnax9w1bCs' target='_blank'><img src='http://img.youtube.com/vi/zCnax9w1bCs/0.jpg' width='800' height=600 /></a>