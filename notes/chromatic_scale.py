# -*- coding: utf-8 -*-
"""
Plots chromatic scale for given frequency range and IOI.
"""
import matplotlib.pyplot as plt
import numpy as np
from notes.note_frequencies import freqs

def chromatic_scale(ioi,start_freq_idx,end_freq_idx,dt=0.01, plot=False):
    '''Calculates and plots ideal frequency values over time 
    for chromatic scale.'''
    start_time=0
    stop_time=start_time+ioi
    time=[]
    y=[]
    
    #Ascending
    for freq_idx in range(start_freq_idx,end_freq_idx+1):
        for idx, t in enumerate(np.arange(start_time,stop_time,dt)):
            y.append(freqs[freq_idx])
            time.append(t)
        start_time=stop_time+dt
        stop_time=start_time+ioi

    #Descending
    for freq_idx in reversed(range(start_freq_idx,end_freq_idx+1)):
        for idx, t in enumerate(np.arange(start_time,stop_time,dt)):
            y.append(freqs[freq_idx])
            time.append(t)
        start_time=stop_time+dt
        stop_time=start_time+ioi   
    
    if plot==True:    
        plt.plot(time,y)
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
        plt.title('Chromatic Scale, A4: 440 Hz')
        plt.show()

    return time, y

if __name__=='__main__':
    #meas_start=68.8 Note: C#2/Db2, 69.30  Hz, Index: 25
    #meas_end=524.3  Note: C5     , 523.25 Hz, Index: 60
    t,y=chromatic_scale(0.250,25,60,plot=True)
    print(t[-1])