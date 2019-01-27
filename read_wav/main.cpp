#include "mbed.h"
#include "arm_math.h"
#include "arm_common_tables.h"
#include "system_parameters.h"

#include "1.h"

//AnalogIn photocell(A0);
Serial serial (USBTX, USBRX);

int main()
{
    //Initialize variables
    uint16_t array_size=1024; //Function supports [32, 64, 128, ..., 4096]
    uint32_t block_size=1024;
    //int time[array_size];
    //int delay;
    float32_t voltage[array_size];
    float32_t output[array_size];
    float32_t output_mag[array_size];
    float32_t max_value;
    float32_t sample_frequency;
    float32_t string_frequency;
    uint32_t max_index;
    uint8_t ifftFlag=0;
    arm_rfft_fast_instance_f32 S;
    arm_rfft_fast_init_f32(&S, array_size);
    
    serial.baud(230400);
    
    //Read time & voltage levels and store in array
    for(int i=0; i<array_size; i++) {
        voltage[i]=wave_data[i];
        }
            
    //Compute real FFT of floating point    
    arm_rfft_fast_f32(&S,        //arm_rfft_fast_instance_f32 structure
                      voltage,   //input buffer. Gets modified during this calculation.
                      output,    //output buffer
                      ifftFlag); //RFFT if flag is 0, RIFFT if flag is 1
       
    //Compute magnitudes
    arm_cmplx_mag_f32(output,
                      output_mag,
                      array_size/2-1); //Number of samples in input vector
    
    //Handle special cases
    output_mag[0]=0; //output[0];
    output_mag[array_size/2]=output[1];
        
    //Find max bin and location of max (first half of bins as this is the only valid section)
    arm_max_f32(output_mag, block_size/2, &max_value, &max_index);
    serial.printf("Maximum signal amplitude is %f at index %i.\n",max_value,max_index);
    
    //Calculate frequency value
    sample_frequency=44100/220; // 44100/samples in between
    serial.printf("Sample frequency is %f Hz.\n",sample_frequency);
    string_frequency=max_index*sample_frequency/array_size;
    serial.printf("String frequency is %f Hz.\n",string_frequency);
    }