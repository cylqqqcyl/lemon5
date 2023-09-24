import React from 'react';
import { Box,  Stack,  } from '@mui/material';
import { GeneratedCard } from './generated-card';

export const GeneratedGrid = ({ generatedCards }) => {

  return (
    <Box sx={{ p: 0, py:2 }}>
      <Stack spacing={2}>
      {generatedCards.map((card) => (
          <GeneratedCard 
            key={card.id}
            voice={card.voice}
            text={card.text} 
            audioUrl={card.audioUrl}
          />
        ))}
      </Stack>
    </Box>
  );
};
