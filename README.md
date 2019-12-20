# pitch-sensing
Fundamental frequency detection.

```
pitch-sensing
|   crepe_accuracy.py
|   crepe_latency.py
|   crepe_stream.py
|   pitch.py
|   PitchSense Demo.ipynb
|   README.md
|   requirements.txt
|
+---crepe
|       cli.py
|       core.py
|       model-full.h5
|       model-large.h5
|       model-medium.h5
|       model-small.h5
|       model-tiny.h5
|       version.py
|       __init__.py
|       __main__.py
|
+---FFT
|       fft.py
|
+---MATLAB
|       chromaticscale250summary05172019.mat
|       CytherSerialConnection.mlx
|       MPR_CREPE_Vis.m
|       Summaryfull.mat
|       wav_generator.m
|
+---notes
|       chromatic_scale.py
|       note_frequencies.py
|       random_frequencies.py
|       whamolaSample.txt
|
\---samples
    +---asc
    |       asc_1_120bpm.wav
    |       asc_1_60bpm.wav
    |       asc_2_120bpm.wav
    |       asc_2_60bpm.wav
    |       asc_3_120bpm.wav
    |       asc_3_60bpm.wav
    |
    +---desc
    |       desc_1_120bpm.wav
    |       desc_1_60bpm.wav
    |       desc_2_120bpm.wav
    |       desc_2_60bpm.wav
    |       desc_3_120bpm.wav
    |       desc_3_60bpm.wav
    |
    \---rand
            rand_1_120bpm.wav
            rand_1_60bpm.wav
            rand_2_120bpm.wav
            rand_2_60bpm.wav
            rand_3_120bpm.wav
            rand_3_60bpm.wav

```

### Instructions
```
git clone https://github.com/MPRlab/pitch-sensing.git
pip install -r requirements.txt
#Replace the installed CREPE library with the files in pitch-sensing/crepe

#Run CREPE for all model sizes, all timesteps (ms), and filters results by confidence level.
python crepe_accuracy.py

#Finds pitch detection latency for CREPE
python crepe_latency.py

#Runs CREPE continuously on audio stream
python crepe_stream.py

```

### Demo
[crepe_stream.py with Violin Scales](https://mega.nz/#!rllziKTS!yD-ATI3LJ8pJr6mXv2yKYUfZ2FFZhYduntcyLT3UGYY)