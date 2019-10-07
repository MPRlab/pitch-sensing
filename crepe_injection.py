# -*- coding: utf-8 -*-
"""
Test pitch detection time of CREPE when reading from numpy array.

https://github.com/marl/crepe
"""

import crepe
import numpy as np
import matplotlib.pyplot as plt
from os import linesep

#Define sample parameters
fs=16000           #Sample Rate (Hz) - CREPE uses 16kHz
crepe_step_size=1 #Step Size (ms)
crepe_model='tiny' #Model Capacity ('tiny', 'small', 'medium', 'large', 'full')
f1=200             #Hz
f2=840           #Hz
t_switch=0.4       #seconds
t_total=10         #seconds
#Onset results (300-400Hz)
#Step Size, Latency
#20ms: 40ms
#10ms: 10ms
#5ms:5ms (but conf=20)
#2ms:4ms (but conf=22)
#1ms:4ms (but conf=21.5)

#Onset results (400-300Hz)
#Step Size, Latency
#20ms:instant? (but conf=39)
#10ms:instant? (but conf=39)
#5ms:instant? (but conf=39)
#2ms:instant? (but conf=39)
#1ms:instant? (but conf=39)

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
    #Generate sin wave with two frequencies
    t,rec_array=sin_wave_shift(f1,f2,t_switch,t_total,plot=False)

    #Run CREPE on sample
    time, frequency, confidence, _ = crepe.predict(audio=rec_array, sr=fs, 
                                                   model_capacity=crepe_model,
	                                               step_size=crepe_step_size)
    
    #Save results
    save_results(time, frequency, confidence)