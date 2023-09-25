import React, { useState, useEffect, useImperativeHandle } from 'react';
import { Card, Typography, Avatar, Box, IconButton } from '@mui/material';
import PlayIcon from '@mui/icons-material/PlayCircleOutline';
import PauseIcon from '@mui/icons-material/PauseCircleOutline';
import { WordPill } from 'src/components/word-pill';
import { voices, statusMap, voiceAvatarMap, voiceAudioMap } from './constants';

const VoicesCard = React.forwardRef(({ index, attributes, onClick, playingAudioRef }, ref) => {
  const [isPlaying, setIsPlaying] = useState(false);
  const [audio, setAudio] = useState(null);
  const voicePath = voiceAudioMap[voices[index - 1]];

  useImperativeHandle(ref, () => ({
    stopAudio: () => {
      if (audio) {
        audio.pause();
        setIsPlaying(false);
        setAudio(null);
      }
    }
  }));

  const handlePlayPauseClick = (event) => {
    console.log("Voice path being played:", voicePath);
    event.stopPropagation();

    if (audio) {
      audio.pause();
      setIsPlaying(false);
      setAudio(null);
      if (playingAudioRef.current === audio) {
        playingAudioRef.current = null;
      }
    } else {
      if (playingAudioRef.current) {
        playingAudioRef.current.pause();
      }
      const newAudio = new Audio(voicePath);
      setAudio(newAudio);
      newAudio.play();
      setIsPlaying(true);
      playingAudioRef.current = newAudio;
    }
  };

  useEffect(() => {
    return () => {
      if (audio) {
        audio.pause();
        setAudio(null);
      }
    };
  }, [audio]);

  return (
    <Card sx={{ p: 1, display: 'flex', justifyContent: 'left', alignItems: 'center', cursor: 'pointer', '&:hover': { backgroundColor: 'primary.lightest', boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' } }} onClick={onClick ? onClick : null}>
      <IconButton color={isPlaying ? 'success' : 'primary'} onClick={handlePlayPauseClick} sx={{ height: 45, width: 45, fontSize: '2.5rem' }}>
        {isPlaying ? <PauseIcon fontSize="inherit" /> : <PlayIcon fontSize="inherit" />}
      </IconButton>
      <Box sx={{ display: 'flex', alignItems: 'center' }}>
        <Avatar sx={{ height: 45, width: 45, bgcolor: isPlaying ? 'success.main' : 'primary.main' }} src={voiceAvatarMap[voices[index - 1]]} />
        <Box sx={{ marginLeft: 2 }}>
          <Typography variant="h6">{voices[index - 1]}</Typography>
          <Box sx={{ display: 'flex', gap: 1, pt: 1 }}>
            {Object.keys(attributes).map((key, i) => (<WordPill key={i} color={statusMap[key]}>{attributes[key]}</WordPill>))}
          </Box>
        </Box>
      </Box>
    </Card>
  );
});

export { VoicesCard };
