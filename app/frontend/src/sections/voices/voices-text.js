import React, { useState, useEffect, useRef } from 'react';
import { Card, Typography, Collapse, 
        IconButton, Box, OutlinedInput, 
        Menu, MenuItem, Button} from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ExpandLessIcon from '@mui/icons-material/ExpandLess';
import { ParameterCard } from './parameter-card';
import UnfoldMoreIcon from '@mui/icons-material/UnfoldMore';


const formats = [ 'wav', 'mp3']

export const VoicesText = ({voiceCardSelected, setTextInput,
                            sdpValue, setSdpValue,
                            emotionValue, setEmotionValue,
                            lengthValue, setLengthValue,
                            speedValue, setSpeedValue,
                            setFormatValue
}) => {
  const [expanded, setExpanded] = useState(false);
  const [inputText, setInputText] = useState(''); // State to hold the input text
  const [anchorEl, setAnchorEl] = useState(null); 
  const [selectedFormat, setSelectedFormat] = useState(null);


  const boxRef = useRef(null); // Create a ref to attach to the Box
  
  const handleMenuClick = (event) => {
  setAnchorEl(event.currentTarget);
};

const handleMenuClose = (item) => {
  setAnchorEl(null);
  if (item){
      setSelectedFormat(item);
      setFormatValue(item);
  }
};

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  const handleInputChange = (event) => {
    setInputText(event.target.value); // Update the state with the new input
    if (event.target.value) {
      setTextInput(event.target.value);
    } else {
        setTextInput('');
        }
  };

  useEffect(() => {
    if (voiceCardSelected) {
      setExpanded(true);
    }
  }, [voiceCardSelected]);

  return (
    <Card sx={{ p: 2, position: 'relative' }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Typography variant="h5" sx={{ color: 'text.primary', p: 1 }}>
          文本框
        </Typography>
        <Box sx={{ display: 'flex', alignItems: 'center', cursor: 'pointer' }} onClick={handleExpandClick}>
          <Typography variant="body1" sx={{ marginRight: 0, color: 'text.secondary', p: 0 }}>
            {expanded ? null : inputText ? '修改文本' : '输入文本'}
          </Typography>
          <IconButton onClick={handleExpandClick} sx={{ position: 'relative' }}>
            {expanded ? <ExpandLessIcon /> : <ExpandMoreIcon />}
          </IconButton>
        </Box>
      </Box>
      {!expanded && inputText && ( 
        <Typography variant="body2" sx={{ color: 'text.secondary', p: 1 }}>
          {inputText}
        </Typography>
      )}
      <Collapse in={expanded}>
      <Typography variant="body1" sx={{ color: 'text.secondary', p: 1 }}>
          输入你想转为语音的文本
      </Typography>
      <OutlinedInput
          multiline
          rows={4}
          placeholder="在这里输入文本"
          value={inputText}
          onChange={handleInputChange} // Handle input changes
          sx={{ width: '100%'}}
        />
        <Typography variant="body1" sx={{ color: 'text.secondary', p: 1,mb:-2 }}>
          调整参数
      </Typography>
      <ParameterCard description="SDP/DP混" min={0.1} max={0.9} step={0.1} 
      defaultValue={sdpValue} onChange={setSdpValue} />
      <ParameterCard description="感情" min={0.2} max={1.1} step={0.1}
      defaultValue={emotionValue} onChange={setEmotionValue} />
      <ParameterCard description="音素长度" min={0.6} max={1.4} step={1}
      defaultValue={lengthValue} onChange={setLengthValue} />
      <ParameterCard description="语速" min={0.6} max={1.9} step={0.1}
      defaultValue={speedValue} onChange={setSpeedValue} />
      <Typography variant="body1" sx={{ color: 'text.secondary', p: 1,mb:-2 }}>
          输出格式
      </Typography>
      <Box ref={boxRef}  // Attach the ref to the Box
      sx={{ p: 0, width: '100%', alignItems: 'center', display: 'flex', justifyContent: 'space-between' }}>
          <Button
            id="demo-customized-button"
            aria-controls={open ? 'demo-customized-menu' : undefined}
            aria-haspopup="true"
            aria-expanded={open ? 'true' : undefined}
            variant="contained"
            onClick={handleMenuClick}
            endIcon={<UnfoldMoreIcon />}
            sx={{ display: 'flex', width: '100%', justifyContent: 'space-between', alignItems: 'center'
          ,backgroundColor: 'neutral.50',p:2,mt:2}}
        >
            {selectedFormat ? selectedFormat : formats[0]}
        </Button>
          <Menu
            anchorEl={anchorEl}
            open={Boolean(anchorEl)}
            onClose={() => handleMenuClose(null)}
            PaperProps={{ style: { width: boxRef.current ? boxRef.current.offsetWidth : undefined }, }}  
          >
            {formats.map((format, index) => (
              <MenuItem key={index} onClick={() => handleMenuClose(format)}
              sx={{ backgroundColor: format === selectedFormat ? 'primary.lightest' : 'inherit', 
              color:'inherit',
              '&:hover': { backgroundColor: 'primary.light'}}}
              >
                {format}
              </MenuItem>
            ))}
          </Menu>
      </Box>

      </Collapse>
    </Card>
  );
};

