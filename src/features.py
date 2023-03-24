'''
Created on: March 23, 2023 at 16:30
Created By: Rahul Sharma
Description: class for extracting different features from the audio files
'''

import librosa
import numpy as np

class AudioFeatures():

    @staticmethod
    def lpc(filepath, nmfcc):
        #load the file
        y, sr = librosa.load(filepath)

        #calculate log of the spectrogram
        mel_spec = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
        log_mel_spec = librosa.logamplitude(mel_spec, ref_power=np.max)

        #get first nmfcc coefficients of the wav file
        mfcc = librosa.feature.mfcc(S=log_mel_spec, n_mfcc=nmfcc)

        return mfcc

    
    @staticmethod
    def mfcc(filepath, order, axis):
        pass