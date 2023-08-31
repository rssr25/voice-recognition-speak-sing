#!/bin/bash

srun --mail-type=ALL \
     --mail-user=rsharma@rptu.de \
     --container-mounts=/netscratch/$USER:/netscratch/$USER \
     --container-image=/netscratch/rsharma/voice-recognition-speak-sing/project.sqsh \
     --partition=A100-40GB \
     --container-workdir="`pwd`" \
     --ntasks=1 \
     --cpus-per-task=4 \
     --mem=32GB \
     --time=1-0:0 \
     python /netscratch/rsharma/voice-recognition-speak-sing/src/preprocess_JukeBox.py