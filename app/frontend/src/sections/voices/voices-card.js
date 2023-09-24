import React, {useState} from 'react';
import { Card, Typography, Avatar, Box, IconButton } from '@mui/material';
import PlayIcon from '@mui/icons-material/PlayCircleOutline';
import PauseIcon from '@mui/icons-material/PauseCircleOutline';
import { WordPill } from 'src/components/word-pill';

const statusMap = {
  age: 'warning',
  gender: 'success',
  accent: 'error',
  style: 'info',
  mood: 'primary'
};

export const SelectedVoiceCard = ({ index, attributes }) => {
  const [isPlaying, setIsPlaying] = useState(false);  // State to manage play/pause

  // Function to handle play/pause button click
  const handlePlayPauseClick = (event) => {
    event.stopPropagation();  // Prevent card click event from firing
    setIsPlaying(!isPlaying);  // Toggle state
    //  play/pause logic here
  };

  return (
    <Card sx={{ p: 1, display: 'flex', justifyContent: 'left', alignItems: 'center'}}>
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
      <Box sx={{ display: 'flex', alignItems: 'center' }}>
        <Avatar
            sx={{
              height: 45,
              width: 45,
              bgcolor: isPlaying ? 'success.main' : 'primary.main',
            }}
          src="/assets/avatars/paimeng.png"
        />
        <Box sx={{ marginLeft: 2 }}>
          <Typography variant="h6">派蒙 {index}</Typography>
          <Box sx={{ display: 'flex', gap: 1, pt:1 }}>
            {Object.keys(attributes).map((key, i) => (
              <WordPill key={i} color={statusMap[key]}>{attributes[key]}</WordPill>
            ))}
          </Box>
        </Box>
      </Box>
    </Card>
  );
};

export const VoicesCard = ({ index, page, rowsPerPage, attributes, onClick }) => {
  const [isPlaying, setIsPlaying] = useState(false);  // State to manage play/pause

  // Function to handle play/pause button click
  const handlePlayPauseClick = (event) => {
    event.stopPropagation();  // Prevent card click event from firing
    setIsPlaying(!isPlaying);  // Toggle state
    //  play/pause logic here
  };

  return (
    <Card sx={{ p: 1, 
      display: 'flex', 
      justifyContent: 'left', 
      alignItems: 'center', 
      cursor: 'pointer',  // Change cursor to pointer on hover
      '&:hover': {  // Hover effect
        backgroundColor: 'primary.lightest',
        boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)'
    }}}
      onClick={onClick}
    >
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
      <Box sx={{ display: 'flex', alignItems: 'center' }}>
        <Avatar
            sx={{
              height: 45,
              width: 45,
              bgcolor: isPlaying ? 'success.main' : 'primary.main',
            }}
          src="/assets/avatars/paimeng.png"
        />
        <Box sx={{ marginLeft: 2 }}>
          <Typography variant="h6">派蒙 {index + 1 + (page - 1) * rowsPerPage}</Typography>
          <Box sx={{ display: 'flex', gap: 1, pt:1 }}>
            {Object.keys(attributes).map((key, i) => (
              <WordPill key={i} color={statusMap[key]}>{attributes[key]}</WordPill>
            ))}
          </Box>
        </Box>
      </Box>
    </Card>
  );
};
