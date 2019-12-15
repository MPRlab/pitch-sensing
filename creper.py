# -*- coding: utf-8 -*-
"""
Helper function for the CREPE module.

https://github.com/marl/crepe
"""

import crepe
from notes.chromatic_scale import chromatic_scale
from scipy.io import wavfile
from math import log
from statistics import mean, StatisticsError
import time as timelib
import pandas as pd
from os.path import splitext
from pitch import freq_generator
from notes.note_frequencies import freqs

def creper(filepath, 
           #t_true,
           #y_true,
           models=['tiny', 'small', 'medium', 'large', 'full'], 
           timesteps=[1, 5, 10, 20, 50, 100, 500, 1000],
           conf_filters=[ii/20 for ii in range(0,20,1)],
           noise_threshold=25):
    '''Runs CREPE on .wav file for all model sizes,
    for all timesteps (ms), and filters results by confidence
    level.  Compares CREPE output with ideal frequencies from
    reference data.'''
    
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
                #t_true,y_true=chromatic_scale(0.250,24,60,dt=timestep/1000)
                seq={i:freqs[i] for i in range(24,61)}
                
                #random sequence, 60bpm
                #rseq={i:rfreqs[i] for i in range(0,16)}
                t_true,y_true=freq_generator(seq,0.125,timestep/1000,ascent=False,descent=True)
                
                #Run (and time) CREPE
                start=timelib.time()
                time, frequency, confidence, _ = crepe.predict(audio, 
                                                               sr, 
                                                               model_capacity=model,
                                                               step_size=timestep)
                end=timelib.time()
                
                #Build dataset for pandas
                cents_error=[1200*log(frequency[i]/y_true[i],2) for i in range(0,len(time))]
                
                #Tag noise/data based on user-defined threshold
                tags=[]
                for i in range(0,len(time)):
                    if abs(cents_error[i])>=noise_threshold:
                        tags.append('noise')
                    else:
                        tags.append('pitch')
                        
                data={'Time':time, 
                      'Frequency':frequency, 
                      'Confidence':confidence,
                      'Ideal Frequency':y_true[0:len(time)],
                      'Errors (Cents)':cents_error,
                      'Tag': tags}
                
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
                    
                    if len(filtered_df)!=0:
                        pitch_count=len(filtered_df[filtered_df['Tag']=='pitch'])
                        percent_of_pitch=pitch_count/len(filtered_df)*100
                    else:
                        percent_of_pitch='No Data'
                        
                    #Log Summary Data
                    df_sum=pd.DataFrame({'Model':[model],
                                         'Timestep (ms)':[timestep],
                                         'Confidence (>=)':[conf_filter],
                                         'Ave. Error (cents)':[ave_error],
                                         'CREPE Runtime (s)':[elapsed_time],
                                         'Largest Time Gap (ms)': [biggest_time_gap],
                                         'Percent of Original Data (%)': [percent_of_original_data],
                                         'Percent of Pitch Tags (%)': [percent_of_pitch]})
                    
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
                          f"Percent of Original Data (%): {percent_of_original_data}, " +
                          f'Percent of Pitch Tags (%): {percent_of_pitch}')
                    
                    counter+=1
                    
if __name__=='__main__':
    #Calls creper function on example file

    #chromatic sequence
    #seq={i:freqs[i] for i in range(25,61)}
    
    divisions=20
    timesteps_input=[ii for ii in range(5,105,5)]
    timesteps_input.insert(0,1)
    
    #chromatic scale, 60bpm
    filepath=r"G:\WPI\MPR Lab\Cyther\CREPE\Creper\samples\desc\desc_1_120bpm.wav"
    creper(filepath,
           models=['tiny'], #'tiny', 'small', 'medium', 'large', 'full'
           timesteps=timesteps_input,
           conf_filters=[ii/divisions for ii in range(0,divisions,1)])