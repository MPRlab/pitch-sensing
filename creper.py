# -*- coding: utf-8 -*-
"""
Helper function for the CREPE module.

https://github.com/marl/crepe
"""

import crepe
from scipy.io import wavfile
import pandas as pd
from os.path import splitext

def creper(filepath, timesteps=[1, 5, 10, 20, 50, 100, 500, 1000]):
    '''Runs CREPE on .wav file for all model sizes and
    for all user-defined timesteps (ms).'''
    
    models=['tiny', 'small', 'medium', 'large', 'full']
    sr, audio = wavfile.read(filepath)
    filename=splitext(filepath)[0]
    
    with pd.ExcelWriter(f'{filename}.xlsx') as writer:
        for model in models:
            for timestep in timesteps:
                time, frequency, confidence, _ = crepe.predict(audio, 
                                                               sr, 
                                                               model_capacity=model,
                                                               step_size=timestep)
                
                data={'Time':time, 'Frequency':frequency, 'Confidence':confidence}       
                df=pd.DataFrame(data,columns=['Time', 'Frequency', 'Confidence'])
                df.to_excel(writer, sheet_name=f'{model}_{timestep}')
                
                print(f'Model: {model}, Timestep (ms): {timestep}. Complete.')
            
if __name__=='__main__':
    #Calls creper function on arbitrary example file
    filepath=r"G:\WPI\MPR Lab\Cyther\CREPE\Creper\pitch detection VI.wav"
    creper(filepath)