#! /bin/bash
while read -ra p
do for s in 500
do for n_eval in  3000 
do for lb in -3
do for ub in 1   
do
# problem, problem dimension, #objectives, data size, lower bound, upper bound, #evaluations
echo ${p[0]}_${p[1]}_${p[2]}_nsga2.job_${s}_${lb}_$(($lb+$ub))_${n_eval} #write bash file

done
done
done
done 
done </Users/wuyoscar/Documents/Project/MOOP/BASH/problems.txt