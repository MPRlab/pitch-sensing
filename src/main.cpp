#include "mbed.h"
#include "yin.h"

/* MBED class APIs */
DigitalOut myled(LED1);
Serial     pc(USBTX, USBRX);
Thread     getADCShit;
Thread     acfThread;

int main() {
    //float maxValue;            // Max FFT value is stored here
    //uint32_t maxIndex;         // Index in Output array where max value is
    pc.baud(9600);
    pc.printf("Starting ACF\r\n");
    getADCShit.start(readSample);
    pc.printf("Started ADC\n");
    acfThread.start(FreqCalc);
    pc.printf("Threads worked.\n");

    return 0;
}