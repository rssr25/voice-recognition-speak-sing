'''
Created on: March 23, 2023 at 16:30
Created By: Rahul Sharma
Description: class for extracting different features from the audio files
1. mfcc
2. lpc
'''

import librosa
import numpy as np

class AudioFeatures():

    @staticmethod
    def mfcc(signal, signalRate, nmfcc):
        '''
        This function takes in the signal and the signal rate with the number of the coefficients
        oen wants and gives out the mfcc. 

        Input: signal (np.ndarray) loaded using librosa,
               signalRate (float/int) loaded using librosa,
               nmfcc (int) number of coefficients required

        Output: mfcc coefficients <3

        '''
        #load the file

        #calculate log of the spectrogram
        mel_spec = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
        log_mel_spec = librosa.logamplitude(mel_spec, ref_power=np.max)

        #get first nmfcc coefficients of the wav file
        mfcc = librosa.feature.mfcc(S=log_mel_spec, n_mfcc=nmfcc)

        return mfcc

    
    @staticmethod
    def lpc(signal: np.ndarray, signalRate: int, order: int, axis: int) -> np.ndarray:
        '''
        This function takes in the signal and the signal rate with the order and axis
        and number of the coefficients
        oen wants and gives out the lpc coefficients. 

        Input: signal (np.ndarray) loaded using librosa,
               signalRate (float/int) loaded using librosa,
               order (int) rder of the linear filter
               axis (int) axis along which to compute the coefficients

        Output: lpc coefficients <3
        
        '''

        lpc = librosa.lpc(signal, order=order)

        return lpc
        