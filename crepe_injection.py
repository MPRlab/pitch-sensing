# -*- coding: utf-8 -*-
"""
Test pitch detection time of CREPE when reading from numpy array.

https://github.com/marl/crepe
"""

import crepe
import numpy as np
import matplotlib.pyplot as plt
from os import linesep
from note_frequencies import freqs
from math import log

#Define sample parameters
# fs=16000           #Sample Rate (Hz) - CREPE uses 16kHz
crepe_step_size=1 #Step Size (ms)
crepe_model='tiny' #Model Capacity ('tiny', 'small', 'medium', 'large', 'full')
# f1=200             #Hz
# f2=840           #Hz
# t_switch=1       #seconds
# t_total=2        #seconds

def detection_stats(time, frequency, confidence, f2, t_switch, conf_threshold=0.8):
    '''Calculates CREPE detection time when shifting from f1 to f2.'''
    #Find first time after switch that confidence is above conf_threshold
    t_switch_idx=np.where(time == t_switch)[0][0]
    idx=t_switch_idx
    max_idx=len(time)-1
    while confidence[idx]<conf_threshold:
        idx+=1
        if idx>max_idx:
            break
    if idx>max_idx:
        latency=None
        cents_error=None
    else:
        t_detect=time[idx]
        #Calculate detection time
        latency=t_detect-t_switch
        #Calculate cents_error after confident detection
        cents_error=1200*log(frequency[idx]/f2,2)

    return latency, cents_error

def all_detection_stats(freq_list,crepe_model,crepe_step_size,conf_threshold=0.65,t_switch=1,t_total=2,fs=16000,plot=False):
    #For all ascending frequency shifts in range, print latency and error
    max_idx=len(freq_list)-1
    with open(f'{crepe_model}_'+f'{crepe_step_size}_'+r'all_detection_stats.txt', 'w') as file:
        for idx, freq in freq_list.items():
            if idx==max_idx:
                break

            #Ascend & Descend
            methods=[[idx,idx+1],
                     [idx+1,idx]]

            for method in methods:
                #Get frequencies
                f1=freq_list[method[0]]
                f2=freq_list[method[1]]

                #Generate sin wave with two frequencies
                t,rec_array=sin_wave_shift(f1,f2,t_switch,t_total,fs,plot)

                #Run CREPE on sample
                time, frequency, confidence, _ = crepe.predict(audio=rec_array, sr=fs, 
                                                               model_capacity=crepe_model,
                                                               step_size=crepe_step_size)
                
                #Save results
                #save_results(time, frequency, confidence,filename='test.txt')

                latency, cents_error=detection_stats(time, frequency, confidence, f2, t_switch, conf_threshold)

                print(f1,f2,latency,cents_error)
                    
                file.write(f"f1: {f1}, f2: {f2}, latency: {latency}, cents_error: {cents_error}" + linesep)
    file.close()

def plot(t,y):
    plt.plot(t,y)
    plt.title('Sine Wave shift')
    plt.ylabel('Amplitude')
    plt.xlabel('Time (s)')
    plt.show()

def sin_wave_shift(f1,f2,t_switch,t_total=1,fs=16000,plot=True):
    '''Returns a numpy array with a sine wave at f1 that switches to f2 at
    t_switch.'''
    period_s=1/fs
    #time
    t1=np.arange(0,t_switch,period_s)
    t2=np.arange(t_switch,t_total,period_s)
    t=np.concatenate((t1,t2))
    #angular frequencies
    w1=2*np.pi*f1
    w2=2*np.pi*f2
    #output wave
    y1=np.sin(w1*t1)
    y2=np.sin(w2*t2)
    y=np.concatenate((y1,y2))

    if plot==True:
        plot(t,y)

    return t,y

def save_results(time, frequency, confidence,filename='results.txt'):
    '''Save CREPE results to txt'''
    with open(filename, 'w') as file:
        id=0
        while id<len(time):
            file.write(f"time: {time[id]}, frequency: {frequency[id]}, confidence: {confidence[id]}" + linesep)
            id+=1
    file.close()

if __name__=='__main__':

    models=['tiny', 'small', 'medium', 'large', 'full']
    timesteps=[1,2,5,10]

    for model in models:
        for timestep in timesteps:
            all_detection_stats(freqs,model,timestep,conf_threshold=0.65,t_switch=1,t_total=2,plot=False)

    #Graph results