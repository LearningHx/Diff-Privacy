#!/bin/bash
#JSUB -q ISN
#JSUB -gpgpu 1
#JSUB -n 5
#JSUB -J test
#JSUB -e error.%J
#JSUB -o output.%J

module load mpc/1.2.1 mpfr/4.1.0 gmp/6.2.1 gcc/6.5.0 cuda/10.2
source /apps/software/anaconda3/etc/profile.d/conda.sh
conda activate ldm

python main.py --base configs/stable-diffusion/v1-finetune.yaml --data_root /data1/hx/diffusion_anonymation_arcface_faceParsing2/dataset --actual_resume /data1/hx/diffusion_anonymation_arcface_faceParsing2/models/sd/sd-v1-4.ckpt -n chicago_wide --gpus 0, -t --lightning
