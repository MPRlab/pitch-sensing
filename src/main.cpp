#include "mbed.h"
#include "platform/CircularBuffer.h"
#include "rtos.h"
#include "yin.h"

/* MBED class APIs */
DigitalOut myled(LED1);
AnalogIn   myADC(A1);
Serial     pc(USBTX, USBRX);
Thread     adcThread;
Thread     avgThread;

void readSample(){
  while(!input.full()){
    //input[globalIndex % LENGTH] = 2 * (myADC.read() - 0.5f);
    float32_t inVal = 2 * (myADC.read() - 0.5f);
    input.push(inVal);
    //pc.printf("%f\n", input[globalIndex % LENGTH]);
    //globalIndex++;
    wait_ms(PERIOD); //read a sample @ 200Hz
  }
}

void movAvg(){
  while(1){
    float32_t moving_average = 0;
    float32_t moving_sum = 0;
    for(int i = 0; i<LENGTH; i++){
      moving_sum += input[i];
    }
    moving_average = moving_sum / LENGTH;
    pc.printf("%f\n",moving_average);
    wait(1); //do the moving average @ 1Hz
  }
}

int main() {
  //float maxValue;            // Max FFT value is stored here
  //uint32_t maxIndex;         // Index in Output array where max value is
  pc.baud(9600);
  pc.printf("Starting ACF\r\n");
  adcThread.start(readSample);
  avgThread.start(movAvg);
}