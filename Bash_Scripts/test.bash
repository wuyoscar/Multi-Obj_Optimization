#!/bin/bash
#PBS -P lk32
#PBS -q normal
#PBS -l mem=2GB
#PBS -l ncpus=1
#PBS -l walltime=01:00:00

# Load modules
module unload python python3
module load python3/3.8.5

# Run Python applications
