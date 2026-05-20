#!/usr/bin/env bash
#SBATCH --mem=64GB
#SBATCH -p gpushort
#SBATCH --gres=gpu:1
#SBATCH --ntasks-per-node=1

make -f ../../Makefile run-cli
