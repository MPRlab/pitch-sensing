#ifndef _YIN_H
#define _YIN_H
#include "mbed.h"
#include "platform/CircularBuffer.h"

/* ACF settings */
#define LENGTH 512 //ACF integration window
#define FS 200 //200 Hz
#define PERIOD (1 / FS) * 1000 //convert to period in ms

/* Public global variables */
CircularBuffer<float32_t, LENGTH> input;

/* YIN Globals */
float32_t rawData[LENGTH];
int tau, j; //Variables for the sums and finding the lag
long r, rold, rt, rtau, dt, dtold, dtold2, dj; //Different function variables
int thresh = 0; //Dynamic threshold of when to output frequency
float32_t freq_per, freq_old, freq_old2, filtered_freq, dpt, dold; //Floats to store frequency and sum data
char pd_state = 0; //Peak-detection state-machine variable

/* Function Prototypes */
void readSample();
float ParaIntrp(int, float, float, float);
void FreqCalc();

#endif