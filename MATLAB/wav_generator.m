% Generates .wav audio files across specified bandwidth

fp='G:\WPI\MPR Lab\Cyther\CREPE\SineWaves\';
Fs=16000; %Hz, CREPE sample rate
t=0:1/Fs:2; %seconds
f_min=20; f_max=20000; f_step=100; %Hz

for f=f_min:f_step:f_max
    y=sin(2*pi*f*t);
    audiowrite(strcat(fp,num2str(f),'.wav'),y,Fs);
end