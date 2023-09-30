import React, {useState} from 'react';
import { Box, Button, Menu, MenuItem, Card, Avatar, Typography  } from '@mui/material';
import UnfoldMoreIcon from '@mui/icons-material/UnfoldMore';
import { voiceAvatarMap } from '../voices/constants';

export const CharacterSelect = ({ characters, selectedCharacter, onCharacterSelected }) => {
  const [anchorEl, setAnchorEl] = useState(null);
  const boxRef = React.useRef(null);

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = (item) => {
    setAnchorEl(null);
    if (item) {
        onCharacterSelected(item);  // Notify the parent component
    }
  };

  return (
    <Card sx={{ p: 2 }}>
      <Box ref={boxRef}
           sx={{ p: 0, width: '100%', alignItems: 'center', display: 'flex', justifyContent: 'space-between' }}>
        <Button
            id="demo-customized-button"
            aria-haspopup="true"
            variant="contained"
            onClick={handleClick}
            endIcon={<UnfoldMoreIcon />}
            sx={{ display: 'flex', width: '100%', justifyContent: 'space-between', alignItems: 'center', backgroundColor: 'neutral.100'}}
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
            <Typography variant="h6" sx={{ ml: 2, color: 'info.main' }}>
              选择对话的角色
            </Typography>
          )}
        </Button>
        <Menu
            anchorEl={anchorEl}
            open={Boolean(anchorEl)}
            onClose={() => handleClose(null)}
            PaperProps={{ style: { width: boxRef.current ? boxRef.current.offsetWidth : undefined } }}
        >
          {characters && characters.map((item, index) => (
            <MenuItem key={index} onClick={() => handleClose(item)}
                      sx={{ backgroundColor: item === selectedCharacter ? 'primary.lightest' : 'inherit',
                            color: 'inherit',
                            '&:hover': { backgroundColor: 'primary.light' }}}
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
  );
};
