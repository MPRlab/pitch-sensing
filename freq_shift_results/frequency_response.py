# -*- coding: utf-8 -*-
"""
Plots freq. vs error.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_freq_response(f1,f2,y,title='Freq. vs. Error',save=False,scatter=False):
    '''Plots frequency response data'''
    if scatter==True:
        plt.scatter(f1,y)
        plt.scatter(f2,y)  
    else:
        plt.plot(f1,y)
        plt.plot(f2,y)
    plt.title(title)
    plt.xlabel('Frequency')
    plt.ylabel('Abs. Error (Cents)')
    plt.legend(['F1', 'F2'], loc='upper right')
    if save==True:
        plt.savefig(title)
    plt.show()

file=pd.ExcelFile(r"C:\Users\Craig\Documents\GitHub\pitch-sensing\freq_shift_results\detection_visualization.xlsx")
sheetnames=file.sheet_names
bandpass_f1=200
bandpass_f2=2000
bandpass=False

for sheetname in sheetnames:
    df=pd.read_excel(file,sheetname)
    if bandpass==True:
        df=df[(df.f1>=bandpass_f1) & (df.f1<=bandpass_f2)]
    f1,f2=df['f1'].values, df['f2'].values
    df['abs_cents_error'] = pd.to_numeric(df['abs_cents_error'], errors='coerce')
    df['abs_cents_error'] = df['abs_cents_error'].replace(np.nan, 0)
    y=df['abs_cents_error'].values
    plot_freq_response(f1,f2,y,title=sheetname,save=True,scatter=True)