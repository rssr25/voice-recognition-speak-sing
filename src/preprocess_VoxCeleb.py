"""
Created by Rahul on 29.08.2023 at 17:53
Used to do parallel conversion of files from m4a to wav
"""

from multiprocessing import Process, cpu_count
from utilities import Utilities
import os
import numpy as np
from pydub import AudioSegment
import json

class PreprocessVox2():

    def __init__(self) -> None:
        pass

    
    @staticmethod
    def convert_m4a_to_wav_multiprocessing():
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
    
    @staticmethod
    def make_5_sec_chunks():

        """The paper has 5s chunks of the audio files. I will do this the following way

        1. Merge all the files in a video folder to one file- 
        2. Make 5 second chunks from the merged file
        3. discard if the last chunk is less than 5 seconds.
        """

        #checking the length of the json for all the files.
        with open("/netscratch/rsharma/voice-recognition-speak-sing/src/vox2_durations.json", "r") as durationFile:

            durations = json.load(durationFile)
        
        assert len(durations) == 1092009, f"Discrepancy in the number of files {len(durations)}/{1092009}"
        print(len(durations))
        

    @staticmethod
    def get_duration_of_files_in_folder(dirPath):

        extensions = [".wav"]
        fileDurations = {}

        for (dirpath, dirnames, filenames) in os.walk(dirPath + "/"):

            for filename in filenames:
                if filename.endswith(tuple(extensions)):
                    
                    filepath = dirpath + '/' + filename
                    audio = AudioSegment.from_file(filepath)
                    fileDurations[filepath] = audio.duration_seconds
        


        with open("/netscratch/rsharma/voice-recognition-speak-sing/src/vox2_durations.json", "w+") as savefile:

            json.dump(fileDurations, savefile)





if __name__ == "__main__":


    dirPath = "/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/audio/dev/aac"
    #PreprocessVox2.get_duration_of_files_in_folder(dirPath)
    PreprocessVox2.make_5_sec_chunks()

    


