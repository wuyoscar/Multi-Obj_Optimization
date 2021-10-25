#! /bin/bash
while read -ra p
do for a in nsga2 nsga3 agnomen moead rnsga2
do for n_gen in 250 2500 
do
python pipeline.py -p ${p[0]} -a $a  -gen ${n_gen} -n ${p[1]} -ob ${p[2]} 
done 
done 
done </Users/wuyoscar/Documents/Project/MOOP/experiments/problems_fixed.txt









