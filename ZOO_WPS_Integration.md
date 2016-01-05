# Installation and usage of wps-grass-bridge with ZOO WPS and GRASS GIS 7

# Introduction #

The wps-grass-bridge is designed to make the integration of GRASS GIS 7 in WPS server as easy as possible. Especially for ZOO WPS a generic approach has been implemented to attach most of the existing and future raster and vector processing modules to ZOO WPS out of the box. The approach is quite similiar to the one implemented for PyWPS.

There is (hopefully) no need to implement a single line of code to attach a grass module as WPS service. Everything is automatically generated and works with grass7.

# How does it work #

Based on a grass module WPS XML description, which must be generated for the module in gis grass7, a zcfg file and a python service file are generated. The generated zcfg file should work out of the box, but it can of course be modified to your needs.

The generated python service file instantiates an object of the class ZOOGrassModuleStarter, passing the input and output maps. This class is derived from GrassModuleStarter?, which is a framework to start gis grass modules based on external data.

The ZOOGrassModuleStarter will write the input data located in the input map to a temporary directory, so grass can import/link it. Then a gis grass location based on the first input is generated. Then the grass module will be executed and the result will be exported and written into the output map, so the zoo kernel can handle it.

Informations what kind of GRASS GIS modules are supported are available here: http://code.google.com/p/wps-grass-bridge/wiki/GRASS_GIS_module_support

# Installation #

The wps-grass-bridge depends on GRASS GIS 7 trunk, ZOO WPS trunk and PyXB 1.1.2.
Please use always the latest svn versions of the wps-grass-bridge, ZOO WPS and GRASS GIS 7, all projects are under active development.

## Overview ##

The general principle is

  1. Install GRASS GIS trunk version 7 and ZOO WPS trunk via svn
  1. Install PyXB, which is needed to generate the ZOO WPS processes and zcfg files
  1. Download the wps-grass-bridge via svn
  1. Modify the GlobalGrassSettings.py script
  1. Create the XML process description for each GRASS GIS module which should be attached
  1. Based on the XML files generate the ZOO WPS processes and zcfg files with GrassXMLtoZCFG.py
  1. Put the ZOOGrassModuleStarter.py, the gms directory and the generated processes into the ZOO WPS process directory

### GRASS GIS 7 trunk installation ###

The wps-grass-bridge is based on the latest GRASS GIS 7 version, which is available as svn download. Download GRASS GIS 7 via svn into your development folder:
```
svn checkout https://svn.osgeo.org/grass/grass/trunk grass_trunk
```

Follow these compilation instruction:
http://grass.osgeo.org/wiki/Compile_and_Install

Only compilation is needed. GRASS GIS 7 must not be installed, it will run perfectly after compilation from the dist directory.

### ZOO WPS trunk installation ###

The ZOO WPS installation process is very well documented. Just follow the installation instructions available here:
http://zoo-project.org/trac/wiki/ZooDocumentation/ZOOKernel

### PyXB 1.1.2 Installation ###

To generate ZOO WPS processes PyXB 1.1.2 is needed to parse the GRASS GIS XML WPS process description files to generate the zcfg and python service files. Because the wps-grass-bridge already ships many ZOO WPS processes and zcfg files PyXB is only needed if more recent or new processes should be generated.

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

All python scripts you need are located in wps-grass-bridge-read-only directory. The ZOOGrassModuleStarter implements the connection between ZOO WPS and GRASS GIS. It is derived from GrassModuleStarter which is located in the gms directory.

To run the ZOOGrassModuleStarter you need to modify the GlobalGrassSetting.py file. The following mostly self explaining variables must be set correctly:

```
WORKDIR="/tmp"
OUTPUTDIR="/tmp"
LOGFILE="/tmp/logfile.txt"
LOGFILE_MODULE_STDOUT="/tmp/logfile_module_stdout.txt"
LOGFILE_MODULE_STDERR="/tmp/logfile_module_sterr.txt"
GRASS_GIS_BASE="/home/soeren/src/grass7.0/grass_trunk/dist.x86_64-unknown-linux-gnu"
GRASS_ADDON_PATH="/home/soeren/src/wps-grass-bridge/gms/Testing/Python/GrassAddons"
GRASS_VERSION="7.0.svn"
```

Make sure the log files are accessible by your web server. The WORKDIR is used to create the temporally GRASS GIS locations, based on the first complex raster or vector input. All results are stored as files in the OUTPUTDIR.

## XML process description generation ##

You can create valid XML process descriptions in any valid GRASS GIS location. Start grass7 and switch to the GRASS GIS shell. To generate the XML process description for r.univar just type:
```
r.univar --wps-process-description > /tmp/r.univar.xml
```

## ZOO WPS process generation ##

To generate ZOO WPS processes the GrassXMLtoZCFG.py script was implemented. Before you can use this script, make sure PyXB version 1.1.2 is in your PYTHONPATH.

Run the generator with the generated XML process description:
```
python GrassXMLtoZCFG.py -x gms/Testing/Python/XML/r.univar.xml -z r_univar.zcfg -p r_univar.py
```

The wps-grass-bridge includes more then hundred generated ZOO WPS services in the zoo\_services directory.

To generate all these processes and zcfg files by hand make sure you are in a valid grass 7 session and in the wps-grass-bridge-read-only directory. Then execute the following commands:
```
cd gms/Testing/Python/XML
sh create_xml.sh
cd -
sh create_zoo_processes.sh 
```

Many processes should now be created in the zoo\_services directory.

## Attaching the processes ##

Put ZOOGrassModuleStarter.py, GlobalGrassSetting.py and the gms directory from the wps-grass-bridge-read-only directory and all generated processes you need into the ZOO WPS process directory. Make sure the main.cfg is present and correctly configured as well as a recent zoo\_loader.cgi executable.

In OpenSuse 11.2 the content of the /srv/www/cgi-bin directory to run two GRASS GIS processes may look like this:

```
-rw-r--r-- 1 wwwrun www    1583 27. Jan 10:43 GlobalGrassSettings.py
drwxr-xr-x 4 wwwrun www    4096 29. Apr 08:58 gms/
-rw-r--r-- 1 wwwrun www     712 27. Jan 10:36 main.cfg
-rw-r--r-- 1 wwwrun www     341 29. Apr 08:54 v_delaunay.py
-rw-r--r-- 1 wwwrun www    3305 29. Apr 08:54 v_delaunay.zcfg
-rw-r--r-- 1 wwwrun www     339 29. Apr 08:54 v_voronoi.py
-rw-r--r-- 1 wwwrun www    2979 29. Apr 08:54 v_voronoi.zcfg
-rw-r--r-- 1 wwwrun www   12706 29. Apr 08:54 ZOOGrassModuleStarter.py
-rwxr-xr-x 1 wwwrun www  354470 29. Apr 08:54 zoo_loader.cgi*
```

## WPS clients ##

To use a WPS service you will need a client. There are several clients (mostly web clients) available in the internet (ZOO WPS, PyWPS, 52North, ...). There is also a very nice WPS plugin for QGIS implemented from Horts Düster. The plugin is available here: http://pyqgis.org/repo/contributed