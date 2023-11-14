import React, { useState, useRef, useEffect } from 'react';
import { Card, Typography, Collapse, IconButton, Box, Stack,} from '@mui/material';
import { VoicesGrid } from './voices-grid';
import { VoicesCard } from './voices-card';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ExpandLessIcon from '@mui/icons-material/ExpandLess';
import { MenuItemCard } from './menuitem-card';

export const VoicesSelect = ({setVoiceCardSelected, searchText}) => {
  const [expanded, setExpanded] = useState(true);
  const [selectedCardIndex, setSelectedCardIndex] = useState(null); // New state variable
  const currentlyPlayingAudioRef = useRef(null);
  const [currentlyPlayingIndex, setCurrentlyPlayingIndex] = useState(null); 
  const [voices, setVoices] = useState([]);
  const [selectedElement, setSelectedElement] = useState('');
  const [selectedStyle, setSelectedStyle] = useState('');

  const handleElementSelect = (element) => {
    setSelectedElement(element);
  };
  
  const handleStyleSelect = (style) => {
    setSelectedStyle(style);
  };
  

  useEffect(() => {
    // Fetch voices data from server
    const url = new URL(`${process.env.NEXT_PUBLIC_BACKEND_URL}/voices`);
  
    if (searchText) {
      url.searchParams.append('name', searchText); // Append searchText as a query parameter
    }
    if (selectedElement&&selectedElement!=='全部') { 
      url.searchParams.append('element', selectedElement);
    }
    if (selectedStyle&&selectedStyle!=='全部') {
      url.searchParams.append('style', selectedStyle);
    } 
    fetch(url)
      .then(response => response.json())
      .then(data => {
        //set selected card index to null when data changes
        setSelectedCardIndex(null);
        setVoices(data);  
      })
      .catch(error => {
        console.error('Error fetching voices data:', error);
      });
  }, [searchText, selectedElement, selectedStyle]);

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
          key={selectedCardIndex} // Pass the key down
          voice={voices[selectedCardIndex-1]} // Pass the voice object down
          playingAudioRef={currentlyPlayingAudioRef} // Pass the ref down
          currentlyPlayingIndex={currentlyPlayingIndex} // Pass the state variable down
          setCurrentlyPlayingIndex={setCurrentlyPlayingIndex} // Pass the state setter down
          />
        )}
      <Collapse in={expanded}>
        <Typography variant="body1" sx={{ color: 'text.secondary', p: 1 }}>
          音色列表
        </Typography>
        <Stack direction="row" spacing={2}>
          <MenuItemCard key={'Element'} label="元素" 
          menuItems={['全部','无', '火', '水', '雷', '冰', '草']} 
          onItemSelect={handleElementSelect}
          />
          <MenuItemCard key={'Style'}  label="风格" 
          menuItems={['全部','萝莉音','少女音','御姐音','烟嗓']} 
          onItemSelect={handleStyleSelect}
          />
        </Stack>
        <VoicesGrid 
        onCardClick={handleCardClick} // Pass down the function
        currentlyPlayingAudioRef={currentlyPlayingAudioRef} // Pass down the ref
        voices={voices}
        setCurrentlyPlayingIndex={setCurrentlyPlayingIndex}
        currentlyPlayingIndex={currentlyPlayingIndex}
        />
      </Collapse>
    </Card>
  );
};
