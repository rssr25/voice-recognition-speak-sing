#!/bin/bash

srun --container-mounts=/netscratch/$USER:/netscratch/$USER \
     --container-image=/netscratch/enroot/nvcr.io_nvidia_pytorch_23.07-py3.sqsh \
     --partition=A100-40GB \
     --container-workdir="`pwd`" \
     --mem=48GB \
     --container-save=/netscratch/rsharma/voice-recognition-speak-sing/project.sqsh /netscratch/rsharma/voice-recognition-speak-sing/projectInstall.sh