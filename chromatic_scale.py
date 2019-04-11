# -*- coding: utf-8 -*-
"""
Plots chromatic scale for given frequency range and IOI.
"""
import matplotlib.pyplot as plt
import numpy as np

def plot_chromatic_scale(ioi,start_freq_idx,end_freq_idx,dt=0.01):
    '''Calculates and plots ideal frequency values over time 
    for chromatic scale.'''
    start_time=0
    stop_time=start_time+ioi
    time=[]
    y=[]
    
    #Ascending
    for freq_idx in range(start_freq_idx,end_freq_idx):
        for idx, t in enumerate(np.arange(start_time,stop_time,dt)):
            y.append(freqs[freq_idx])
            time.append(t)
        start_time=stop_time
        stop_time=start_time+ioi

    #Descending
    for freq_idx in reversed(range(start_freq_idx,end_freq_idx)):
        for idx, t in enumerate(np.arange(start_time,stop_time,dt)):
            y.append(freqs[freq_idx])
            time.append(t)
        start_time=stop_time
        stop_time=start_time+ioi   
        
    plt.plot(time,y)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Chromatic Scale, A4: 440 Hz')
    plt.show()


#Frequencies from: http://pages.mtu.edu/~suits/notefreqs.html
#A4=440Hz
freqs=  {0: 16.35,
         1: 17.32,
         2: 18.35,
         3: 19.45,
         4: 20.6,
         5: 21.83,
         6: 23.12,
         7: 24.5,
         8: 25.96,
         9: 27.5,
         10: 29.14,
         11: 30.87,
         12: 32.7,
         13: 34.65,
         14: 36.71,
         15: 38.89,
         16: 41.2,
         17: 43.65,
         18: 46.25,
         19: 49.0,
         20: 51.91,
         21: 55.0,
         22: 58.27,
         23: 61.74,
         24: 65.41,
         25: 69.3, #Note: C#2/Db2
         26: 73.42,
         27: 77.78,
         28: 82.41,
         29: 87.31,
         30: 92.5,
         31: 98.0,
         32: 103.83,
         33: 110.0,
         34: 116.54,
         35: 123.47,
         36: 130.81,
         37: 138.59,
         38: 146.83,
         39: 155.56,
         40: 164.81,
         41: 174.61,
         42: 185.0,
         43: 196.0,
         44: 207.65,
         45: 220.0,
         46: 233.08,
         47: 246.94,
         48: 261.63,
         49: 277.18,
         50: 293.66,
         51: 311.13,
         52: 329.63,
         53: 349.23,
         54: 369.99,
         55: 392.0,
         56: 415.3,
         57: 440.0,
         58: 466.16,
         59: 493.88,
         60: 523.25, #Note: C5 
         61: 554.37,
         62: 587.33,
         63: 622.25,
         64: 659.25,
         65: 698.46,
         66: 739.99,
         67: 783.99,
         68: 830.61,
         69: 880.0,
         70: 932.33,
         71: 987.77,
         72: 1046.5,
         73: 1108.73,
         74: 1174.66,
         75: 1244.51,
         76: 1318.51,
         77: 1396.91,
         78: 1479.98,
         79: 1567.98,
         80: 1661.22,
         81: 1760.0,
         82: 1864.66,
         83: 1975.53,
         84: 2093.0,
         85: 2217.46,
         86: 2349.32,
         87: 2489.02,
         88: 2637.02,
         89: 2793.83,
         90: 2959.96,
         91: 3135.96,
         92: 3322.44,
         93: 3520.0,
         94: 3729.31,
         95: 3951.07,
         96: 4186.01,
         97: 4434.92,
         98: 4698.63,
         99: 4978.03,
         100: 5274.04,
         101: 5587.65,
         102: 5919.91,
         103: 6271.93,
         104: 6644.88,
         105: 7040.0,
         106: 7458.62,
         107: 7902.13}

if __name__=='__main__':
    iois=[0.250,0.125]
    for ioi in iois:
        #meas_start=68.8 Note: C#2/Db2, 69.30  Hz
        #meas_end=524.3  Note: C5     , 523.25 Hz
        plot_chromatic_scale(ioi,25,60)