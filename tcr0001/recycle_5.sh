#!/bin/bash
#SBATCH --job-name=alphafold
#SBATCH --partition=gpu
#SBATCH --gres=gpu:2
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --ntasks-per-core=1
#SBATCH --threads-per-core=1
#SBATCH --exclude=g8-13,g8-5
#SBATCH --time=3-00:00:00
#SBATCH --verbose
#SBATCH --mail-type=ALL
#SBATCH --mail-user=zarollins@ucdavis.edu 

module list
module load pgi/nvhpc/21.2
module load colabfold
set -x
date
pwd
printenv 2>&1|egrep SLURM
pip3 install torch
pip3 install --upgrade "jax[cuda]" -f https://storage.googleapis.com/jax-releases/jax_releases.html
ls -latr /share/apps/src/colab/colabfold_batch/colabfold/params/params_model_1.npz
colabfold_batch --templates --num-recycle 3 --model-type AlphaFold2-multimer TCR0001.csv 3
