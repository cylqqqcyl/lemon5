import React, {useState} from 'react';
import { Card, Box, Button,
    Typography, Avatar, 
    OutlinedInput, InputAdornment, 
    IconButton, ToggleButton, ToggleButtonGroup } from '@mui/material';
import UserIcon from '@mui/icons-material/Person';
import SendIcon from '@mui/icons-material/Send';
import NewConvIcon from '@mui/icons-material/Add';
import { RecordCard } from '../voices/record-card';
import { CustomSnackbar } from '../message/custom-snackbar';

import { voiceAvatarMap } from '../voices/constants';

export const ConversationCard = ({ messages, setMessages, selectedCharacter }) => {
    const [inputValue, setInputValue] = useState('');  // State to keep track of input value
    const [inputMode, setInputMode] = useState('text');  // State to track input mode
    const [recording, setRecording] = useState(false);  // State to track recording status
    const [snackbarConfig, setSnackbarConfig] = useState({ message: '', type: '' });

    const handleInputChange = (event) => {
        setInputValue(event.target.value);  // Update input value
    };

      const handleSendClick = async () => {
        setSnackbarConfig({ message: '', type: '' });
        const newMessage = {
          sender: 'user',
          text: inputValue,
        };
    
        // 先将用户的消息添加到对话中
        setMessages([...messages, newMessage]);

        // 重置输入值
        setInputValue('');
    
        // 向后端发送请求
        try {
          const response = await fetch('https://460dc553.r11.cpolar.top/chat', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
              prompt: inputValue,
              character: selectedCharacter
            }),
          });
    
          const responseData = await response.json();
    
          if (responseData && responseData.response) {
            const botMessage = {
              sender: responseData.character || 'Bot',  // 此处需要确定后端返回的角色字段名
              text: responseData.response,
            };
            setMessages((prevMessages) => [...prevMessages, botMessage]);
          }
    
        } catch (error) {
          console.error('Error sending message:', error);
          setSnackbarConfig({ message: 'Error sending message:', type: 'error' });
        }
    
    };
  
    const handleNewConvClick = () => {
        // Handle new conversation button click
        setMessages([]);  // Clear messages
      };

    const handleRecordClick = () => {
        setRecording(!recording)
        if (recording) {
          setInputValue('录制音频');
        }
      };

    const handleModeChange = (event, newMode) => {
        if (newMode !== null) {
          setInputMode(newMode);  // Update input mode
        }
      };

  return (
    <Card sx={{ p: 2, mt: 3 }}>
      {snackbarConfig.message && <CustomSnackbar message={snackbarConfig.message} type={snackbarConfig.type} />}
      {messages.length !== 0 && (
          <IconButton
              variant="outlined"
              edge="end"
              onClick={handleNewConvClick}
              borderColor="success.main"
              sx={{borderRadius: '15px', border: '2px solid', borderColor: 'success.main', color: 'success.main'}}
            >
              <NewConvIcon />
              <Typography variant="body2" sx={{fontWeight:'bold'}}>新对话</Typography>
          </IconButton>
      )}
      <Box sx={{ display: 'flex', flexDirection: 'column' }}>
        {messages.map((message, index) => (
          <Box
            key={index}
            sx={{
              mb: 1,
              display: 'flex',
              flexDirection: message.sender === 'user' ? 'row-reverse' : 'row',
              alignItems: 'center',
            }}
          >
            {message.sender !== 'user' && (
              <Avatar sx={{ height: 45, width: 45, bgcolor: 'primary.main' }} 
               src={voiceAvatarMap[message.sender]} />
            )}
            {message.sender === 'user' && (
              <Avatar sx={{ height: 45, width: 45, bgcolor: 'primary.main' }}>
              <UserIcon />
            </Avatar>
            )}
            <Box
              sx={{
                p: 1,
                borderRadius: 1,
                backgroundColor: message.sender === 'user' ? 'primary.light' : 'grey.300',
                mx: 1,
              }}
            >
              <Typography variant="body2">{message.text}</Typography>
            </Box>
          </Box>
        ))}
        
        <ToggleButtonGroup
        value={inputMode}
        exclusive
        onChange={handleModeChange}
        color="success"
        sx={{ alignSelf: 'flex-start', mt: 2 }}
      >
        <ToggleButton
          value="text"
          aria-label="text input"
          sx={{
            backgroundColor: inputMode === 'text' ? 'success.light' : 'primary.lightest',
            color: inputMode === 'text' ? 'info.main' : 'info.light',
            '&:hover': {
              backgroundColor: inputMode === 'text' ? 'success.darkest' : 'success.lightest',
            }
          }}
        >
          文字输入
        </ToggleButton>
        <ToggleButton
          value="audio"
          aria-label="audio input"
          sx={{
            backgroundColor: inputMode === 'audio' ? 'success.light' : 'primary.lightest',
            color: inputMode === 'audio' ? 'info.main' : 'info.light',
            '&:hover': {
              backgroundColor: inputMode === 'audio' ? 'success.darkest' : 'success.lightest',
            }
          }}
        >
          语音输入
        </ToggleButton>
      </ToggleButtonGroup>
      </Box>

      {inputMode === 'text' && (
        <OutlinedInput
        defaultValue=""
        value={inputValue}
        onChange={handleInputChange}
        fullWidth
        placeholder="发送信息"
        endAdornment={(
            <InputAdornment position="end"
            sx={{ p: 1,ml:3 }}>
              <IconButton
              variant="contained"
              edge="end"
              onClick={handleSendClick}
              disabled={!inputValue}  // Disable button if inputValue is empty
              sx={{borderRadius: '15px',mr:1,
                backgroundColor: inputValue ? 'success.main' : 'grey.300',  // Conditional background color
                color: 'white',
                '&:hover': {
                  backgroundColor: inputValue ? 'success.dark' : 'grey.400',
                }
              }}
            >
              <SendIcon />
            </IconButton>
            </InputAdornment>
          )}
        sx={{ p:1, borderRadius: '15px',mt:2 }}
        />
        )}
    {inputMode === 'audio' && (
      <Box sx={{ mt:2}}>
        <RecordCard />
      </Box>
    )}
    </Card>
  );
};

export default ConversationCard;
