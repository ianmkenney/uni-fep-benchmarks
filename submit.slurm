#!/usr/bin/env bash
#SBATCH --mem=64GB
#SBATCH -p gpu
#SBATCH --gres=gpu:1
#SBATCH --ntasks-per-node=1
#SBATCH --time=08:00:00

ARCHIVE_DUMP_DIR=${DATA}/projects/uni_fep_benchmarks

make -f ../../Makefile run-cli

DATASET_NAME=`basename $(pwd)`
ARCHIVE_NAME=${DATASET_NAME}.tar.gz
ARCHIVE_PATH=${ARCHIVE_DUMP_DIR}/${ARCHIVE_NAME}

tar cvfz ${ARCHIVE_PATH} ../${DATASET_NAME}/

if [ -f ${ARCHIVE_PATH} ]; then
    rm -r ../${DATASET_NAME}
fi

exit 1
