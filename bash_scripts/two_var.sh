#! /bin/bash
for p in $(cat /scratch/lk32/ow6835/MOOP/Bash_Loop/problem_txt/two_var_problems.txt)
do for s in 50 100 150 200
do for n_eval in  3000 5000 7000 8000
do for lb in {-3..-1}
do for ub in {1..4}
do
cat <<EnD>/scratch/lk32/ow6835/jobs/${p-2-[lb,ub]-s-n_eval}.sh
#!/bin/bash
#PBS -l ncpus=1,mem=20GB
#PBS -l walltime=24:00:00
#PBS -P lk32
#PBS -q normal
#PBS -l wd
#PBS -o /scratch/lk32/ow6835/JOBOUTS
#PBS -e /scratch/lk32/ow6835/JOBOUTS

#Use submission environment
#PBS -V
#Start job from the directory it was submitted
module load gcc/11.1.0
module load intel-mkl/2020.3.304  python3/3.9.2

python3 /scratch/lk32/ow6835/MOOP/NSGA-II.py -p $p -s $s -n_eval $n_eval -lb $lb $lb -ub  $ub $ub -d 2 -f $p-2-[$lb,$ub]-$n_eval-$s
EnD


sleep 1
done
done
done
done 
done



