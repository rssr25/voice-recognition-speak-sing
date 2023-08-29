"""
Created by Rahul on 29.08.2023 at 17:53
Used to do parallel conversion of files from m4a to wav
"""

from multiprocessing import Process, cpu_count
from utilities import Utilities
import os
import numpy as np


if __name__ == "__main__":

    #getting all the dirpaths for VoxCeleb 2 for dev
    #mainPath = "/netscratch/rsharma/voice-recognition-speak-sing/src/testFolder/V2/aac/" ##just for testing
    mainPath = "/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/audio/dev/aac/"
    dirPaths = [mainPath + i for i in os.listdir(mainPath)]
    splits = np.array_split(dirPaths, cpu_count())
    procs = []
    formats_to_convert = ['.m4a']

    for split in splits:

        proc = Process(target=Utilities.convertToWav, args=(formats_to_convert, split))
        procs.append(procs)
        proc.start()
    
    #complete the processes
    for proc in procs:
        proc.join()


