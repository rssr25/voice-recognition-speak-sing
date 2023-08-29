#!/bin/bash
DONEFILE="/tmp/install_done_${SLURM_JOBID}"
if [[ $SLURM_LOCALID == 0 ]]; then

	echo "Installing dependencies for the semester project"
	apt update
    apt install ffmpeg
       	#apt clean
	pip3 install pydub
	pip3 install matplotlib
	pip3 install numpy
	pip3 install openml
	pip3 install optuna
	pip3 install optuna-dashboard
	pip3 install pandas
	pip3 install ray
	pip3 install scikit_learn
	pip3 install scipy
	pip3 install shap
    pip3 install librosa
	touch "${DONEFILE}"

else
	while [[ ! -f "${DONEFILE}"  ]]; do sleep 1; done
fi

"$@"