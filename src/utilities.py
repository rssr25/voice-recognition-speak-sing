'''
Created on: Feb 13, 2023 at 18:43
Created by: Rahul Sharma
Description: Some utility functions for the project
'''


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
    def findCommonData():
        '''
        Finds common data between VocCeleb1 and JukeBox1
        '''
        #TODO: do this sis!
        
    
    @staticmethod
    def arrangeData():
        pass