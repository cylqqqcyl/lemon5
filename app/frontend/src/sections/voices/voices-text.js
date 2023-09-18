import React, { useState, useEffect } from 'react';
import { Card, Typography, Collapse, IconButton, Box, OutlinedInput} from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ExpandLessIcon from '@mui/icons-material/ExpandLess';


export const VoicesText = ({voiceCardSelected, setTextInput}) => {
  const [expanded, setExpanded] = useState(false);
  const [inputText, setInputText] = useState(''); // State to hold the input text

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
      </Collapse>
    </Card>
  );
};
