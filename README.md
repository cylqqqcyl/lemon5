# Lemon5 多媒体WEB应用

[![document](https://readthedocs.org/projects/lemon5/badge/?version=latest)](https://lemon5.readthedocs.io/zh/latest)

<img src=imgs/login.gif>

<img src=imgs/welcome-demo.gif>

本项目现为Web应用，前端使用react，后端使用Python Flask 框架。 

前端debug 模式启动方法：

```bash
cd app/frontend
npm install
npm run dev
```

1. Text-to-Speech
<img src=imgs/text2speech-demo.gif>

2. Voice Conversion
<img src=imgs/vc-demo.gif>

3. Voice Chat
<img src=imgs/chat-demo.gif>



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
   natsume>=1.0.0
   ```

5. python _tts.py to test if VITS works

<!-- 生成一个强调 -->
**注意：** 本项目使用pyside2-uic.exe编译.ui文件
