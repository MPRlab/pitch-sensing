# -*- coding: utf-8 -*-
"""
Helper function for the CREPE module.

https://github.com/marl/crepe
"""

import crepe
from chromatic_scale import chromatic_scale
from scipy.io import wavfile
from math import log
from statistics import mean
import time as timelib
import pandas as pd
from os.path import splitext

def creper(filepath, 
           models=['tiny', 'small', 'medium', 'large', 'full'], 
           timesteps=[1, 5, 10, 20, 50, 100, 500, 1000]):
    '''Runs CREPE on .wav file for all model sizes and
    for all user-defined timesteps (ms).'''
    
    if type(models)==str:
        models=[models]
    
    sr, audio = wavfile.read(filepath)
    filename=splitext(filepath)[0]
    
    with pd.ExcelWriter(f'{filename}.xlsx') as writer:
        for model in models:
            for timestep in timesteps:
                #Calculate ideal frequencies
                #chromatic_scale(ioi,start_freq_idx,end_freq_idx,dt=0.01, plot=False)
                t_scale,y_scale=chromatic_scale(0.250,24,60,dt=timestep/1000)
                
                #Run (and time) CREPE
                start=timelib.time()
                time, frequency, confidence, _ = crepe.predict(audio, 
                                                               sr, 
                                                               model_capacity=model,
                                                               step_size=timestep)
                end=timelib.time()
                
                #Build dataset for pandas
                cents_error=[1200*log(frequency[i]/y_scale[i],2) for i in range(0,len(time))]
                data={'Time':time, 
                      'Frequency':frequency, 
                      'Confidence':confidence,
                      'Ideal Frequency':y_scale[0:len(time)],
                      'Errors (Cents)':cents_error,
                      'Abs. Errors (Cents)':[abs(error) for error in cents_error]}  
                
                #Get column names
                cols=[label for label, _ in data.items()]
                #Write to excel                
                df=pd.DataFrame(data,columns=cols)
                df.to_excel(writer, sheet_name=f'{model}_{timestep}')
                #Calculate and print summary values
                ave_error=round(mean(data['Abs. Errors (Cents)']),2)
                elapsed_time=round(end-start,6)
                print(f"""Model: {model}, 
                      Timestep (ms): {timestep}, 
                      Average Error: {ave_error} (cents), 
                      CREPE Time: {elapsed_time} (s). 
                      Complete.""")
            
if __name__=='__main__':
    #Calls creper function on chromatic scale example file
    filepath=r"G:\WPI\MPR Lab\Cyther\CREPE\Creper\chromaticscale_250.wav"
    creper(filepath)