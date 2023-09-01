"""
Created by Rahul on 31.08.2023
Description: jukebox related khurapati
"""

import os
from pydub import AudioSegment
import numpy as np
from multiprocessing import cpu_count
from multiprocessing import Process
import pandas as pd
import json



def check_duration_jukeBox(artistDirs):
    ###### checking if the tracks in JukeBox is 30 seconds each or not
    """
    THIS HAS BEEN CHECKED AND ALMOST ALL OF THE SNIPPETS ARE 30 SECONDS FOR TRAIN so I will not preprocess on my own.
    THIS HAS BEEN CHECKED AND ALMOST ALL OF THE SNIPPETS ARE 30 SECONDS FOR TEST so I will not preprocess on my own. 
    """
    for artistDir in artistDirs:

        #print(os.listdir(artistDir))
        tracks_paths = [artistDir + "/" + i.decode('utf8') for i in os.listdir(artistDir)]

        for trackpath in tracks_paths:

            track = AudioSegment.from_file(trackpath)
            if track.duration_seconds != 30:
                print(f"{trackpath}: {track.duration_seconds}")


def get_vox_1_2_jukebox_commons():

    jukeMeta_path = "/netscratch/rsharma/voice-recognition-speak-sing/JukeBox_FULL/metadata.csv"
    vox1Meta_path = "/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V1/vox1/vox1_meta.csv"
    vox2Meta_path = "/netscratch/rsharma/voice-recognition-speak-sing/vox2_id_celeb_pair.json"

    jukeMeta = pd.read_csv(jukeMeta_path, header=0)
    vox1Meta = pd.read_csv(vox1Meta_path, header=0, delimiter="\t")

    print(list(vox1Meta))

    with open(vox2Meta_path, "r") as vox2MetaFile:
        vox2Meta = json.load(vox2MetaFile)
    

    jukeBoxNames = jukeMeta["artist_name"].unique()
    vox1Names    = vox1Meta["VGGFace1 ID"]
    vox2Names    = vox2Meta.values()

    jukeBoxNames = [str(i).lower() for i in jukeBoxNames]
    vox1Names    = [str(i).lower() for i in vox1Names]
    vox2Names    = [str(i).lower() for i in vox2Names]

    jukeBoxNames = [i.replace(" ", "_") for i in jukeBoxNames]
    vox1Names    = [i.replace(" ", "_") for i in vox1Names]
    vox2Names    = [i.replace(" ", "_") for i in vox2Names]


    jukeAndVox1Commons = set(jukeBoxNames) & set(vox1Names)
    jukeAndVox2Commons = set(jukeBoxNames) & set(vox2Names)
    commons_between_above_2_sets = jukeAndVox1Commons & jukeAndVox2Commons
    commonsVox1_2 = set(vox1Names) & set(vox2Names)

    print(f"Total JukeBoxNames: {len(jukeBoxNames)}")
    print(f"Total vox1Names: {len(vox1Names)}")
    print(f"Total vox2Names: {len(vox2Names)}")
    print(f"Common between jukebox and vox1: {len(jukeAndVox1Commons)}")
    print(f"Common between jukebox and vox2: {len(jukeAndVox2Commons)}")
    print(f"Common between above 2: {len(commons_between_above_2_sets)}")
    print(f"Common between vox1 and  vox2: {len(commonsVox1_2)}")






if __name__ == "__main__":

    # dirPath = "/netscratch/rsharma/voice-recognition-speak-sing/JukeBox_FULL/TEST/"
    # artistDirs = [dirPath + i for i in os.listdir(dirPath)]

    # splits = np.array_split(artistDirs, cpu_count())
    # procs = []
    # for split in splits:
    #     proc = Process(target=check_duration_jukeBox, args=(split, ))
    #     procs.append(procs)
    #     proc.start()
    
    # for proc in procs:
    #     proc.join()        

    get_vox_1_2_jukebox_commons()