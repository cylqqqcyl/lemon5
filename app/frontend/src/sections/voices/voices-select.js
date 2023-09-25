import React, { useState } from 'react';
import { Card, Typography, Collapse, IconButton, Box, Stack, Button, Menu, MenuItem } from '@mui/material';
import { VoicesGrid } from './voices-grid';
import { VoicesCard } from './voices-card';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ExpandLessIcon from '@mui/icons-material/ExpandLess';
import UnfoldMoreIcon from '@mui/icons-material/UnfoldMore';

import { voices, attributes } from './constants';

// Function to render each menu item
const MenuItemCard = ({ label, menuItems }) => {
  const [anchorEl, setAnchorEl] = useState(null);
  const boxRef = React.useRef(null); // Create a ref to attach to the Box
  const [selectedItem, setSelectedItem] = useState(menuItems[0]);  // New state variable

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = (item) => {
    setAnchorEl(null);
    if (item){
        setSelectedItem(item);
    }
  };

  return (
    <Box ref={boxRef}  // Attach the ref to the Box
    sx={{ p: 0, width: '100%', alignItems: 'center', display: 'flex', justifyContent: 'space-between' }}>
        <Button
            id="demo-customized-button"
            aria-controls={open ? 'demo-customized-menu' : undefined}
            aria-haspopup="true"
            aria-expanded={open ? 'true' : undefined}
            variant="contained"
            onClick={handleClick}
            endIcon={<UnfoldMoreIcon />}
            sx={{ display: 'flex', width: '100%', justifyContent: 'space-between', alignItems: 'center',  
        backgroundColor: 'neutral.100'}}
        >
            {selectedItem==menuItems[0] ? label : selectedItem}
        </Button>
          <Menu
            anchorEl={anchorEl}
            open={Boolean(anchorEl)}
            onClose={() => handleClose(null)}
            PaperProps={{ style: { width: boxRef.current ? boxRef.current.offsetWidth : undefined }, }}  
          >
            {menuItems.map((item, index) => (
              <MenuItem key={index} onClick={() => handleClose(item)}
              sx={{ backgroundColor: item === selectedItem ? 'primary.lightest' : 'inherit', 
              color:'inherit',
              '&:hover': { backgroundColor: 'primary.light'}}}
              >
                {item}
              </MenuItem>
            ))}
          </Menu>
      </Box>
  );
};

export const VoicesSelect = ({setVoiceCardSelected}) => {
  const [expanded, setExpanded] = useState(true);
  const [selectedCardIndex, setSelectedCardIndex] = useState(null); // New state variable

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
          <VoicesCard index={selectedCardIndex} attributes={attributes} />
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
        selectedCardIndex={selectedCardIndex} // Pass down the state
        onCardClick={handleCardClick} // Pass down the function
        />
      </Collapse>
    </Card>
  );
};
