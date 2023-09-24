import React, {useState} from 'react';
import { Box, Button, Menu, MenuItem, Card, Avatar, Typography  } from '@mui/material';
import UnfoldMoreIcon from '@mui/icons-material/UnfoldMore';

const voiceAvatarMap = {
  '派蒙': '/assets/avatars/paimeng.png',
  '可莉': '/assets/avatars/keli.png',
  '甘雨': '/assets/avatars/ganyu.png',
  '刻晴': '/assets/avatars/keqing.png',
  '申鹤': '/assets/avatars/shenhe.png'
};


export const CharacterSelect = ({ characters }) => {

  const [anchorEl, setAnchorEl] = useState(null);
  const boxRef = React.useRef(null); // Create a ref to attach to the Box
  const [selectedCharacter, setSelectedCharacter] = useState(null);  // New state variable

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = (item) => {
    setAnchorEl(null);
    if (item){
        setSelectedCharacter(item);
    }
  };

  return (
  <Card sx={{ p: 2 }}>
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
            {selectedCharacter ? (
            <>
              <Avatar sx={{ height: 45, width: 45, bgcolor: 'primary.main' }} 
              src={voiceAvatarMap[selectedCharacter]} />
              <Typography variant="h6" sx={{ ml: 2, color: 'info.main' }}>
              {selectedCharacter}
              </Typography>
            </>
          ) : (
            <Typography variant="h6" sx={{ ml: 2, color: 'info.main'  }}>
            选择对话的角色
            </Typography>
          )}
        </Button>
          <Menu
            anchorEl={anchorEl}
            open={Boolean(anchorEl)}
            onClose={() => handleClose(null)}
            PaperProps={{ style: { width: boxRef.current ? boxRef.current.offsetWidth : undefined }, }}  
          >
            {characters && characters.map((item, index) => (
              <MenuItem key={index} onClick={() => handleClose(item)}
              sx={{ backgroundColor: item === selectedCharacter ? 'primary.lightest' : 'inherit', 
              color:'inherit',
              '&:hover': { backgroundColor: 'primary.light'}}}
              >
               <Avatar
                  sx={{
                    height: 45,
                    width: 45,
                    mr: 2,
                  }}
                  src={voiceAvatarMap[item]}
                />
                <Typography variant="h6" sx={{ color: 'inherit' }}>
                {item}
                </Typography>
              </MenuItem>
            ))}
          </Menu>
      </Box>
  </Card>
  )
};
