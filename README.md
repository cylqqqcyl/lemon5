# Lemon4 多媒体工具箱

1. TextToSpeech
<img src=imgs/text2speech.png>

2. VoiceConversion
<img src=imgs/voiceConversion.png>

3. AudioDenoise
<img src=imgs/Denoising.png>

4. ImageRefinement
<img src=imgs/ImageRefinement.png>



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
   PySide2
   PyQT5
   ```

5. python _tts.py to test if VITS works



<!-- 生成一个强调 -->
**注意：** 本项目使用pyside2-uic.exe编译.ui文件
