import React, { useState } from 'react';
import { Box, Button, Menu, MenuItem } from '@mui/material';
import UnfoldMoreIcon from '@mui/icons-material/UnfoldMore';


// Function to render each menu item
export const MenuItemCard = ({ label, menuItems }) => {
    const [anchorEl, setAnchorEl] = useState(null);
    const boxRef = React.useRef(null); // Create a ref to attach to the Box
    const [selectedItem, setSelectedItem] = useState(menuItems[0]);  
  
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