#! /bin/bash
i=0
while read -ra p
do for a in nsga2 nsga3 agnomen rnsga2
do for e_val in  10000000  
do for pop in 100  
do
cat <<EnD>/home/582/ow6835/bash_scripts/${p[0]}_${a}_${e_val}
#!/bin/bash
#PBS -l ncpus=6,mem=32GB
#PBS -l walltime=24:00:00
#PBS -P lk32
#PBS -q normal
#PBS -l wd
#PBS -m n
#PBS -o /home/582/ow6835/bash_ouput
#PBS -e /home/582/ow6835/bash_error_ouput
module load gcc/11.1.0
module load intel-mkl/2020.3.304  python3/3.9.2
python3 pipeline.py -p ${p[0]} -a $a  -e_val ${e_val} -n ${p[1]} -ob ${p[2]} -pop $pop

EnD
echo python3 pipeline.py -p ${p[0]} -a $a  -e_val ${e_val} -n ${p[1]} -ob ${p[2]} -pop $pop
echo This is runing ${i} job
((i++))
qsub /home/582/ow6835/bash_scripts/${p[0]}_${a}_${e_val}
sleep 1 
done 
done 
done
done <problem_large.txt
echo ${i} number of jobs, totally
