#include "mbed.h"
#include "yin.h"

/* MBED class APIs */
DigitalOut myled(LED1);
Serial     pc(USBTX, USBRX);
Ticker     getADCShit;
Thread     avgThread;

int main() {
  //float maxValue;            // Max FFT value is stored here
  //uint32_t maxIndex;         // Index in Output array where max value is
  pc.baud(9600);
  pc.printf("Starting ACF\r\n");
  getADCShit.attach_us(&readSample, PERIOD);
  avgThread.start(FreqCalc);
}