#! /bin/bash
i=0
while read -ra p
do for a in nsga2 nsga3 agnomen rnsga2
do for n_eval in 1000 3000 5000  10000 50000
do for pop in 40 100 200 
do
cat <<EnD>/home/582/ow6835/bash_scripts/${p[0]}_${a}_${n_eval}
#!/bin/bash
#PBS -l ncpus=4,mem=12GB
#PBS -l walltime=10:00:00
#PBS -P lk32
#PBS -q normal
#PBS -l wd
#PBS -m n
#PBS -o /home/582/ow6835/bash_ouput
#PBS -e /home/582/ow6835/bash_error_ouput
module load gcc/11.1.0
module load intel-mkl/2020.3.304  python3/3.9.2
python3 pipeline.py -p ${p[0]} -a $a  -e_val ${n_eval} -n ${p[1]} -ob ${p[2]} -pop $pop

EnD
echo python3 pipeline.py -p ${p[0]} -a $a  -e_val ${n_eval} -n ${p[1]} -ob ${p[2]} -pop $pop
echo This is runing ${i} job
((i++))
qsub /home/582/ow6835/bash_scripts/${p[0]}_${a}_${n_eval}
sleep 1 
done 
done 
done
done <problem_3.txt
echo ${i-1} number of jobs, totally








