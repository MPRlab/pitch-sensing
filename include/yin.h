#ifndef _YIN_H
#define _YIN_H
#include "mbed.h"
#include "rtos.h"
#include "platform/CircularBuffer.h"

/* ACF settings */
#define LENGTH 2048 //ACF integration window
#define FS 200 //200 Hz
#define PERIOD_ACF (1 / FS) * 1000000 //convert to period in us
#define PD_FUDGE 0.6


class Yin{

public:
	// CONSTRUCTOR
	Yin(PinName analogPort);

	/* Function Prototypes */
	void readSample();
	float FreqCalc();

	/* Class member variables */
	CircularBuffer<float, (LENGTH * 4)> input;



private:
	float ParaIntrp(int, float, float, float);


	/* YIN Globals */
	float rawData[LENGTH];
	int tau, j; //Variables for the sums and finding the lag
	float r, rold, rt, rtau, dt, dtold, dtold2, dj; //Different function variables
	int thresh = 0; //Dynamic threshold of when to output frequency
	float freq_per, freq_old, freq_old2, filtered_freq, dpt, dold; //Floats to store frequency and sum data
	float filtered_freq_old = 0.0f;
	char pd_state = 0; //Peak-detection state-machine variable
	AnalogIn * myADC;
};



#endif 