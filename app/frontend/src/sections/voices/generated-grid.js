import React from 'react';
import { Box,  Stack,  } from '@mui/material';
import { AudioCard } from './audio-card';

export const GeneratedGrid = ({ generatedCards }) => {

  return (
    <Box sx={{ p: 0, py:2 }}>
      <Stack spacing={2}>
      {generatedCards.map((card) => (
          <AudioCard
            key={card.id}
            voice={card.voice}
            text={card.text}
            noise={card.noise}
            noisew={card.noisew}
            sdp={card.sdp}
            length={card.length}
            audioURL={card.audioURL}
          />
        ))}
      </Stack>
    </Box>
  );
};
