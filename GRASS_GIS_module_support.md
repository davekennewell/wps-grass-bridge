#This page describes which GRASS GIS 7 modules are supported by wps-grass-bridge

# Overview #

The wps-grass-bridge is designed to support most of the raster and vector processing modules out of the box. The wps-grass-bridge approach is very strong coupled on the WPS XML process description generation mechanism of GRASS GIS 7. For each module in GRASS a valid XML process description document can be generated which is the base for the generation of ZOO WPS and PyWPS processes.

# Supported modules #

## Raster r.`*` ##

Most raster modules are supported, if they have no multiple outputs or non standard (other than raster, vector, text) inputs. Single and multiple inputs are supported. In case of single inputs and multichannel input data, a band number must be specified. Mixed multiple and single inputs are possible, but a band number must be specified. In case of modules which support only multiple inputs (r.univar) multichannel input data will be accepted without the specification of a band number.

Using import and output raster modules (r.in.`*` and r.out.`*`) should be avoided.

Modules which print there output to stdout are supported. The stdout will be logged and send as mime type plain/text in the response.

## Vector v.`*` ##

Most vector modules are supported, if they have no multiple outputs or non standard (other than raster, vector, text) inputs.

## Imagery i.`*` ##

Most imagery modules are supported, if they have no multiple outputs or non standard (other than raster, vector, text) inputs. Imagery modules which only accept grouped data (groups in grass) are currently not supported. Supporting such modules can be implemented using a wrapper script, which has multiple raster inputs.

# Unsupported modules #

## Raster3d [r3](https://code.google.com/p/wps-grass-bridge/source/detail?r=3).`*` ##

Support for 3d raster maps is currently not available. It can be implemented using multilevel tiff files or other data formats (HDF5) which support 3d pixel.

## General g.`*` ##

WPS Processes for general modules can be generated and will work, but they should not be used, because they offer GRASS GIS specific information's which not relevant for WPS services.

## Display d.`*` ##

Not supported.

## Database db.`*` ##

Not supported.