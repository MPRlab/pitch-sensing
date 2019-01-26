#include "yin.h"


Yin::Yin(PinName analogPort){
    myADC = new AnalogIn(analogPort);
}

void Yin::readSample(){
    // while(1){
        // input[globalIndex % LENGTH] = 2 * (myADC.read() - 0.5f);
        float inVal = 2 * (myADC->read() - 0.5f);
        input.push(inVal);
        // printf("inVal: %f\tID: %f\n", inVal, Thread::getid());
        // wait_us(PERIOD_ACF);
    //     Thread::wait(5);
    // }
}

float Yin::ParaIntrp(int c, float fa, float fb, float fc) {
    int a = c - 2;
    int b = c - 1;
    float x;
    x = (float)(b - ((b - a) * (b - a) * (fb - fc) - (b - c) * (b - c) * (fb - fa)) / (2 * (b - a) * (b - a) *
        (fb - fc) - (b - c) * (fb - fa)));
    return x;
}

//Calculates the frequency of the input signal with YIN Autocorrelation
//and peak - detection state - machine
float Yin::FreqCalc() {
    // while(1){
        //printf("%d\n",input.size());
        //printf("Thread is running\n");
        if (!(input.size()<LENGTH)) {
            //printf("Input is full\n");
            //First empty the buffer into the rawData[] array
            for(int i = 0; i < LENGTH; i++){
                input.pop(rawData[i]);
            }
            //Init values for YIN           
            dt = 0;
            dtold = 0;
            dtold2 = 0;
            dj = 0;
            dpt = 0;
            r = 0;
            rt = 0;
            rtau = 0;
            pd_state = 0;
            float period = 0;
            int period_old = 0;
            float current_lowest = 10;
            for (tau = 0; tau < LENGTH; tau++) {
                // YIN-Autocorrelation
                dtold2 = dtold;
                dtold = dt;
                dold = dpt;
                rold = 0;
                r = 0;
                dt = 0;
                dpt = 0;
                //printf("%f\n",rawData[tau]);
                for (j = 0; j < LENGTH / 2; j++) {
                    if (j + tau >= LENGTH) {
                        r = 0;
                        rt = rawData[j] * rawData[j];
                        rtau = 0;
                    } else {
                        r = rawData[j] * rawData[j + tau];
                        rt = rawData[j] * rawData[j];
                        rtau = rawData[j + tau] * rawData[j + tau];
                    }
                    dt += rt + rtau - 2 * r;
                    rold += r;
                }

                dj += dt;
                
                if (tau == 0) {
                    dpt = 1;
                } else {
                    dpt = (float)(dt * tau) / dj;
                }
                
                // Peak Detect State Machine
                if (pd_state == 2 && dold < dpt && dpt < PD_FUDGE) {
                    period_old = tau - 1;
                    period = ParaIntrp(tau, dt, dtold, dtold2);
                    pd_state = 3;
                    break;
                } else if (pd_state == 2 && dold < dpt && dold < current_lowest - 0.1) {
                    current_lowest = dold;
                    period_old = tau - 1;
                    period = ParaIntrp(tau, dt, dtold, dtold2);
                    pd_state = 1;
                }
                if (pd_state == 1 && dold > dpt) {
                    pd_state = 2;
                }
                
                if (!tau) {
                    thresh = rold * 0.5;
                    pd_state = 1;
                }  
            }
            printf("took %d iterations\n",tau);
            // Frequency identified in Hz
            if (thresh > 2) {
                if (period != 0) {
                    freq_old2 = freq_old;
                    freq_old = filtered_freq;
                    freq_per = FS / period;
                    filtered_freq = 0.8 * freq_per + 0.1 * freq_old + 0.1 * freq_old2;
                    if (filtered_freq > FS) {
                        filtered_freq = freq_old;
                        freq_per = freq_old;
                    }
                    if (tau == LENGTH) {
                        filtered_freq = filtered_freq_old;
                    }else{
                        filtered_freq_old = filtered_freq;
                    }
                }
            }
            printf("Locked frequency: %f\n",filtered_freq*250);
            return filtered_freq;
        }
    // }
}