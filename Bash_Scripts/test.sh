#!/bin/bash
#PBS -P lk32
#PBS -q normal
#PBS -l mem=2GB
#PBS -l ncpus=1
#PBS -l walltime=01:00:00

# Load modules
module load intel-mkl/2020.3.304
module load python3/3.9.2


# Run Python applications
python3 /scratch/lk32/ow6835/NSGA-II/NSGA-II_crossover.py > $PBS_JOBID.log