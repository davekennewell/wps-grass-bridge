# Convert all XML process descriptions into PyWPS processes
echo -n "__all__ = [" > pywps_services/__init__.py
for name in `find gms/Testing/Python/XML/ -name \*.xml` ; do
	echo "convert $name into `basename $name .xml `"
	script=`basename $name .xml | sed -e s/\\\./_/g`
	python GrassXMLtoPyWPS.py -x $name -p pywps_services/${script}.py
	echo -n "\"$script\", " >> pywps_services/__init__.py
done
echo "]">> pywps_services/__init__.py 
