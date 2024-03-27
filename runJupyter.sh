#!/bin/bash
srun --mail-type=ALL \
     --mail-user=rsharma@rhrk.uni-kl.de \
     --container-mounts=/netscratch/$USER:/netscratch/$USER \
     --container-image=/netscratch/rsharma/voice-recognition-speak-sing/project.sqsh \
     --container-workdir="`pwd`" \
     --ntasks=1 \
     --cpus-per-task=8 \
     --partition=batch \
     --mem=32GB \
     --export="NCCL_SOCKET_IFNAME=bond,NCCL_IB_HCA=mlx5" \
     bash -c 'hostname -a; jupyter notebook --ip $(hostname -f) --no-browser --port=8989 --allow-root'