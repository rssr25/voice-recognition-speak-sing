'''
Created on: Feb 13, 2023 at 18:43
Created by: Rahul Sharma
Description: Some utility functions for the project
'''

import json
import os
import shutil
import sys
import argparse
from pydub import AudioSegment

class Utilities():

    @staticmethod
    def createMarkdownTable(header:list, data:list):
        '''
         Creates a markdown table with data of the form
         header: [col1, col2,..., coln]
         data: [[element1, element2,..., element_n], 
                [element1, element2,..., element_n], 
                 ..., 
                [element1, element2,..., element_n]]
        '''

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
    def arrangeVoxCommonData():
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
            logfile.write("\n")

        
        
        
    
    @staticmethod
    def arrangeJukeCommonData():

        ######################## FOR JUKEBOX COMMON DATA ##############################
        logfile = open("/netscratch/rsharma/voice-recognition-speak-sing/src/commonCopyLogs.txt", 'a')
        juke1_mainDir = "/netscratch/rsharma/voice-recognition-speak-sing/JukeBox_FULL/TRAIN/"
        with open("/netscratch/rsharma/voice-recognition-speak-sing/juke_id_celeb_commons.json", 'r') as juke_commons:
            jukeCelebs = json.load(juke_commons)
        
        with open("/netscratch/rsharma/voice-recognition-speak-sing/auxiliarys.json") as auxBitches:
            auxis = json.load(auxBitches)
        
        dontInclude = [key for key, value in auxis.items()]

        outDir = "/netscratch/rsharma/voice-recognition-speak-sing/data/singing/"

        for id, name in jukeCelebs.items():
            if id in dontInclude:
                continue

            print("Arranging Juke data for: " + id + name)
            #getting all the folders from vox1 to the artist's current outpath
            currentInPath = juke1_mainDir + id
            shutil.copytree(currentInPath, outDir + name)


        #SANITY CHECK
            srcElements = sorted([i for i in os.listdir(juke1_mainDir + id)])
            dstElements = sorted([j for j in os.listdir(outDir + name)])
            assert len(srcElements) == len(dstElements), 'src and dst have different number of files'
            
            for i in range(len(srcElements)):
                if not srcElements[i] == dstElements[i]:
                    print("elements are not same")
                    sys.exit(0)
            
            logfile.write("Successfully transferred Vox data for {}: {}".format(id, name))
            logfile.write("\n")
        
    
    @staticmethod
    def convertToWav(formats_to_convert:list, dirPath):

        for dirPath in dirPaths:
            for (dirpath, dirnames, filenames) in os.walk(dirPath + "/"):
                
                for filename in filenames:
                    if filename.endswith(tuple(formats_to_convert)):

                        filepath = dirpath + '/' + filename
                        (path, file_extension) = os.path.splitext(filepath)
                        file_extension_final = file_extension.replace('.', '')
                        try:
                            track = AudioSegment.from_file(filepath,
                                    file_extension_final)
                            wav_filename = filename.replace(file_extension_final, 'wav')
                            wav_path = dirpath + '/' + wav_filename
                            print('CONVERTING: ' + str(filepath))
                            file_handle = track.export(wav_path, format='wav')
                            os.remove(filepath)
                        except:
                            print("ERROR CONVERTING " + str(filepath))
