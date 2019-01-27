# pitch-sensing
Fundamental frequency detection functions for mbed framework

# craig-fft
MATLAB files are for running an FFT on live audio data or previously recorded voltages from a photoresistor.

read_photoresistor.cpp is dependant on system_parameters.h, CMSIS_DSP_5, and mbed-os.

## read_wav ##
Reads data from header files.  Header files are labeled 1-19, which correspond to loops of Whamola sample audio:

ID, Note, Estimated Frequency

1, D2, 73 Hz

2, C#2, 69 Hz

3, Eb2, 77 Hz

4, C2, 65 Hz

5, D2, 73 Hz

6, Bb1, 58 Hz

7, D2, 73 Hz

8, Ab1, 52 Hz

9, F1, 43 Hz

10, D2, 73 Hz

11, Eb2, 77 Hz

12, D2, 73 Hz

13, C#2, 69 Hz

14, C2, 65 Hz

15, B1, 61 Hz

16, A1, 55 Hz

17, G1, 49 Hz

18, E1, 41 Hz

19, C#1, 34 Hz

## read_photoresistor_float ##
Reads data from A0 pin of Nucleo.
