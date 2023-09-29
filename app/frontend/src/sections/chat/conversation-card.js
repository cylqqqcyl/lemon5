import React, {useState} from 'react';
import { Card, Box,
    Typography, Avatar, 
    OutlinedInput, InputAdornment, 
    IconButton, ToggleButton, ToggleButtonGroup } from '@mui/material';
import UserIcon from '@mui/icons-material/Person';
import SendIcon from '@mui/icons-material/Send';
import NewConvIcon from '@mui/icons-material/Add';
import { ConversationAudio } from './conversation-audio';
import { RecordCard } from '../voices/record-card';
import { CustomSnackbar } from '../message/custom-snackbar';

import { voiceAvatarMap } from '../voices/constants';

export const ConversationCard = ({ messages, setMessages, selectedCharacter }) => {
    const [inputValue, setInputValue] = useState('');  // State to keep track of input value
    const [inputMode, setInputMode] = useState('text');  // State to track input mode
    const [wasRecording, setWasRecording] = useState(false);  // State variable to keep track of previous recording state
    const [snackbarConfig, setSnackbarConfig] = useState({ message: '', type: '' });

    const handleInputChange = (event) => {
        setInputValue(event.target.value);  // Update input value
    };

    const handleSendClick = async () => {
      setSnackbarConfig({ message: '', type: '' });
      const newMessage = {
        sender: 'user',
        text: inputValue,
        mode: 'text',
      };
  
      // 先将用户的消息添加到对话中
      setMessages([...messages, newMessage]);

      // 重置输入值
      setInputValue('');
  
      // 向后端发送请求
      try {
        const response = await fetch('https://3023c993.r9.cpolar.top/chat', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ 
            prompt: inputValue,
            character: selectedCharacter
          }),
        });
        console.log('selectedCharacter', selectedCharacter)
        

        const responseData = await response.json();
        const noiseValue = 0.5
        const sdpValue = 0.2
        const noisewValue = 0.9
        const formatValue = 'wav'
        const lengthValue = 1
        if (responseData && responseData.response) {

          console.log('response', responseData.response)

          const response_tts = await fetch(
            `https://3b7259cf.r16.cpolar.top/genshinAPI?speaker=${selectedCharacter}&text=${responseData.response}&format=${formatValue}&length=${lengthValue}&noise=${noiseValue}&noisew=${noisewValue}&sdp=${sdpValue}`
            , {
              method: 'GET'
            });
          if (response_tts.ok) {
            const audioBlob = await response_tts.blob();
            const response_audio = URL.createObjectURL(audioBlob);
                        
            const botMessage = {
              sender: responseData.character || 'Bot',  // 此处需要确定后端返回的角色字段名
              text: responseData.response,
              mode: responseData.mode || 'audio', 
              audioURL: response_audio, // 此处需要确定后端返回的模式字段名
            };
            
            setMessages((prevMessages) => [...prevMessages, botMessage]);
          } else {
            console.error('Error fetching audio:', response_tts.statusText);
          }  
        }
  
      } catch (error) {
        console.error('Error sending message:', error);
        setSnackbarConfig({ message: 'Error sending message:', type: 'error' });
      }

  
    };


    const handleRecordClick = (recording, recordURL) => {
      if (recording) {
        setWasRecording(true);  // Update wasRecording state when recording starts
      } else if (!recording && wasRecording && recordURL) {
        // Only add the message if the state has transitioned from recording to stop
        const newMessage = {
          sender: 'user',
          text: '[语音消息]',
          mode: 'audio',
          audioURL: recordURL,
        };
        
        setMessages((prevMessages) => [...prevMessages, newMessage]);
        setWasRecording(false);  // Reset for the next recording cycle
      }
      else {
        setWasRecording(false);  // Reset for the next recording cycle
      }
    };

  
    const handleNewConvClick = () => {
        // Handle new conversation button click
        setMessages([]);  // Clear messages
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
              bordercolor="success.main"
              sx={{borderRadius: '15px', border: '2px solid', 
              color: 'success.main', mb: 2,}}
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
              {message.mode === 'audio' && (
                <ConversationAudio
                  id={index} 
                  audioUrl={message.audioURL}
                />
              )}
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
        <RecordCard handleRecordClickOverride={handleRecordClick}/>
      </Box>
    )}
    </Card>
  );
};

export default ConversationCard;