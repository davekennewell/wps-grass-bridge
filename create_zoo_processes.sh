#!/bin/sh
# Convert all XML process descriptions into ZOO YAML processes
for name in `find gms/Testing/Python/XML -name \*.xml` ; do
	echo "convert $name into `basename $name .xml `"
	script=`basename $name .xml | sed -e s/\\\./_/g`
	# python GrassXMLtoYAML.py -x $name -y zoo_services/${script}.yaml -p zoo_services/${script}.py
	python GrassXMLtoZCFG.py -x $name -z zoo_services/${script}.zcfg -p zoo_services/${script}.py
done

#echo "r.add.xml to r_add.zcfg"
#python GrassXMLtoZCFG.py -x gms/Testing/Python/r.add.xml -z r_add.zcfg -p r_add.py
#echo "r.sub.xml to r_sub.zcfg"
#python GrassXMLtoZCFG.py -x gms/Testing/Python/r.sub.xml -z r_sub.zcfg -p r_sub.py
#echo "r.div.xml to r_div.zcfg"
#python GrassXMLtoZCFG.py -x gms/Testing/Python/r.div.xml -z r_div.zcfg -p r_div.py
#echo "r.mult.xml to r_mult.zcfg"
#python GrassXMLtoZCFG.py -x gms/Testing/Python/r.mult.xml -z r_mult.zcfg -p r_mult.py
#echo "r.watershed.xml to r_watershed.zcfg"
#python GrassXMLtoZCFG.py -x gms/Testing/Python/r.watershed.xml -z r_watershed.zcfg -p r_watershed.py
#echo "r.univar.xml to r_univar.zcfg"
#python GrassXMLtoZCFG.py -x gms/Testing/Python/r.univar.xml -z r_univar.zcfg -p r_univar.py
#echo "r.neighbors.xml to r_neighbors.zcfg"
#python GrassXMLtoZCFG.py -x gms/Testing/Python/r.neighbors.xml -z r_neighbors.zcfg -p r_neighbors.py
#echo "r.contour.xml to r_contour.zcfg"
#python GrassXMLtoZCFG.py -x gms/Testing/Python/r.contour.xml -z r_contour.zcfg -p r_contour.py
#echo "v.buffer.xml to v_buffer.zcfg"
#python GrassXMLtoZCFG.py -x gms/Testing/Python/v.buffer.xml -z v_buffer.zcfg -p v_buffer.py
#echo "v.voronoi.xml to v_voronoi.zcfg"
#python GrassXMLtoZCFG.py -x gms/Testing/Python/v.voronoi.xml -z v_voronoi.zcfg -p v_voronoi.py
#echo "v.to.rast.xml to v_to_rast.zcfg"
#python GrassXMLtoZCFG.py -x gms/Testing/Python/v.to.rast.xml -z v_to_rast.zcfg -p v_to_rast.py
#echo "v.patch.xml to v_patch.zcfg"
#python GrassXMLtoZCFG.py -x gms/Testing/Python/v.patch.xml -z v_patch.zcfg -p v_patch.py
#echo "v.sample.xml to v_sample.zcfg"
#python GrassXMLtoZCFG.py -x gms/Testing/Python/v.sample.xml -z v_sample.zcfg -p v_sample.py
#echo "v.hull.xml to v_hull.zcfg"
#python GrassXMLtoZCFG.py -x gms/Testing/Python/v.hull.xml -z v_hull.zcfg -p v_hull.py
#echo "v.delaunay.xml to v_delaunay.zcfg"
#python GrassXMLtoZCFG.py -x gms/Testing/Python/v.delaunay.xml -z v_delaunay.zcfg -p v_delaunay.py
