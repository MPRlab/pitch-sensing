# -*- coding: utf-8 -*-
"""
Runs CREPE continuously on audio stream.
"""
import sounddevice as sd
import crepe
import time as timelib
import tensorflow as tf
from multiprocessing import Process, Queue
import sys

#Define sample parameters
t_sample=0.5       #CREPE Sample Period
fs=16000           #Sample Rate (Hz) - CREPE uses 16kHz
crepe_step_size=50 #Step Size (ms)
crepe_model='tiny' #Model Capacity ('tiny', 'small', 'medium', 'large', 'full')
time_global=0      #Set start time (s)

#Initialize tensorflow GPU settings
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.7)
config = tf.ConfigProto(gpu_options=gpu_options)
config.gpu_options.allow_growth = True
session = tf.Session(config=config)

def reader_proc(queue):
    '''Read recording from queue, run CREPE, and print results.'''
    ## Read from the queue; this will be spawned as a separate Process
    #print('time, frequency, confidence')
    global time_global
    while True:
        start=timelib.time()
        recording = queue.get()
        #Run CREPE on sample
        time, frequency, confidence, _ = crepe.predict(audio=recording, sr=fs, 
                                                   model_capacity=crepe_model,
                                                   step_size=crepe_step_size)
        #Adjust time
        time+=time_global
        i=0
        while i<len(time):
            print(time[i],frequency[i],confidence[i])
            i+=1
        time_global+=t_sample
        end=timelib.time()
        print('Reader & CREPE loop runtime: '+str(end-start)+' seconds.')

def writer(queue):
    '''Records audio sample (as nparray) and puts in queue.'''
    while True:
        #Record sample
        recording = sd.rec(int(t_sample*fs), samplerate=fs, channels=1)
        #Wait until finished recording
        sd.wait()
        #Write to the queue
        queue.put(recording)
    
if __name__=='__main__':
    pqueue = Queue() # writer() writes to pqueue from _this_ process         
    #Start reader as a separate process
    reader_p = Process(target=reader_proc, args=((pqueue),))
    reader_p.daemon = True
    reader_p.start()        # Launch reader_proc() as a separate python process
    writer(pqueue)          # Record Data
    reader_p.join()         # Process Data