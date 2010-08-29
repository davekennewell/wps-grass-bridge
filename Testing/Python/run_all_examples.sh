#!/bin/sh

echo "Running module r.contour"
python ../../GrassModuleStarter.py -f r.contour_input.txt     -l 1.log  -o 1_stdout.log  -e 1_stderr.log
echo "Running module r.neighbors"
python ../../GrassModuleStarter.py -f r.neighbors_input.txt   -l 2.log  -o 2_stdout.log  -e 2_stderr.log
echo "Running module r.univar"
python ../../GrassModuleStarter.py -f r.univar2_input.txt     -l 3.log  -o 3_stdout.log  -e 3_stderr.log
echo "Running module r.univar"
python ../../GrassModuleStarter.py -f r.univar2_mc_input.txt  -l 4.log  -o 4_stdout.log  -e 4_stderr.log
echo "Running module r.univar"
python ../../GrassModuleStarter.py -f r.univar_input.txt      -l 5.log  -o 5_stdout.log  -e 5_stderr.log
echo "Running module r.univar"
python ../../GrassModuleStarter.py -f r.univar_mc_input.txt   -l 6.log  -o 6_stdout.log  -e 6_stderr.log
echo "Running module r.watershed"
python ../../GrassModuleStarter.py -f r.watershed_input.txt   -l 7.log  -o 7_stdout.log  -e 7_stderr.log
echo "Running module v.buffer"
python ../../GrassModuleStarter.py -f v.buffer_input.txt      -l 8.log  -o 8_stdout.log  -e 8_stderr.log
echo "Running module v.to.rast"
python ../../GrassModuleStarter.py -f v.to.rast_input.txt     -l 9.log  -o 9_stdout.log  -e 9_stderr.log
echo "Running module r.contour"
python ../../GrassModuleStarter.py -f r.contour_res_input.txt -l 10.log -o 10_stdout.log -e 10_stderr.log
echo "Running addon module r.add"
python ../../GrassModuleStarter.py -f r.add_input.txt         -l 11.log -o 11_stdout.log -e 11_stderr.log
echo "Running addon module r.sub"
python ../../GrassModuleStarter.py -f r.sub_input.txt         -l 12.log -o 12_stdout.log -e 12_stderr.log
echo "Running addon module r.mult"
python ../../GrassModuleStarter.py -f r.mult_input.txt        -l 13.log -o 13_stdout.log -e 13_stderr.log
echo "Running addon module r.div"
python ../../GrassModuleStarter.py -f r.div_input.txt         -l 14.log -o 14_stdout.log -e 14_stderr.log
echo "Running module r.neighbors producing an error"
python ../../GrassModuleStarter.py -f r.neighbors_error_input.txt   -l 15.log  -o 15_stdout.log  -e 15_stderr.log
echo "Running module v.voronoi"
python ../../GrassModuleStarter.py -f v.voronoi_input.txt     -l 16.log -o 16_stdout.log -e 16_stderr.log

