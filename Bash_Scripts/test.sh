#!/bin/bash
#PBS -P lk32
#PBS -q normal
#PBS -l mem=2GB
#PBS -l ncpus=1
#PBS -l walltime=01:00:00

# Load modules
module unload intel-compiler python python3 pymoo
module load python3/3.8.5


# Run Python applications
python3 /home/582/ow6835/Loopfiles/algorithmns/NSGA-II/NSGA-II_crossover.py > $PBS_JOBID.log