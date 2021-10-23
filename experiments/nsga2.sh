#! /bin/bash
mkdir bash_jobs
while read -ra p
do for n_gen in 10 30 60 100 200 500 
do
# problem, problem dimension, #objectives, data size, (lower bound, upper bound,) #evaluations
# create PBS job with paramaters 
cat <<EnD>bash_jobs/${p[0]}_${p[1]}_${p[2]}_nsga2.job_${s}_${n_gen} 
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

python3 /scratch/lk32/ow6835/MOOP/NSGA-II.py -p ${p[0]} -s $s -n_gen $n_gen -d ${p[1]} -o ${p[2]} -f ${p[0]}_${p[1]}_${p[2]}_nsga2.job_${s}_${n_gen}

EnD

#submited jobs
#echo -p ${p[0]} -s $s -n_gen $n_gen  -d ${p[1]} -o ${p[2]} -f ${p[0]}_${p[1]}_${p[2]}_nsga2.job_${s}_${n_gen}
qsub bash_jobs/${p[0]}_${p[1]}_${p[2]}_nsga2.job_${s}_${n_gen}

/scratch/lk32/ow6835/paretofront /scratch/lk32/ow6835/MOOP_Result/Result/output_X/${p[0]}_${p[1]}_${p[2]}_nsga2.job_${s}_${n_gen} /scratch/lk32/ow6835/MOOP_Result/paratofront/pf_${p[0]}_${p[1]}_${p[2]}_nsga2.job_${s}_${n_gen}  ${p[1]}  ${s} 1 0 

done
done
done
done 
done </scratch/lk32/ow6835/MOOP/BASH/problems.txt



