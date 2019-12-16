# -*- coding: utf-8 -*-
"""
Runs CREPE continuously on audio stream.
"""
import sounddevice as sd
import crepe
import time as timelib
import tensorflow as tf
from multiprocessing import Process, Queue
import csv

#Define sample parameters
t_sample=0.2       #CREPE Sample Period
fs=16000           #Sample Rate (Hz) - CREPE uses 16kHz
crepe_step_size=20 #Step Size (ms)
crepe_models= ['tiny', 'small', 'medium', 'large', 'full'] #Model Capacity Choices
crepe_model=crepe_models[0]   #Model Capacity
time_global=timelib.time()    #Set start time (s)

#Initialize tensorflow GPU settings
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.9)
config = tf.ConfigProto(gpu_options=gpu_options)
config.gpu_options.allow_growth = True
session = tf.Session(config=config)

def reader_proc(queue,save_to_file=True):
    '''Read recording from queue, run CREPE, and print results as separate process.'''
    global time_global
    while True:
    	if queue.empty()==False:
	        start=timelib.time()
	        recording = queue.get_nowait() # Reading queue with .get() is ~98% of runtime for tiny model
	        #get_end=timelib.time()

	        #Run CREPE on sample
	        time, frequency, confidence, _ = crepe.predict(audio=recording, sr=fs, 
	                                                   model_capacity=crepe_model,
	                                                   step_size=crepe_step_size)
	        #Adjust time
	        time+=timelib.time()
	        i=0
	        while i<len(time):
	            print(time[i],frequency[i],confidence[i])
	            if save_to_file==True:
	            	filename=r'crepe_stream_data.csv'
	            	with open(filename,mode='a', newline='') as csv_file:
	            		writer=csv.writer(csv_file,delimiter=',')
	            		writer.writerow([time[i],frequency[i],confidence[i]])
	            i+=1
	        time_global+=t_sample
	        end=timelib.time()
	        print('Reader & CREPE loop runtime: '+str(end-start)+' seconds.')

def writer(queue):
    '''Records audio sample (as np.array) and puts in queue.'''
    while True:
        #Record sample
        recording = sd.rec(int(t_sample*fs), samplerate=fs, channels=1)
        #Wait until finished recording
        sd.wait()
        #Write to the queue
        queue.put(recording)
    
if __name__=='__main__':
    q = Queue() # writer() writes to q from _this_ process         
    #Start reader as a separate process
    reader_p = Process(target=reader_proc, args=((q),))
    reader_p.daemon = True
    reader_p.start()        # Launch reader_proc() as a separate python process
    writer(q)               # Record Data
    reader_p.join()         # Process Data