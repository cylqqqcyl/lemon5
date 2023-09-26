import React, { useState, useEffect } from 'react';
import { Card, Typography, Avatar, Box, IconButton } from '@mui/material';
import PlayIcon from '@mui/icons-material/PlayCircleOutline';
import PauseIcon from '@mui/icons-material/PauseCircleOutline';
import { voices, statusMap, voiceAvatarMap, voiceAudioMap } from './constants';
import { WordPill } from 'src/components/word-pill';

const VoicesCard = ({ index, attributes, onClick, currentlyPlayingIndex, setCurrentlyPlayingIndex, playingAudioRef }) => {
  const isPlaying = currentlyPlayingIndex === index; // Check if the card is playing
  const [audio, setAudio] = useState(null);
  const voicePath = voiceAudioMap[voices[index-1]];

  const handlePlayPauseClick = async (event) => {  // Make the function asynchronous
    event.stopPropagation();
  
    // Pause and reset any currently playing audio
    if (playingAudioRef.current) {
      playingAudioRef.current.pause();
      playingAudioRef.current.currentTime = 0;
      setCurrentlyPlayingIndex(null);
    }
  
    if (audio) {
      if (isPlaying) {
        audio.pause();
        setCurrentlyPlayingIndex(null);
      } else {
        await audio.play();  // Wait for the audio to start playing
        playingAudioRef.current = audio;
        setCurrentlyPlayingIndex(index);
      }
    } else {
      const newAudio = new Audio(voicePath);
      setAudio(newAudio);
      await newAudio.play();  // Wait for the audio to start playing
      playingAudioRef.current = newAudio;
      setCurrentlyPlayingIndex(index);
    }
  };
  

  // Create a useEffect to clean up the audio when the component is unmounted
  useEffect(() => {
    return () => {
      if (audio) {
        audio.pause();
        setAudio(null);
      }
    };
  }, [audio]);
  

  // Return the card component
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
};

// Export the VoicesCard component
export { VoicesCard };