#! /bin/bash
i=0
while read -ra p
do for pop in 40 100 200 
do
python /Users/wuyoscar/Documents/Project/MOOP/experiments/RandomSearch_pipeline.py -p ${p[0]}  -n ${p[1]} -ob ${p[2]} -pop $pop
echo This is runing ${i} job
echo -p ${p[0]}  -n ${p[1]} -ob ${p[2]} -pop $pop
((i++))
sleep 1 
done
done <problem_large.txt
echo ${i} number of jobs, totally
