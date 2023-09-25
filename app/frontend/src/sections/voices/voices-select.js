import React, { useState, useRef } from 'react';
import { Card, Typography, Collapse, IconButton, Box, Stack,} from '@mui/material';
import { VoicesGrid } from './voices-grid';
import { VoicesCard } from './voices-card';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ExpandLessIcon from '@mui/icons-material/ExpandLess';

import { MenuItemCard } from './menuitem-card';
import { voices, attributes } from './constants';

export const VoicesSelect = ({setVoiceCardSelected}) => {
  const [expanded, setExpanded] = useState(true);
  const [selectedCardIndex, setSelectedCardIndex] = useState(null); // New state variable
  const currentlyPlayingAudioRef = useRef(null); 
  const [currentlyPlayingIndex, setCurrentlyPlayingIndex] = useState(null);

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  const handleCardClick = (index) => { // New function
    setSelectedCardIndex(index);
    setVoiceCardSelected(voices[index-1]);
    setExpanded(false);
  };

  return (
    <Card sx={{ p: 2, position: 'relative' }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Typography variant="h5" sx={{ color: 'text.primary', p: 1 }}>
          音色选择
        </Typography>
        <Box sx={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }} onClick={handleExpandClick}> 
          <Typography variant="body1" sx={{ marginRight: 0, color: 'text.secondary', p: 0 }}>
            {expanded ? null : selectedCardIndex !== null ? '更换音色' : '选择音色'}
          </Typography>
          <IconButton sx={{ position: 'relative' }}>
            {expanded ? <ExpandLessIcon /> : <ExpandMoreIcon />}
          </IconButton>
        </Box>
      </Box>
      {selectedCardIndex !== null && (
        <VoicesCard 
          key={selectedCardIndex}
          index={selectedCardIndex} 
          attributes={attributes} 
          playingAudioRef={currentlyPlayingAudioRef}
          currentlyPlayingIndex={currentlyPlayingIndex}
          setCurrentlyPlayingIndex={setCurrentlyPlayingIndex}
          />
        )}
      <Collapse in={expanded}>
        <Typography variant="body1" sx={{ color: 'text.secondary', p: 1 }}>
          音色列表
        </Typography>
        <Stack direction="row" spacing={2}>
          <MenuItemCard key={'Age'} label="年龄" menuItems={['全部', '青年', '成年']} />
          <MenuItemCard key={'Gender'}  label="性别" menuItems={['全部', '男性', '女性']} />
          <MenuItemCard key={'Accent'}  label="口音" menuItems={['全部', '普通话', '河南话']} />
          <MenuItemCard key={'Style'}  label="风格" menuItems={['全部', '普通', '播音']} />
          <MenuItemCard key={'Mood'}  label="心情" menuItems={['全部', '开心', '愤怒','难过']} />
        </Stack>
        <VoicesGrid 
        onCardClick={handleCardClick} // Pass down the function
        currentlyPlayingAudioRef={currentlyPlayingAudioRef} // Pass down the ref
        currentlyPlayingIndex={currentlyPlayingIndex}
        setCurrentlyPlayingIndex={setCurrentlyPlayingIndex}
        />
      </Collapse>
    </Card>
  );
};
