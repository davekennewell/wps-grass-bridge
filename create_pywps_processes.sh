# Convert all XML process descriptions into PyWPS processes
echo -n "__all__ = [" > __init__.py
for name in `find gms/Testing/Python/ -name \*.xml` ; do
	echo "convert $name into `basename $name .xml `"
	script=`basename $name .xml | sed -e s/\\\./_/g`
	python GrassXMLtoPyWPS.py -x $name -p ${script}.py
	echo -n "\"$script\", " >> __init__.py
done
echo "]">> __init__.py 

#python GrassXMLtoPyWPS.py -x gms/Testing/Python/r.univar.xml -p r_univar.py
#python GrassXMLtoPyWPS.py -x gms/Testing/Python/r.univar.xml -p r_univar.py
#python GrassXMLtoPyWPS.py -x gms/Testing/Python/r.math.xml -p r_math.py
#python GrassXMLtoPyWPS.py -x gms/Testing/Python/r.watershed.xml -p r_watershed.py
#python GrassXMLtoPyWPS.py -x gms/Testing/Python/v.buffer.xml -p v_buffer.py
#python GrassXMLtoPyWPS.py -x gms/Testing/Python/v.to.rast.xml -p v_to_rast.py
#python GrassXMLtoPyWPS.py -x gms/Testing/Python/v.voronoi.xml -p v_voronoi.py


