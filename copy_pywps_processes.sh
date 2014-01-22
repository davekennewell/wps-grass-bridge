#!/bin/sh
# This script copies all needed Python scripts into a PyWPS
# process directory, so that they are visible as PyWPS processes
# The GlobalGrassSettings.py must be edited to point to the correct paths
# call bash copy_pywps_processes.sh "Pathvto the pywps service directory"
# eg: bash copy_pywps_processes.sh /usr/local/lib/pywpsprocesses

PDIR=$1

if [ -z $1 ] ; then
       exit "Argument missing"
fi       

if [ ! -d "${PDIR}/Addons" ] ; then
	mkdir "${PDIR}/Addons"
fi
if [ ! -d "${PDIR}/gms" ] ; then
	mkdir "${PDIR}/gms"
fi

cp gms/*.py "${PDIR}/gms"
cp gms/Testing/Python/GrassAddons/* "${PDIR}/Addons"
cp pywps_services/*.py "${PDIR}/"
cp GlobalGrassSettings.py "${PDIR}/"
cp PyWPSGrassModuleStarter.py "${PDIR}/"
