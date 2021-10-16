#!/bin/bash
#PBS -l ncpus=1,mem=1GB
#PBS -l walltime=1:00:00
#PBS -P lk32
#PBS -q normal
#PBS -l wd
#PBS -m n
#PBS -o /scratch/lk32/ow6835/MOOP_Result/bash_jobs_output/
#PBS -e /scratch/lk32/ow6835/MOOP_Result/bash_jobs_error_output/

module load gcc/11.1.0
module load intel-mkl/2020.3.304  python3/3.9.2

python3 /scratch/lk32/ow6835/MOOP/NSGA-II.py -p chankong -s 500 -n_eval 3000  -d 2 -o 2 -f chankong_2_2_nsga2.job_500_3000

EnD

#submited jobs
#echo -p ${p[0]} -s $s -n_eval $n_eval -lb $lb  -ub  ${ub} -d ${p[1]} -o ${p[2]} -f ${p[0]}_${p[1]}_${p[2]}_nsga2.job_${s}_${n_eval}
qsub bash_jobs/${p[0]}_${p[1]}_${p[2]}_nsga2.job_${s}_${n_eval}

/scratch/lk32/ow6835/paretofront /scratch/lk32/ow6835/MOOP_Result/Result/output_X/${p[0]}_${p[1]}_${p[2]}_nsga2.job_${s}_${n_eval} /scratch/lk32/ow6835/MOOP_Result/paratofront/pf_${p[0]}_${p[1]}_${p[2]}_nsga2.job_${s}_${n_eval}  ${p[1]}  ${s} 1 0 
