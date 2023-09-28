# Singing Voice Conversion


## Format

Output audio is saved in the sampling format of `dbl`. To convert it to `s16` format, use the command below.

```bash
ffmpeg -i input.wav -acodec pcm_s16le output.wav
```

## Mix vocal and accompaniment

```bash
ffmpeg -i input1.wav -i input2.wav -filter_complex "[0:a]atrim=0:duration=287[a1]; [1:a]atrim=0:duration=287[a2]; [a1][a2]amix=inputs=2:duration=first:dropout_transition=2[out]" -map "[out]" output.wav
```

Change `duration` to match your own files.

