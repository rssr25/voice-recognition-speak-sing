#!/bin/bash

srun --container-mounts=/netscratch/$USER:/netscratch/$USER \
     --container-image=/netscratch/rsharma/voice-recognition-speak-sing/project.sqsh \
     --partition=A100-40GB \
     --container-workdir="`pwd`" \
     --ntasks=1 \
     --cpus-per-task=64 \
     --mem=128GB \
     python /netscratch/rsharma/voice-recognition-speak-sing/src/khurapati.py