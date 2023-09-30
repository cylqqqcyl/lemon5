import React, { useState, useEffect, useRef } from 'react';
import { Card, Typography, Box, IconButton, Slider, Stack } from '@mui/material';
import { styled, useTheme } from '@mui/material/styles';
import PlayIcon from '@mui/icons-material/PlayCircleOutline';
import PauseIcon from '@mui/icons-material/PauseCircleOutline';
import DownloadIcon from '@mui/icons-material/Download';
import { WordPill } from 'src/components/word-pill';

const TinyText = styled(Typography)({
    fontSize: '0.75rem',
    opacity: 0.38,
    fontWeight: 500,
    letterSpacing: 0.2,
});

export const AudioCard = ({ id, voice, text, audioURL, audioDuration, isGenerated }) => {
    const [isPlaying, setIsPlaying] = useState(false);
    const [duration, setDuration] = useState(0);
    const [position, setPosition] = useState(0);
    const audioRef = useRef(null);

    const handlePlayPauseClick = (event) => {
        if (isPlaying) {
            audioRef.current.pause();
        } else {
            audioRef.current.play();
        }
        setIsPlaying(!isPlaying);
    };

    useEffect(() => {
        const audio = audioRef.current;
        if (isPlaying) {
            audio.play();
        } else {
            audio.pause();
        }
    }, [isPlaying]);

    const handleDownload = () => {
      // Create a new anchor element
      const a = document.createElement("a");
  
      // Set the href and download attributes for the anchor element
      a.href = audioURL;
      a.download = text + ".wav";  // Set the downloaded file's name to the provided text with a ".wav" extension
  
      // Append the anchor to the body. This is required for the download to start.
      document.body.appendChild(a);
  
      // Trigger a click on the anchor
      a.click();
  
      // Remove the anchor from the body
      document.body.removeChild(a);
  };
  
    function formatDuration(value) {
        const minute = Math.floor(value / 60);
        const secondLeft = value - minute * 60;
        return `${minute}:${secondLeft < 10 ? `0${secondLeft}` : secondLeft}`;
    }

    return (
        <Card
            key={id}
            sx={{
                p: 1,
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                width: '100%',
            }}
        >
            <audio 
                ref={audioRef} 
                src={audioURL} 
                preload="auto" 
                onEnded={() => {setIsPlaying(false)
                  setPosition(audioDuration? audioDuration : audioRef.current.duration)
                }}
                onLoadedMetadata={() => {
                    setDuration(audioDuration? audioDuration : audioRef.current.duration);
                }}
                onTimeUpdate={() => {
                    setPosition(audioRef.current.currentTime);
                }}
            ></audio>

            <Box sx={{ display: 'flex', alignItems: 'center' }}>
                <IconButton 
                    color={isPlaying ? 'success' : 'primary'}
                    onClick={handlePlayPauseClick}
                    sx={{
                        height: 45,
                        width: 45,
                        fontSize: '2.5rem'
                    }}
                >
                    {isPlaying ? <PauseIcon fontSize="inherit" /> : <PlayIcon fontSize="inherit" />}
                </IconButton>
                { isGenerated && (
                <Box sx={{ marginLeft: 2 }}>
                    <Typography variant="body1" sx={{ color: 'text.primary'}}>
                        {text}
                    </Typography>
                    <Box sx={{ gap: 0, pt: 2 }}>
                        <WordPill color={'info'}>{voice}</WordPill>
                    </Box>
                </Box>
                )}

                { !isGenerated && (
                <Box sx={{ marginLeft: 1 }}>
                    <Typography variant="body1" sx={{ color: 'text.primary'}}
                    style={{ wordWrap: 'break-word', maxWidth: '100%' }}>
                        {text}
                    </Typography>
                </Box>
                )}
            </Box>
            <Box sx={{ display: 'flex', alignItems: 'center'}}>
                <Stack sx={{ display: 'flex', alignItems: 'center', pr: 2 }}>
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
                { isGenerated && (
                <IconButton onClick={handleDownload} sx={{ marginRight: 1 }}>
                    <DownloadIcon />
                </IconButton>
                )}
            </Box>
        </Card>
    );
};
