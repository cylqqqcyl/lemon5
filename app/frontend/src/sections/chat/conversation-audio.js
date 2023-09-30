import React, { useState, useEffect, useRef } from 'react';
import { Typography, Box,  Divider, Stack } from '@mui/material';
import { styled } from '@mui/material/styles';
import Wifi1Bar from '@mui/icons-material/Wifi1Bar';
import Wifi2Bar from '@mui/icons-material/Wifi2Bar';
import Wifi3Bar from '@mui/icons-material/Wifi';


const TinyText = styled(Typography)({
    fontSize: '0.75rem',
    opacity: 0.38,
    fontWeight: 500,
    letterSpacing: 0.2,
});

export const ConversationAudio = ({ id , audioURL, audioDuration }) => {
    const [isPlaying, setIsPlaying] = useState(false);
    const [wifiBars, setWifiBars] = useState(3);
    const [duration, setDuration] = useState(0);
    const [position, setPosition] = useState(0);

    // debug
    // const duration = 200; // seconds
    // const [position, setPosition] = useState(32); 

    const audioRef = useRef(null);

    let intervalId = null;

    const handlePlayPauseClick = (event) => {
        if (isPlaying) {
            audioRef.current.pause();
        } else {
            audioRef.current.play();
        }
        setIsPlaying(!isPlaying);
    };

    useEffect(() => {
        if (isPlaying) {
          intervalId = setInterval(() => {
            setWifiBars((prevWifiBars) => (prevWifiBars === 3 ? 1 : prevWifiBars + 1));
          }, 500);
        } else {
          setWifiBars(3);
          clearInterval(intervalId);
        }
    
        return () => {
          setWifiBars(3);
          clearInterval(intervalId);
        };
      }, [isPlaying]);
    
      const getWifiIcon = () => {
        switch (wifiBars) {
          case 1:
            return <Wifi1Bar fontSize="inherit" sx={{rotate: '90deg'}} />
          case 2:
            return <Wifi2Bar fontSize="inherit" sx={{rotate: '90deg'}} />
          case 3:
            return <Wifi3Bar fontSize="inherit" sx={{rotate: '90deg'}} />
          default:
            return <Wifi3Bar fontSize="inherit" sx={{rotate: '90deg'}} />
        }
      };

    useEffect(() => {
        const audio = audioRef.current;
        if (isPlaying) {
            audio.play();
        } else {
            audio.pause();
        }
    }, [isPlaying]);
  
    function formatDuration(value) {
        const minute = Math.floor(value / 60);
        const secondLeft = value - minute * 60;
        return `${minute}'${secondLeft < 10 ? `0${secondLeft}` : secondLeft}''`;
    }

    return (
        <Box
            key={id}
            sx={{
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'space-between',
                alignItems: 'center',
                mb: 1,
            }}
        >
            <Box
            sx={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            width: '100%',  // Make sure it takes full width
            }}
        >
                <audio 
                    ref={audioRef} 
                    src={audioURL} 
                    preload="auto" 
                    onEnded={() => setIsPlaying(false)}
                    onLoadedMetadata={() => {
                        setDuration(audioDuration ? audioDuration : audioRef.current.duration);
                    }}
                    onTimeUpdate={() => {
                        setPosition(audioRef.current.currentTime);
                    }}
                ></audio>

                <Box
                    sx={{
                        display: 'flex',
                        alignItems: 'center',
                        cursor: 'pointer', // Add cursor pointer
                        }}
                        onClick={handlePlayPauseClick} // Move onClick here
                >
                    {getWifiIcon()}
                    <TinyText>{formatDuration(Math.ceil(duration))}</TinyText>
                </Box>
            </Box>
            <Divider sx={{ mt:1, width: '100%' }} />  {/* Add Divider here */}
        </Box>
    );
};
