# VITS text-to-speech API document

## Introduction

This is a readme about how to use the VITS API file.

## Prerequisites 

1. conda create -n soft_eng python=3.8

2. conda activate soft_eng

3. go to project8853-288/app/backend/vits

4. pip install -r requirements.txt 

   including these packages:

   ```
   Cython==0.29.21
   librosa==0.8.0
   matplotlib==3.3.1
   numpy==1.21.6
   phonemizer==2.2.1
   scipy==1.5.2
   Unidecode==1.1.1
   pypinyin==0.47.0
   pydub
   playsound
   pygame
   gtts
   torch
   sounddevice
   ```

5. python run _tts.py to test if VITS works

## Usage

_tts.py utilizes multiprocessing to split long sentences and generate audio concurrently, with better speech quality and faster synthesizing speed than simply inferencing the whole text.

```python
from _tts import VitsWrapper
vits = VitsWrapper()
my_string = "your_input_chinese_text"
vits.generate_audio_fast(new_string = my_string) #plays audio automaticly
```

## Trouble-shooting