#! /bin/bash
i=0
while read -ra p
do for a in nsga2 nsga3 agnomen moead rnsga2
do for n_gen in 100 1000 10000 100000 1000000
do 
cat <<EnD>/home/582/ow6835/bash_scripts/${p[0]}_${a}_${n_gen}
#!/bin/bash
#PBS -l ncpus=1,mem=2GB
#PBS -l walltime=24:00:00
#PBS -P lk32
#PBS -q normal
#PBS -l wd
#PBS -m n
#PBS -o /home/582/ow6835/bash_ouput
#PBS -e /home/582/ow6835/bash_error_ouput
module load gcc/11.1.0
module load intel-mkl/2020.3.304  python3/3.9.2
python3 pipeline.py -p ${p[0]} -a $a  -gen ${n_gen} -n ${p[1]} -ob ${p[2]} 

EnD
((i++))
qsub /home/582/ow6835/bash_scripts/${p[0]}_${a}_${n_gen}
sleep 1 
done 
done 
done <kur1.txt
echo ${i} number of jobs
