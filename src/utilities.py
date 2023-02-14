'''
Created on: Feb 13, 2023 at 18:43
Created by: Rahul Sharma
Description: Some utility functions for the project
'''


class Utilities():

    @staticmethod
    def findCommonData():
        '''
        Finds common data between VocCeleb1 and JukeBox1
        '''
    
    @staticmethod
    def createTable(header:list, data:list):

        h = ""
        headSeparator = ":---:"
        for heading in header:
            h += " | " + heading

        h += " |\n"
        for heading in header:
            h += " | " + heading
        
        h+= "| \n"

        
    
    @staticmethod
    def arrangeData():
        pass