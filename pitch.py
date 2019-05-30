# -*- coding: utf-8 -*-
"""
Defines Pitch Sense Class for easy implementation of various pitch detection
algorithms, comparing to reference data, and plotting.
"""

from os.path import splitext
import crepe
from scipy.io import wavfile
import time as timelib
from numpy import arange

def freq_generator(sequence,ioi,dt,ascent=True,descent=False):
    '''Generates list of true frequency values over time given sequence (dict),
    ioi, and timestep (dt).'''
    start_time=0
    stop_time=start_time+ioi
    time=[]
    y=[]
    min_freq_idx=min(sequence.keys())
    max_freq_idx=max(sequence.keys())
    
    if ascent==True:
        #List proper frequency for each timestep in ascending order
        for freq_idx in range(min_freq_idx,max_freq_idx+1):
            for idx, t in enumerate(arange(start_time,stop_time,dt)):
                y.append(sequence[freq_idx])
                time.append(t)
            start_time=stop_time+dt
            stop_time=start_time+ioi
    
    if descent==True:
        #List proper frequency for each timestep in descending order
        for freq_idx in reversed(range(min_freq_idx,max_freq_idx+1)):
            for idx, t in enumerate(arange(start_time,stop_time,dt)):
                y.append(sequence[freq_idx])
                time.append(t)
            start_time=stop_time+dt
            stop_time=start_time+ioi
            
    return time, y
        
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

#    def export(self):
#        '''Exports data to csv.'''
        
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