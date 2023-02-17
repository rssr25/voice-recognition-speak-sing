'''
Created on: Feb 13, 2023 at 18:43
Created by: Rahul Sharma
Description: Some utility functions for the project
'''

import json
import os
import shutil
import sys

class Utilities():

    @staticmethod
    def createMarkdownTable(header:list, data:list):


        assert len(header) == len(data), 'header size does not match data size'
        columnLength = len(data[0])

        for column in data:

            assert len(column) == columnLength, 'data columns should have the same length'


        h = ""
        headSeparator = ":---:"
        for heading in header:
            h += " | " + heading

        h+= "\n"
        for heading in header:
            h += " | " + headSeparator + " "

        ###########
        d = ""

        for i in range(len(data[0])):
            for j in range(len(data)):

                d += "|" + str(data[j][i])
            
            d+= "\n"
        
        return h, d


    @staticmethod
    def arrangeCommonData():
        '''
        Finds common data between VocCeleb1 and JukeBox1
        '''
        logfile = open("/netscratch/rsharma/voice-recognition-speak-sing/src/commonCopyLogs.txt", 'w+')

        ######################## FOR VOXCELEB COMMON DATA ##############################
        vox1_mainDir = "/netscratch/rsharma/voice-recognition-speak-sing/VoxCeleb_1_2/V1/vox1/wav/"
        with open("/netscratch/rsharma/voice-recognition-speak-sing/vox_id_celeb_commons.json", 'r') as vox_commons:
            voxCelebs = json.load(vox_commons)
        
        #take id, name. get all the folders from that id in voxdata to the corresponding name of the celebrity in your folder
        outDir = "/netscratch/rsharma/voice-recognition-speak-sing/data/speaking/"

        for id, name in voxCelebs.items():
            
            print("Arranging vox data for: " + id + name)
            #getting all the folders from vox1 to the artist's current outpath
            currentInPath = vox1_mainDir + id
            shutil.copytree(currentInPath, outDir + name)
            #os.rename(outDir + id, outDir + name)
            
            #SANITY CHECK
            srcElements = sorted([i for i in os.listdir(vox1_mainDir + id)])
            dstElements = sorted([j for j in os.listdir(outDir + name)])
            assert len(srcElements) == len(dstElements), 'src and dst have different number of files'
            
            for i in range(len(srcElements)):
                if not srcElements[i] == dstElements[i]:
                    print("elements are not same")
                    sys.exit(0)
            
            logfile.write("Successfully transferred Vox data for {}: {}".format(id, name))
        
    
    @staticmethod
    def arrangeData():
        pass