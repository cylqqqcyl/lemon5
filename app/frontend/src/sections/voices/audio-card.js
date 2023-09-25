import React, { useState, useEffect } from 'react';
import { Card, Typography, Box, IconButton, Slider, Stack } from '@mui/material';
import { styled, useTheme } from '@mui/material/styles';
import PlayIcon from '@mui/icons-material/PlayCircleOutline';
import PauseIcon from '@mui/icons-material/PauseCircleOutline';

const TinyText = styled(Typography)({
    fontSize: '0.75rem',
    opacity: 0.38,
    fontWeight: 500,
    letterSpacing: 0.2,
  });

export const AudioCard = ({ source }) => {
  const [isPlaying, setIsPlaying] = useState(false);  // State to manage play/pause
  const duration = 200; // seconds
  const [position, setPosition] = useState(32); // seconds

  // Function to handle play/pause button click
  const handlePlayPauseClick = (event) => {
    event.stopPropagation();  // Prevent card click event from firing
    setIsPlaying(!isPlaying);  // Toggle state
    //  play/pause logic here
  };


  function formatDuration(value) {
    const minute = Math.floor(value / 60);
    const secondLeft = value - minute * 60;
    return `${minute}:${secondLeft < 10 ? `0${secondLeft}` : secondLeft}`;
  }

  useEffect(() => {
    let newTimer = null; // Local variable to hold the timer
  
    if (isPlaying) {
      // Start the timer if the audio is playing
      newTimer = setInterval(() => {
        setPosition((prevPosition) => {
          if (prevPosition >= duration) {
            // Reached the end, pause the audio
            setIsPlaying(false);
            clearInterval(newTimer); // Clear the timer
            return duration; // Set position to the duration
          }
          return Math.min(prevPosition + 0.1, duration); // Otherwise, update the position
        });
      }, 100); // Update every 100 milliseconds
    } else {
      // Clear the timer if the audio is paused
      if (newTimer) {
        clearInterval(newTimer);
      }
    }
  
    // Cleanup: Clear the timer when the component is unmounted
    return () => {
      if (newTimer) {
        clearInterval(newTimer);
      }
    };
  }, [isPlaying, duration]);  

  return (
    <Card 
    key={'audio-card'}
    sx={{ p: 1, 
      display: 'flex', 
      justifyContent: 'space-between',
      alignItems: 'center', 
      width: '100%',
    }}
    >
    <Box sx={{ display: 'flex', alignItems: 'center' }}>
      <IconButton color= {isPlaying ? 'success' : 'primary'}
          onClick={handlePlayPauseClick} 
          sx={{
            height: 45,
            width: 45, 
            fontSize: '2.5rem'
          }}
      >
        {isPlaying ? <PauseIcon fontSize="inherit" /> : <PlayIcon fontSize="inherit" />}
      </IconButton>
        <Box sx={{ ml: 1,mr: 2}}>
            <Typography variant="body1" sx={{ color: 'text.primary'}}>
            {source}
            </Typography>
        </Box>
    </Box>
    <Box sx={{ display: 'flex', alignItems: 'center'}}>
      <Stack sx={{ display: 'flex', alignItems: 'center', pr:2 }}>
        <Slider
          aria-label="time-indicator"
          size="small"
          value={position}
          min={0}
          step={1}
          max={duration}
          onChange={(_, value) => setPosition(value)}
          sx={{
            width: 400,
            height: 4,
            borderRadius: 2,
            alignItems: 'center',
          }}
        />
        <Box
          sx={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            width: '100%'
          }}
        >
          <TinyText>{formatDuration(Math.round(position))}</TinyText>
          <TinyText>-{formatDuration(Math.round(duration - position))}</TinyText>
        </Box>
        </Stack>
    </Box>
    </Card>
  );
};
