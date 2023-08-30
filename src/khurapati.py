#### Extra space for random housekeeping stuff
import json
import pandas as pd
from utilities import Utilities
import os
import threading


# meta = pd.read_csv("/Users/rahulsharma/Desktop/Semester 4/Project/MyProject/voice-recognition-speak-sing/data/metdata.csv")
# header = list(meta)[1:]
# data = []
# for columnName in header:
#     data.append(list(meta[columnName]))


# h, d = Utilities.createMarkdownTable(header, data)
# print(h)


def doubleCheckJukebox():

    '''
    Take all the ids of vox2 data and compare them to the text and audio data
    '''
    workdir = "/netscratch/rsharma/voice-recognition-speak-sing/"
    with open(workdir + "vox2_id_celeb_pair.json", "r") as data:

        vox2data = json.load(data)
    

    ids = set(list(vox2data.keys()))

    #get the ids from the audio data
    audio_mainDir = "/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/audio/"
    audio_test = set(os.listdir("/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/audio/test/aac"))
    audio_dev = set(os.listdir("/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/audio/dev/aac"))
    audio_ids = audio_test.union(audio_dev)


    #get the ids from the text data
    text_mainDir = "/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/audio/"
    text_test = set(os.listdir("/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/no_audio/test"))
    text_dev = set(os.listdir("/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/no_audio/dev"))
    text_ids = text_test.union(text_dev)


    print("***************** INFORMATION ON COUNT OF DATA *******************")
    print(f'num_of_ids: {len(ids)}')

    print(f'audio_test: {len(audio_test)}')
    print(f'audio_dev: {len(audio_dev)}')
    print(f'audio_test + audio_dev: {len(audio_test) + len(audio_dev)}')

    print(f'text_test: {len(text_test)}')
    print(f'text_dev: {len(text_dev)}')
    print(f'text_test + text_dev: {len(text_test) + len(text_dev)}')


    """
    Missing data
    id05348 ,n00534s7 ,m ,test ----> n005347, "Luke_Hemsworth", 422, 0, m
    id04170 ,n004169 ,m ,test ----> n004169, "Joel_Lundqvist", 360, 1, m


    wheere index changed in Vox2_meta: id01420 ,n001419 ,f ,dev 
    """



def convert_to_wav(listOfExtensions, dirPath):

    
    Utilities.convertToWav(formats_to_convert, dirPath)


def verify_the_VoxCeleb_m4a_2_wav():

    dirPath = "/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/audio/dev/aac"
    formats_to_convert = [".wav"]
    counter = 0

    for (dirpath, dirnames, filenames) in os.walk(dirPath + "/"):

        for filename in filenames:
            if filename.endswith(tuple(formats_to_convert)):
                counter += 1

                #filepath = dirpath + '/' + filename
                #(path, file_extension) = os.path.splitext(filepath)
    
    print(counter)




if __name__ == "__main__":

    formats_to_convert = ['.m4a']
    dirPath = "/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/audio/dev/aac"
    #convert_to_wav(formats_to_convert, dirPath)

    verify_the_VoxCeleb_m4a_2_wav()