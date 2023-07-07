'''
Created by: Rahul Sharma
Created on: June 6, 2023
Description: Downloads Voxceleb V2 dataset
'''

import os
#import pandas as pd
import itertools
import json
import csv

class VoxCeleb_V2():

    voxDir = None

    @staticmethod
    def checkVox_dev_test_meta(dev_dir, test_dir, meta):
        
        dev_folder = set(os.listdir(dev_dir))
        test_folder = set(os.listdir(test_dir))
        #meta = pd.read_csv(meta, index_col=False)

        #checking the consistency of the metadata and the folders that I have
        meta_ids = list(meta["VoxCeleb2 ID "])
        meta_ids = set([str(id)[:-1] for id in meta_ids])
        data_ids = dev_folder.union(test_folder)
        
        print(list(data_ids)[:10])
        print(list(meta_ids)[:10])

        print("Num of folders: ", str(len(data_ids)))
        print("Num of IDS in metadata: ", str(len(meta)))
        print(data_ids - meta_ids)
        print(meta_ids - data_ids)

    @staticmethod
    def makeVox2Meta():#
        #vggIDs
        vox2meta = []
        with open("/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/vgg_id_celeb_list.json", "r") as data:
            
            vggIDCelebJson = json.load(data)
            #print(vggIDCelebJson)

        
        with open("/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/vox2_meta.csv", "r") as meta:
            
            reader = csv.reader(meta, delimiter=",")
            for row in reader:
                vox2meta.append(row)
        
        vox2meta = vox2meta[1:]
        print(vox2meta[0])

        vox2VggIds_double = [(meta[0].rstrip(), meta[1].rstrip()) for meta in vox2meta]
        
        
        #make Vox ID and celeb name metadata
        vox2_ID_celeb_pair = {}

        for double in vox2VggIds_double:
            vox2ID = double[0]
            vggID = double[1]

            vox2_ID_celeb_pair[vox2ID] = vggIDCelebJson[vggID]
        

        with open("/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/vox2_id_celeb_pair.json", "w+") as pairdata:

            json.dump(vox2_ID_celeb_pair, pairdata)


        





if __name__ == "__main__":

    # dev_path = "/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/dev"
    # test_path = "/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/test"
    # meta_path = "/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V2/vox2_meta.csv"

    # VoxCeleb_V2.checkVox_dev_test_meta(dev_path, test_path, meta_path)


    VoxCeleb_V2.makeVox2Meta()
