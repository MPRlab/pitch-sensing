#ifndef _YIN_H
#define _YIN_H
#include "mbed.h"
#include "rtos.h"
#include "platform/CircularBuffer.h"

/* ACF settings */
#define LENGTH 2048 //ACF integration window
#define FS 200 //200 Hz
#define PERIOD (1 / FS) * 1000000 //convert to period in us

/* Public global variables */
extern CircularBuffer<float, (LENGTH * 4)> input;

/* YIN Globals */
extern float rawData[LENGTH];
extern int tau, j; //Variables for the sums and finding the lag
extern float r, rold, rt, rtau, dt, dtold, dtold2, dj; //Different function variables
extern int thresh; //Dynamic threshold of when to output frequency
extern float freq_per, freq_old, freq_old2, filtered_freq, dpt, dold; //Floats to store frequency and sum data
extern char pd_state; //Peak-detection state-machine variable
extern AnalogIn myADC;

/* Function Prototypes */
void readSample();
float ParaIntrp(int, float, float, float);
void FreqCalc();

#endif