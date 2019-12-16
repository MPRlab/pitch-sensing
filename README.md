# pitch-sensing
Fundamental frequency detection.

```
pitch-sensing
|   creper.py
|   crepe_injection.py
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
\---notes
        chromatic_scale.py
        note_frequencies.py
        random_frequencies.py
        whamolaSample.txt
```

### Instructions
```
git clone https://github.com/MPRlab/pitch-sensing.git
pip install -r requirements.txt
#Replace the installed CREPE library with the files in pitch-sensing/crepe

#Run CREPE for all model sizes, all timesteps (ms), and filters results by confidence level.
python creper.py

#Finds pitch detection latency for CREPE
python crepe_injection.py

#Runs CREPE continuously on audio stream
python crepe_stream.py

```

### Demo
[crepe_stream.py with Violin Scales](https://mega.nz/#!rllziKTS!yD-ATI3LJ8pJr6mXv2yKYUfZ2FFZhYduntcyLT3UGYY)