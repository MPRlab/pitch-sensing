# -*- coding: utf-8 -*-
"""
Runs CREPE continuously on audio stream.
"""

import sounddevice as sd
import crepe
#Use 'python -m sounddevice' to find device list (Webcam mic=1)

t=10       #Recording Duration (Seconds)
t_sample=1 #CREPE Period
fs=16000   #Sample Rate (Hz)

for sample in range(0,t+1,t_sample):
    #Record sample
    recording = sd.rec(int(t_sample*fs), samplerate=fs, channels=1)
    sd.wait()
    
    #Run CREPE on sample
    time, frequency, confidence, _ = crepe.predict(audio=recording, 
                                                   sr=fs, 
                                                   model_capacity='full',
                                                   step_size=20)
    #Print Results
    i=0
    print('time, frequency, confidence')
    while i<len(time):
        print(time[i],frequency[i],confidence[i])
        i+=1

#print('Start Playing')
#sd.playrec(recording, samplerate=fs, channels=1,blocking=True)