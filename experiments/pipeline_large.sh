#! /bin/bash
i=1
while read -ra p
do for a in nsga2 nsga3 agnomen rnsga2
do for e_val in  10000000 50000000  
do for pop in 50  
do
cat <<EnD>/home/582/ow6835/bash_scripts/${p[0]}_${a}_${e_val}
#!/bin/bash
#PBS -l ncpus=8,mem=208GB
#PBS -l walltime=12:00:00
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
sleep 2 
done 
done 
done
done <problem_large.txt
echo ${i} number of jobs, totally
