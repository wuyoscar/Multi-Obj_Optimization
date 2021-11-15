#!/bin/bash
#PBS -l ncpus=6,mem=128GB
#PBS -l walltime=6:00:00
#PBS -P lk32
#PBS -q normal
#PBS -l wd
#PBS -m n
#PBS -o /home/582/ow6835/bash_ouput
#PBS -e /home/582/ow6835/bash_error_ouput
module load gcc/11.1.0
module load intel-mkl/2020.3.304  python3/3.9.2
python3 pipeline.py -p tkly1 -a nsga2  -e_val 50000000 -n 4 -ob 2 -pop 100

