#! /bin/bash
while read -ra p
do for s in 500 1000
do for n_eval in 3000 5000 10000 
do for lb in {-3..5}
do for ub in {1..3}  
do
# problem, problem dimension, #objectives, data size, lower bound, upper bound, #evaluations
# create PBS job with paramaters 
cat <<EnD>/scratch/lk32/ow6835/MOOP_Result/bash_jobs/${p[0]}_${p[1]}_${p[2]}_nsga2.job_${s}_${lb}_$(($lb+$ub))_${n_eval} 
#!/bin/bash
#PBS -l ncpus=1,mem=2GB
#PBS -l walltime=24:00:00
#PBS -P lk32
#PBS -q normal
#PBS -l wd
#PBS -m n
#PBS -o /scratch/lk32/ow6835/MOOP_Result/bash_jobs_output
#PBS -e /scratch/lk32/ow6835/MOOP_Result/bash_jobs_error_output


module load gcc/11.1.0
module load intel-mkl/2020.3.304  python3/3.9.2
python3 /scratch/lk32/ow6835/MOOP/NSGA-II.py -p ${p[0]} -s $s -n_eval $n_eval -lb $lb  -ub  $(($lb+$ub)) -d ${p[1]} -o ${p[2]} -f ${p[0]}_${p[1]}_${p[2]}_nsga2.job_${s}_${lb}_$(($lb+$ub))_${n_eval}
EnD

#submited jobs
echo -p ${p[0]} -s $s -n_eval $n_eval -lb $lb  -ub  $(($lb+$ub)) -d ${p[1]} -o ${p[2]} -f ${p[0]}_${p[1]}_${p[2]}_nsga2.job_${s}_${lb}_$(($lb+$ub))_${n_eval}
qsub /scratch/lk32/ow6835/MOOP_Result/bash_jobs/${p[0]}_${p[1]}_${p[2]}_nsga2.job_${s}_${lb}_$(($lb+$ub))_${n_eval}
done
done
done
done 
done </scratch/lk32/ow6835//MOOP/BASH/problems.txt



