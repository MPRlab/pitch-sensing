# -*- coding: utf-8 -*-
"""
Defines Pitch Sense Class for easy implementation of various pitch detection
algorithms, comparing to reference data, and plotting.
"""

from os.path import splitext
import crepe
from scipy.io import wavfile
import time as timelib

class PitchSense:
    '''For easy implementation of various pitch detection
       algorithms, comparing to reference data, and plotting.'''
    
    audio_format='.wav'
    
    def __init__(self, sample_name):
        self.name=sample_name
        self.sample=[]
        self.t_true=[]
        self.f_true=[]
        self.models={'crepe':{},
                     'fft':{}}
        
    def __repr__(self):
        return f'PitchSense({self.name})'
    
    def __str__(self):
        return f'{self.name}'
        
    def add_audio_sample(self, sample_audio):
        '''Adds .wav file.'''
        _, ext=splitext(sample_audio)
        if ext.upper()=='.WAV':
            self.sample.append(sample_audio)
        else:
            print("Unexpected filetype.  Please specify .wav file.")
            raise TypeError

    def add_true_freq(self, time_true, freq_true):
        '''Add known frequencies over time interval.'''
        #Validate input data by comparing to length and number of samples
        #in PitchSense data
        self.t_true.append(time_true)
        self.f_true.append(freq_true)
        
#    def compare(self, model):
#        '''Compares model predictions to reference frequencies.'''
        
#    def plot(self):
#        '''Plots Error, % of Data Lost and Largest Time Gap'''
    
    def run_crepe(self, timestep, crepe_model='full'):
        '''Runs CREPE on .wav file'''
        sr, audio = wavfile.read(self.sample[0])
        
        #Run (and time) CREPE
        start=timelib.time()
        time, frequency, confidence, _ = crepe.predict(audio, 
                                                       sr, 
                                                       model_capacity=crepe_model,
                                                       step_size=timestep)
        end=timelib.time()
        elapsed_time=round(end-start,6)
        
        #Save data to object
        latest_crepe_version=len(self.models['crepe'])
        self.models['crepe']={latest_crepe_version:{'runtime':elapsed_time,
                                                    'time':time,
                                                    'frequency':frequency,
                                                    'confidence':confidence}}
        
#    def run_fft(self):
#        return data      