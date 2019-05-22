# -*- coding: utf-8 -*-
"""
Defines Pitch Sense Class for easy implementation of various pitch detection
algorithms, comparing to reference data, and plotting.
"""

class PitchSense:
    '''For easy implementation of various pitch detection
       algorithms, comparing to reference data, and plotting.'''
    
    audio_format='.wav'
    
    def __init__(self, sample_name):
        self.name=sample_name
        self.samples=[]
        self.t_ref=[]
        self.f_ref=[]
        
    def __repr__(self):
        return f'PitchSense({self.name})'
    
    def __str__(self):
        return f'{self.name}'
        
    def add_audio_sample(self, sample_audio):
        self.samples.append(sample_audio)

    def add_ref_freq(self, time_ref, freq_ref):
        #Validate input data by comparing to length and number of samples
        #in PitchSense data
        self.samples.append(time_ref)
        
    def pitch_sense(algorithm): #need additional args
        algorithm=algorithm.upper()
#        if algorithm=='CREPE':
#            pred_data=
#        elif algorithm=='FFT':
#            pred_data=
#            
#        #Add to object rather than return    
#        return pred_data
        