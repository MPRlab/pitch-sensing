# -*- coding: utf-8 -*-
"""
Helper function for the CREPE module.

https://github.com/marl/crepe
"""

import crepe
from chromatic_scale import chromatic_scale
from scipy.io import wavfile
from math import log
from statistics import mean, StatisticsError
import time as timelib
import pandas as pd
from os.path import splitext

def creper(filepath, 
           models=['tiny', 'small', 'medium', 'large', 'full'], 
           timesteps=[1, 5, 10, 20, 50, 100, 500, 1000],
           conf_filters=[ii/20 for ii in range(0,20,1)]):
    '''Runs CREPE on .wav file for all model sizes and
    for all user-defined timesteps (ms).  Compares CREPE
    output with ideal frequencies from reference data.'''
    
    if type(models)==str:
        models=[models]
    
    sr, audio = wavfile.read(filepath)
    filename=splitext(filepath)[0]
    
    counter=0
    
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
                      'Errors (Cents)':cents_error}
                
                #Get column names
                cols=[label for label, _ in data.items()]
                df=pd.DataFrame(data,columns=cols)
                
                #Write to excel                
                for conf_filter in conf_filters:
                    filtered_df=df[df['Confidence']>=conf_filter]
                    filtered_df.to_excel(writer, 
                                         sheet_name=f'{model}_{timestep}_{conf_filter}')
                    #Calculate summary data
                    abs_error=[abs(error) for error in filtered_df['Errors (Cents)']]
                    try:
                        ave_error=round(mean(abs_error),2)
                    #Exception for case when no values are found
                    except StatisticsError:
                        ave_error="No Data"
                    elapsed_time=round(end-start,6)
                    
                    #Calculate largest time interval between samples
                    #filtered_df_rows=len(filtered_df)
                    filtered_df_indices=list(filtered_df.index)
                    biggest_time_gap=0
                    if filtered_df_indices:
                        for num, idx in enumerate(filtered_df_indices):
                            if idx != 0:
                                prev_idx=filtered_df_indices[num-1]
                                time_gap=filtered_df['Time'][idx]-filtered_df['Time'][prev_idx]
                                if time_gap>biggest_time_gap:
                                    biggest_time_gap=time_gap
                            else: #Row=0
                                time_gap=filtered_df['Time'][idx]-0
                                biggest_time_gap=time_gap
                        last_sample_to_end=max(time)-filtered_df['Time'][max(filtered_df_indices)]
                        if last_sample_to_end>biggest_time_gap:
                            biggest_time_gap=last_sample_to_end
                    else:
                        biggest_time_gap='No Data'
                    
                    #Convert to milliseconds
                    if type(biggest_time_gap)!=str:
                        biggest_time_gap=biggest_time_gap*1000
                    
                    percent_of_original_data=len(filtered_df)/len(df)*100
                    
                    #Log Summary Data
                    df_sum=pd.DataFrame({'Model':[model],
                                         'Timestep (ms)':[timestep],
                                         'Confidence (>=)':[conf_filter],
                                         'Ave. Error (cents)':[ave_error],
                                         'CREPE Runtime (s)':[elapsed_time],
                                         'Largest Time Gap (ms)': [biggest_time_gap],
                                         'Percent of Original Data (%)': [percent_of_original_data]})
                    if counter==0: #First Iteration
                        startrow_arg=0
                        header_arg=True
                    else:
                        startrow_arg=counter+1
                        header_arg=False
                    df_sum.to_excel(writer,
                                    sheet_name='Summary', 
                                    startrow=startrow_arg, 
                                    index = False, 
                                    header=header_arg)
                    #Print Summary Data
                    print(f"Model: {model}, " +
                          f"Timestep (ms): {timestep}, " +
                          f"Confidence (>=): {conf_filter}, " +
                          f"Ave. Error (cents): {ave_error}, " +
                          f"CREPE Runtime (s): {elapsed_time}, " +
                          f"Largest Time Gap (ms): {biggest_time_gap}, " +
                          f"Percent of Original Data (%): {percent_of_original_data}.")
                    
                    counter+=1
                    
if __name__=='__main__':
    #Calls creper function on chromatic scale example file
    filepath=r"G:\WPI\MPR Lab\Cyther\CREPE\Creper\chromaticscale_250.wav"
    divisions=20
    creper(filepath, 
           models=['tiny', 'small', 'medium', 'large', 'full'], 
           timesteps=[ii for ii in range(5,105,5)],
           conf_filters=[ii/divisions for ii in range(0,divisions,1)])